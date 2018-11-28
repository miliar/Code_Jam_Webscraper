#include <cstdio>

int i,j,k,s,t,n,m,tar,T;
int opt[20000][2];
const int oo=100000000;
struct node{
	int x,y;
}a[20000];
void calc(int nu,int ta){
	if (opt[nu][ta]!=-1) return ;
	opt[nu][ta]=oo;
	if (nu*2<n){
		calc(nu*2,0);
		calc(nu*2,1);
		calc(nu*2+1,0);
		calc(nu*2+1,1);
		if (a[nu].x==1){
			if (ta==1)
				opt[nu][ta]<?=opt[nu*2][1]+opt[nu*2+1][1];
			else 
				opt[nu][ta]<?=opt[nu*2][0]+opt[nu*2+1][1]<?(opt[nu*2][1]+opt[nu*2+1][0]<?opt[nu*2+1][0]+opt[nu*2][0]);
		}
		else{
			if (ta==1)
				opt[nu][ta]<?=opt[nu*2][1]+opt[nu*2+1][0]<?opt[nu*2][0]+opt[nu*2+1][1]<?opt[nu*2][1]+opt[nu*2+1][1];
			else opt[nu][ta]<?=opt[nu*2][0]+opt[nu*2+1][0];
		}
		if (a[nu].y==1){
			if (a[nu].x==1){
				if (ta==1) opt[nu][ta]<?=opt[nu*2][0]+opt[nu*2+1][1]+1<?opt[nu*2][1]+opt[nu*2+1][0]+1;
			}
			else
				if (ta==0) opt[nu][ta]<?=opt[nu*2][0]+opt[nu*2+1][1]+1<?opt[nu*2][1]+opt[nu*2+1][0]+1;
		}
	}
	else if (ta==a[nu].x) opt[nu][ta]=0; else opt[nu][ta]=oo;
}
main()
{
	scanf("%d",&T);
	int I=0;
	while (T--)
	{
		scanf("%d%d",&n,&tar);
		for (i=1;i<=(n-1)/2;++i)
			scanf("%d%d",&a[i].x,&a[i].y);
		for (i=(n-1)/2+1;i<=n;++i)
			scanf("%d",&a[i].x);
		for (i=1;i<=n;++i)
			for (j=0;j<=1;++j)
				opt[i][j]=-1;
		calc(1,tar);
		printf("Case #%d: ",++I);
		if (opt[1][tar]>=oo) printf("IMPOSSIBLE\n");
		else printf("%d\n",opt[1][tar]);
	}
	return 0;
}
