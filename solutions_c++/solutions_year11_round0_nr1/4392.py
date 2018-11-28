#include<stdio.h>
#include<string.h>
struct seq{int a,b;};
int main(){
	int cs;
	scanf("%d",&cs);
	for(int ct=1;ct<=cs;ct++){
		int n;
		scanf("%d",&n);getchar();
		seq a[n],b[n];
		memset(a,0x7f,sizeof(a));
		memset(b,0x7f,sizeof(b));
		int ctra=0,ctrb=0;
		for(int i=1;i<=n;i++){
			char c;int y;
			scanf("%c %d",&c,&y);getchar();
			if(c=='O'){
				a[ctra++]=(seq){y,i};
				a[ctra]=(seq){y,n+5};
			}else{
				b[ctrb++]=(seq){y,i};
				b[ctrb]=(seq){y,n+5};
			}
		}
		int ans=0,cura=0,curb=0,posa=1,posb=1;
		while(cura<ctra||curb<ctrb){
			bool xx=0,yy=0;
			if(cura<ctra){
				if(posa<a[cura].a){//move to a+1
					posa++;
					//puts("move to a+1");
				}
				else if(posa>a[cura].a){//move to a-1
					posa--;
					//puts("move to a-1");
				}
				else if(a[cura].b<b[curb].b){ //kl bs push
					//cura++;
					xx=1;
				}
				//puts("a jln");
			}
			if(curb<ctrb){
				if(posb<b[curb].a){//move to b+1
					posb++;
					//printf("move to b+1=%d\n",posb);
				}
				else if(posb>b[curb].a){ //move to b-1
					posb--;
					//puts("move to b-1");
				}
				else if(a[cura].b>b[curb].b){ //kl bs push
					//curb++;
					yy=1;
					//puts("b push");
				}//else puts("ASDASDASD");

				//puts("b jln");
			}
			if(xx){
				cura++;
				//puts("a push");
			}
			if(yy){
				curb++;
				//puts("b push");
			}
			ans++;
			//printf("%d %d\n",a[cura].b,b[curb].b);getchar();
			//printf("%d %d\n",curb,ctrb);getchar();
			//printf("%d\n",ans);getchar();
			//puts("");
		}
		printf("Case #%d: %d\n",ct,ans);
	}
	return 0;
}
