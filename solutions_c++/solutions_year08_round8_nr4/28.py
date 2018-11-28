

#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set> 
#include<queue>
#include<string>
#include<stack>
#include<sstream>
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it) 
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) cerr << #x << " = "; FOREACH(it,(x)) cerr << *it << ","; cerr << "\n"; 
#define fup(i,a,b) for(int i=a;i<=b;i++)
#define fdo(i,a,b) for(int i=a;i>=b;i--)
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) (int)a.size()
#define inf 1000000000
#define SQR(a) ((a)*(a))
#define maxn 1005
using namespace std;

typedef long long int64;
const int64 mod=30031;
int n,k,p;
int64 ile[maxn][(1<<11)];
int main(){
	int cas;cin>>cas;
	fup(c,1,cas){
		memset(ile,0,sizeof(ile));
		cin>>n>>k>>p;
		int sum=0;
		fup(i,0,k-1)sum+=(1<<i);
		ile[k][sum]=1;
		fup(i,k,n-1){
			fup(j,0,(1<<p)-1){
				ile[i][j]%=mod;
				if(ile[i][j]==0)continue;
				int mask=j;
				if(mask&(1<<(p-1))){
					int nmask=mask^(1<<(p-1));
					nmask<<=1;
					nmask|=(1<<0);
					ile[i+1][nmask]+=ile[i][mask];
					continue;	
				}
				fup(j,0,p-1){
					if(mask&(1<<j)){
						int nmask=mask^(1<<j);
						nmask<<=1;
						nmask|=(1<<0);
						ile[i+1][nmask]+=ile[i][mask];
					}
				}
			}
		}
		int64 wyn=ile[n][sum]%mod;
		int w=wyn;
		printf("Case #%d: %d\n",c,w);

	}		
	return 0;	
}
