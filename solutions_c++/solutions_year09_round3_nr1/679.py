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

int solve(){
	gets(buffer);
	string tmp;
	stringstream ss(buffer);
	ss>>tmp;
	set < char > chars;
	map <char,int> val;
	bool f,s;
	f=true;
	s=false;
	for(int i=0;i<tmp.size();i++){
		if(chars.find(tmp[i])==chars.end()){
			if(f){ val[tmp[i]]=1; f=false; s=true;chars.insert(tmp[i]); continue; };
			if(s){ val[tmp[i]]=0; f=false; s=false;chars.insert(tmp[i]); continue; };
			val[tmp[i]]=chars.size();
			chars.insert(tmp[i]);
		};
		
	};
	int b =chars.size();
	if(b==1) b++;
	long long sum=0;
	for(int i=0; i<tmp.size();i++){
		//chars.insert(tmp[i]);
		//printf("%c %d power %d\n",tmp[i],val[tmp[i]],tmp.size()-1-i);
		sum+= val[tmp[i]] * pow( b +0.0, tmp.size()-1-i+0.0 );
	};
	printf("%d\n", sum);
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
