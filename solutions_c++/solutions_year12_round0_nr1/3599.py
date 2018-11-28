#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
const int maxn=1100;
char Mp[]="yhesocvxduiglbkrztnwjpfmaq";
int tt,n,Run;
char a[maxn],b[maxn];

namespace Ninit{
	void init(){
		scanf(" "),gets(a);
		n=strlen(a);
	}
}

namespace Nsolve{
	void solve(){
		int i;
		for(i=0;i<n;++i)
			if(islower(a[i]))b[i]=Mp[a[i]-'a'];
			else b[i]=a[i];
		b[n]=0;
		printf("Case #%d: %s\n",Run,b);
	}
}

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("love.out","w",stdout);
	for(cin>>tt,Run=1;tt;--tt,++Run){
		Ninit::init();
		Nsolve::solve();
	}
	fclose(stdout);
	return 0;
}
