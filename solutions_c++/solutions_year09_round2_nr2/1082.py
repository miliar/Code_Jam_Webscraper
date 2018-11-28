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
#define SWAP(x,y) int t;t=x;x=y;y=t

#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 


char buffer[100];
long long N;
int tmp;

int solve(){
	gets(buffer);
	//sscanf(buffer, "%d %d", &Y , &X);	
	stringstream ss(buffer);
	string in;
	ss>>in;
	VI inp;
	for(int i=0;i<in.size();i++) {
		inp.PB(in[i]-'0');
	};
	
	reverse(ALL(inp));
	
	inp.PB(0);
	VI reste;
	for(int i=0;i<inp.size()-1;i++){
		reste.PB(inp[i]);
		sort(ALL(reste));
		if(inp[i+1]<reste[reste.size()-1]){
			int j=0;
			while(inp[i+1]>=reste[j]) j++;
			SWAP(inp[i+1],reste[j]);
			sort(ALL(reste));
			reverse(ALL(reste));
			for(int k=0;k<reste.size();k++) inp[k]=reste[k];
			break;
		};
	};
	reverse(ALL(inp));
	for(int i=0;i<inp.size();i++){
		if(i==0 && inp[0]==0) continue;
		printf("%d",inp[i]);
	};
	printf("\n");
	return 0;


};




int main(){
	
	freopen("/Users/nicolas/Desktop/input.txt","r",stdin);freopen("/Users/nicolas/Desktop/output.txt","w",stdout);
	gets(buffer);
	sscanf(buffer, "%d", &N);
	REP(i,N){
		printf("Case #%d: ",i+1);
		solve();
	};
	fflush(stdout);
	return 0;
}
