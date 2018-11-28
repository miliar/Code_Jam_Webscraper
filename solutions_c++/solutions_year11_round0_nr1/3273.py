#include <cstdio>

using namespace std;
int t,n;

int max(int a, int b){
	return (a>b)?a:b;
}
int abs(int a){
	return (a>0)?a:(-a);
}
int main(){
	freopen("robo.in","r",stdin);
	freopen("robo.out","w",stdout);
	scanf("%d",&t);
	for (int i=0;i<t;i++){
		int ans=0;
		int ot=0, bt=0;
		int op=1, bp=1;
		scanf("%d",&n);
		//printf("!!!%d!\n",n);
		for (int j=0;j<n;j++){
			int p;
			char c;
			scanf(" %c %d",&c,&p);
			//printf("%c %d \n",c,p);
			if (c=='O'){
				ans=1+max(bt,ot+abs(p-op));
				ot=1+max(bt,ot+abs(p-op));
				op=p;
			}
			if (c=='B'){
				ans=1+max(ot,bt+abs(p-bp));
				bt=1+max(ot,bt+abs(p-bp));
				bp=p;
			}
		}
		printf("Case #%d:  %d\n",i+1,ans);
	}
}