#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdio>
#include <cctype>
#include <cassert>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define sz size()
#define pb push_back
#define GI ({int t;scanf("%d",&t);t;})
#define INF int(1e9)

typedef long long LL;
typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;

string b="welcome to code jam";
string a;
int mem[520][20];

#define MOD (int)1e4

int go(int i,int j){
	if(j>=b.sz)	return 1;
	if(i>=a.sz)	return 0;
	int & ret=mem[i][j];
	if(ret!=-1)	return ret;
	ret=0;
	if(a[i]==b[j])	(ret+=go(i+1,j+1))%=MOD;	
	(ret+=go(i+1,j))%=MOD;
	return ret;
}

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int Kase;cin>>Kase;cin.get();
	FOR(kase,1,Kase+1){
		getline(cin,a);
		REP(i,520)	REP(j,20)	mem[i][j]=-1;
		int r=go(0,0);
		char buf[6];
		sprintf(buf,"%d",r);
		string z=buf;
		while(z.sz<4)	z="0"+z;
		printf("Case #%d: %s\n",kase,z.c_str());
	}
	
//	GI;
	return 0;
}
