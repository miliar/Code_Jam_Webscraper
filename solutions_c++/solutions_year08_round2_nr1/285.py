#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <list>
#include <deque>
#include <stack>
#include <sstream>
#include <fstream>

#define ll long long int
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define RFOR(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define RREP(i,n) RFOR(i,0,n)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define V(x) vector< x >
#define vi V(int)
#define vs V(string)
#define pb push_back
#define mkp make_pair
#define PII pair <int,int>
#define uli unsigned long long int
#define GI ({int t;scanf("%d",&t);t;})
#define SORT(X) sort(x.begin(),x.end())
const int INF = (int)1<<30;

using namespace std;

int main() {	int T=GI;
	REP(t,T) {
		ll n,ans=0LL,A,B,C,D,X0,Y0,M,x[100001],y[100001];
		cin>>n>>A>>B>>C>>D>>X0>>Y0>>M;
		x[0]=X0;y[0]=Y0;
		ll mp[3][3];
		REP(i,3)REP(j,3)mp[i][j]=0LL;
		FOR(i,1,n) {
			x[i]=(A*x[i-1]+B)%M;
			y[i]=(C*y[i-1]+D)%M;
		}
		REP(i,n)mp[x[i]%3][y[i]%3]++;
		REP(i,9)
			FOR(j,i+1,9)
				FOR(k,j+1,9)
					if((i/3+j/3+k/3)%3==0 && (i+j+k)%3==0) ans+=mp[i/3][i%3]* mp[j/3][j%3] * mp[k/3][k%3];
//		REP(i,9)
	//		FOR(j,i+1,9)
		//		if(((i/3)*2+j/3)%3==0 && (2*i+j)%3==0 && mp[i/3][i%3]>=2) ans+=mp[i/3][i%3]* mp[j/3][j%3] * (mp[i/3][i%3]-1) / 2LL;
		REP(i,9) 
			if(mp[i/3][i%3]>=3) ans+=(mp[i/3][i%3])*(mp[i/3][i%3]-1)*(mp[i/3][i%3]-2)/6LL;
		cout<<"Case #"<<t+1<<": "<<ans<<endl;
	}
	return 0;
}
