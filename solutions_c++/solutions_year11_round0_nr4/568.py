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
	freopen("D-large.in","r",stdin);
	freopen("pdbigout.txt","w",stdout);
	int ans,v,in,t,tt,n,i;
	cin >> tt;
	for(t=1 ; t<=tt ; t++){
		cin >> n;
		ans=0;
		for(i=1 ; i<=n ; i++){
			cin >> v;
			if(v!=i) ans++;
		}
		cout << "Case #" << t << ": " << ans << ".000000" << endl;
	}
}

