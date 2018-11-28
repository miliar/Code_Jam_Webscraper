#include<iostream>
#include<sstream>
#include<vector>
#include<map>
#include<string>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<queue>
#include<stack>
#define INF (1<<29)
#define EPS (1e-14)
#define two(a) (1<<(a))
#define sca(t) scanf("%d",&t)
#define scal(t) scanf("%lld",&t)
#define rep(a,b) for(a=0 ; a<b ; ++a)
#define xrep(a,b,c) for(a=b ; a<c ; ++a)
#define limit 1000100
typedef long long ll;
using namespace std;

int del[limit+1000],pri[limit],plen;

int main(){
	freopen("C-large.in","r",stdin);
	freopen("pcbig.txt","w",stdout);
	int i,j,k,t,tt;
	ll n;
	cin >> t;
	for(tt=1 ; tt<=t ; tt++){
		cin >> n;
		for(i=5 ; i*i<=limit ; i+=4){         //limit為限定值,建質數表
			if(!del[i]) for(j=i*i ; j<=limit ; j+=i) del[j]=1;   i+=2;
			if(!del[i]) for(j=i*i ; j<=limit ; j+=i) del[j]=1;
		}
		pri[0]=2,pri[1]=3,plen=2;   //後面為取出質數所需
		for(i=5 ; i<=limit ; i+=4){
				if(!del[i]) pri[plen++]=i;   i+=2;
				if(!del[i]) pri[plen++]=i;
		}
		int a(0),b(0);
		for(i=0 ; i<plen ; i++){
			if(pri[i]<=n){
				ll nn=n;
				a++;
				while(nn>=pri[i]){
					b++;
					nn/=pri[i];
				}
			}
		}
		if(n!=1) b++;
		cout <<"Case #" << tt << ": " <<  b-a << endl;
		
	}
}
