#pragma comment(linker, "/STACK:65777216")

#include <algorithm>
#include <iostream>
#include <string>
#include<sstream>
#include<string.h>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include<stack>
#include <set>
#include <map>
#include<ctime>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef unsigned long long ull;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back

const int  mod = 1000003;

int n,m;
string s[111];
int a[111][111];

int main(){ 
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	int tc;
	cin>>tc;
	REP(TC,tc){
		cin>>n>>m;
		REP(i,n) cin>>s[i];
		int t = n*m;

		int res = 0;
		REP(mask,1<<t){
			REP(i,n) REP(j,m) a[i][j]=0;
			bool good = 1;
			REP(i,n)REP(j,m){
				int dx=-1,dy;
				if(s[i][j]=='|') dx = -1 ,dy = 0;
				if(s[i][j]=='-') dx = 0 ,dy = 1;
				if(s[i][j]=='/') dx = -1, dy = 1;
				if(s[i][j]=='\\') dx = 1, dy = 1;
				if(mask&(1<<(i*m+j))) dx*=(-1),dy*=(-1);

				int nx = i + dx;
				int ny = j + dy;
				nx = (nx + n ) %n;
				ny = (ny + m) % m;

				a[nx][ny]++;
				if(a[nx][ny]>1) {good=0;break;}
			}
			if(good) res++;
		}

		printf("Case #%d: %d\n",TC+1,res);
	}
#ifdef LocalHost
	//cout<<endl<<endl<<"TIME: "<<clock()<<endl;
#endif
	return 0;
}
