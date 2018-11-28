#include<cstdio>
#include<cstring>
struct node{
	int ty[3];
	int pos;
}p[105];
int n;

int ABS(int a){
	if(a>=0) return a;
	return -a;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cas;
	int r=1;
	scanf("%d",&cas);
	while(cas--){
		scanf("%d",&n);
		for(int i=0; i<n; i++){
			scanf("%s%d",p[i].ty, &p[i].pos);
		}
		//printf("%d\n",cas);
		
		int res=0;
		int posa=1,at=0,posb=1,bt=0;
		for(int i=0; i<n; i++){
			//printf("i= %d\n",i);
			
			int npos;
			int nd;
			int tt;
			if(p[i].ty[0]=='B'){
				npos=p[i].pos;
				nd=ABS(npos-posb);
				tt=(nd-bt);
				if(tt<0) tt=0;
				tt+=1;
				res+=tt;
				at+=tt;
				bt=0;
				posb=npos;
			}else{
				npos=p[i].pos;
				nd=ABS(npos-posa);
				tt=(nd-at);
				if(tt<0) tt=0;
				tt+=1;
				res+=tt;
				bt+=tt;
				at=0;
				posa=npos;
			}
		}
		printf("Case #%d: ",r++);
		printf("%d\n",res);
	}
}