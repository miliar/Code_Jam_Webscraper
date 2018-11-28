#include<cstdio>
#include<algorithm>
using namespace std;
int T,n,v,b[105],o[105],O,B,i,j,k,t,k1,k2,auxo,auxb;
char c[105];
int main(){
	freopen("bottrust.in","r",stdin);
	freopen("bottrust.out","w",stdout);
	scanf("%d",&T);
	for(i=1;i<=T;++i){
		scanf("%d ",&n);
		for(j=1;j<=n;++j){
			scanf("%c%d ",&c[j],&v);
			if(c[j]=='B'){
				++k;
				b[k]=v;
			}
			else{
				++k;
				o[k]=v;
			}
		}
		O=1;
		B=1;
		t=0;
		auxo=0;
		auxb=0;
		for(j=1;j<=n;++j){
			if(c[j]=='O'){
				for(k=1;k<=t-auxo;++k){
					if(O>o[j]){
						--O;
					}
					if(O<o[j]){
						++O;
					}
				}
				t+=(max(o[j],O)-min(o[j],O)+1);
				O=o[j];
				auxo=t;
			}
			if(c[j]=='B'){
				for(k=1;k<=t-auxb;++k){
					if(B>b[j]){
						--B;
					}
					if(B<b[j]){
						++B;
					}
				}
				auxb=t;
				t+=(max(b[j],B)-min(b[j],B)+1);
				B=b[j];
				auxb=t;
			}
		}
		printf("Case #%d: %d\n",i,t);
		k=0;
	}
	return 0;
}