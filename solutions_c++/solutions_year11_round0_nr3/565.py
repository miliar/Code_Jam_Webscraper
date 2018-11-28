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
#include<stdio.h>
#include<stdlib.h>
#define INF (1<<29)
#define EPS (1e-7)
#define two(a) (1<<(a))
#define rep(a,b) for(a=0 ; a<b ; ++a)
#define xrep(a,b,c) for(a=b ; a<c ; ++a)
#define sca(t) scanf("%d",&t)
#define scal(t) scanf("%lld",&t)
typedef long long ll;
using namespace std;

int main(){
	freopen("C-large.in","r",stdin);
	freopen("pcbigout.txt","w",stdout);
	int i,j,n,a,x,t,tt,ans,minx;
	cin >> tt;
	for(t=1 ; t<=tt ; t++){
		x=ans=0;
		minx=INF;
		cin >> n;
		rep(i,n){
			cin >> a;
			minx=min(minx,a);
			ans+=a;
			x^=a;
		}
		cout << "Case #" << t << ": " ;
		if(x!=0) cout << "NO" << endl;
		else cout << ans-minx << endl;
	}
}

