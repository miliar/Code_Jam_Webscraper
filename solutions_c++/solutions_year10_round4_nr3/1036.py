#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#define oo 105

int a[oo][oo];
int Test,n,now,x1,x2,y1,y2;


void Solve()
{
	for (int t=1;;++t){
		if (Test<100){
			int xp=0;
		}
		now=0;
		for (int i=100;i>=1;--i)
		for (int j=100;j>=1;--j){
			if (!a[i][j]) a[i][j]=a[i-1][j] & a[i][j-1];
			else a[i][j]=a[i-1][j] | a[i][j-1];
			now+=a[i][j];
		}
		if (!now){
			printf("%d\n",t);
			return;
		} 
	}
}


int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	
	scanf("%d",&Test);
	for (int i=1;i<=Test;++i){
		scanf("%d",&n);
		memset(a,0,sizeof(a));
		for (int j=1;j<=n;++j){
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (int y=y1;y<=y2;++y)
			for (int x=x1;x<=x2;++x)
				a[y][x]=1;
		}
		printf("Case #%d: ",i);
		Solve();
	}
	
	
	return 0;
}
