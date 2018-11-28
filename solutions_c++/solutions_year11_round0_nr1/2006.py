#include<stdio.h>
#include<malloc.h>
typedef struct {
	int val;
	char ch;
}array;
int main(){
	int T;
	int n;
	array *a;
	int O[101],B[101];
	int i,j,k;
	int indexo,indexb,indexa;
	char ch;	
int o,b;
	scanf("%d",&T);
	int yash;
	int ans;
	int nexto,nextb,poso,posb;
	for(yash=1;yash<=T;yash++){
		ans=0;
		scanf("%d",&n);
		a=(array*)malloc(sizeof(array)*n);
		indexo=0;
		indexb=0;
		for(i=0;i<n;i++){
			ch='Q';
			while(ch!='O'&&ch!='B'){
				scanf("%c",&ch);
			}
			scanf("%d",&k);
			a[i].ch=ch;
			a[i].val=k;
			if(ch=='O')
			{       O[indexo]=k;
				indexo++;
			}
			else if(ch=='B'){B[indexb]=k;indexb++;}
		}
		poso=1;
		posb=1;
		nexto=0;
		nextb=0;
		indexa=0;
		int timer;
		while(indexa!=n){
			if(a[indexa].ch=='O'){
				timer=0;
				if(poso<a[indexa].val){
					while(poso!=a[indexa].val){poso++;timer++;}
				}
				else if(poso>a[indexa].val){while(poso!=a[indexa].val){poso--;timer++;}}
				timer++;
				if(nextb<indexb&&posb<B[nextb]){for(j=0;j<timer&&posb<B[nextb];j++)posb+=1;}
				if(nextb<indexb&&posb>B[nextb]){for(j=0;j<timer&&posb>B[nextb];j++)posb-=1;}
				indexa++;
				ans+=timer;
				nexto++;
			}
			else if(a[indexa].ch=='B'){
				timer=0;
				if(posb<a[indexa].val){
					while(posb!=a[indexa].val){posb++;timer++;}
				}
				else if(posb>a[indexa].val){while(posb!=a[indexa].val){posb--;timer++;}}
				timer++;
				if(nexto<indexo&&poso<O[nexto]){for(j=0;j<timer&&poso<O[nexto];j++)poso+=1;}
				if(nexto<indexo&&poso>O[nexto]){for(j=0;j<timer&&poso>O[nexto];j++)poso-=1;}
				indexa++;
				ans+=timer;
				nextb++;
			}
		}

		printf("Case #%d: %d\n",yash,ans);
	}
	return 0;
}
