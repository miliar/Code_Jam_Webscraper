#include<stdio.h>
#include<memory.h>
#include<algorithm>
#include<math.h>
#include<stdlib.h>

int T;
struct Tp{
	int p,v;
} a[333333];
int n,ans,ch,k;


void add(int x,int y){
	for(int i=0;i<n;i++) if(a[i].p==x){
		a[i].v+=y;
		return;
	}
	a[n++].p=x;
	a[n-1].v=y;
}

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		scanf("%d",&n);
		ans=0;
		for(int i=0;i<n;i++)	scanf("%d%d",&a[i].p,&a[i].v);
		do{
			ch=0;
			for(int i=0;i<n;i++) if(a[i].v>1) { ch=1; break;}
			if(!ch) break;

			for(int i=0;i<n;i++)if(a[i].v>1){
				k=a[i].v>>1;
				ans+=k;
				a[i].v-=k<<1;
				add(a[i].p-1,k);
				add(a[i].p+1,k);
			}
		}while(1);
		
		printf("Case #%d: %d\n",_,ans);
	}
	return 0;
}
