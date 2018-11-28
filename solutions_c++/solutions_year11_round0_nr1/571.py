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
	freopen("A-large.in","r",stdin);
	freopen("paout.txt","w",stdout);
	int so,sb,ino,inb,i,j,n,ns,t,tt,ans;
	char c;
	cin >> tt;
	for(t=1 ; t<=tt ; t++){
		ans=0;
		cin >> n;
		so=sb=0;
		ino=inb=1;
		rep(i,n){
			int w=0,ww;
			cin >> c >> ns;
			if(c=='O'){
				w=abs(ino-ns);
				w=max(w-so,0);
				ans+=w+1;
				sb+=w+1;
				so=0;
				ino=ns;
			}
			else if(c=='B'){
				w=abs(inb-ns);
				w=max(w-sb,0);
				ans+=w+1;
				so+=w+1;
				sb=0;
				inb=ns;
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
}
