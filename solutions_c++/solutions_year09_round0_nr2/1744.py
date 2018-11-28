#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,pocz,koniec) for (int var=(pocz); var<=(koniec); ++var)
#define FORD(var,pocz,koniec) for (int var=(pocz); var>=(koniec); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 


char buffer[100];
int X, Y, N;

int heights[100][100];

string names="abcdefghijklmnopqrstuvwxyz";



int geth(int x, int y){
	if(x<0 || y<0) return 20000;
	if((x-X)*(y-Y)==0) return 20000;
	return heights[x][y];
};

PII next(PII current){
	PII out=current;
	//N
	if(geth(out.ST,out.ND)>geth(current.ST,current.ND-1)) out = make_pair(current.ST,current.ND-1);
	//W
	if(geth(out.ST,out.ND)>geth(current.ST-1,current.ND)) out = make_pair(current.ST-1,current.ND);
	//E
	if(geth(out.ST,out.ND)>geth(current.ST+1,current.ND)) out = make_pair(current.ST+1,current.ND);
	//S
	if(geth(out.ST,out.ND)>geth(current.ST,current.ND+1)) out = make_pair(current.ST,current.ND+1);
	
	return out;
};


int solve(){
	gets(buffer);
	sscanf(buffer, "%d %d", &Y , &X);
	for(int i=0; i<Y; i++){
		gets(buffer);
		stringstream ss(buffer);
		string buf;
		int j=0;
		while(ss>>buf){
			heights[j][i]=atoi(buf.c_str());
			j++;
		};
		//printf(buffer);
		//printf("\n");
		
	};
	string::iterator name=names.begin();
	map< PII, char > labels;
	REP(j,Y){
		REP(i,X){
			//printf("%d %d\n",i,j);
			if(labels.find(make_pair(i, j))!=labels.end()) continue;
			PII current = make_pair(i,j);
			PII n = next( current );
			//printf("going from %d %d (%d) to %d %d (%d) \n", current.ST,current.ND,geth(current.ST,current.ND),n.ST,n.ND,geth(n.ST,n.ND));
			while(n!=current){
				if(labels.find(n)!=labels.end()){
					//printf("set the label of pos %d %d",n.ST,n.ND);
					labels[make_pair(i, j)]=labels[n];
				};
					
				current=n;
				n=next(n);
				//printf("going from %d %d (%d) to %d %d (%d) \n", current.ST,current.ND,geth(current.ST,current.ND),n.ST,n.ND,geth(n.ST,n.ND));
				
				
			};
			//printf("sink found at %d %d \n",current.ST,current.ND);
			if(labels.find(n)==labels.end()){
				//printf("assigning label %c\n",*name);
				labels[n]=*name;
				labels[make_pair(i, j)]= *name;
				name++;
			};
		};
	};
	
	REP(j,Y){
		REP(i,X){
			printf("%c ",labels[make_pair(i, j)]);
		};
		printf("\n");
	};
	
	
	
	return 0;


};




int main(){
	
	freopen("/Users/nicolas/Desktop/input.txt","r",stdin);freopen("/Users/nicolas/Desktop/output.txt","w",stdout);
	gets(buffer);
	sscanf(buffer, "%d", &N);
	REP(i,N){
		printf("Case #%d:\n",i+1);
		solve();
	};
	fflush(stdout);
	return 0;
}
