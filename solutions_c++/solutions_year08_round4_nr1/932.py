#include <stdio.h>
const int MAXVALUE=500000;
bool a[50000][2];
int num[50000][2];
int N,M,V,G,C;

int max(int x,int y)
{
	if(x>y) return x;
	else return y;
}
int min(int x,int y)
{
	if(x>y)return y;
	else return x;
}

void func(int index)
{
	if(index*2>M) return ;
	int l=index*2,r=l+1;
	func(l);
	func(r);
	if(a[index][0]==true){			//and
		num[index][0]=min(num[l][0]+min(num[r][0],num[r][1]),num[r][0]+min(num[l][0],num[l][1]));
		num[index][1]=num[l][1]+num[r][1];
		if(a[index][1]==true){	//changable
			num[index][1]=min(num[index][1],min(num[l][0]+num[r][1],num[l][1]+num[r][0])+1);
		}
	}
	else{
		num[index][1]=min(num[l][1]+min(num[r][0],num[r][1]),num[r][1]+min(num[l][0],num[l][1]));
		num[index][0]=num[l][0]+num[r][0];
		if(a[index][1]==true){	//changable
			num[index][0]=min(num[index][0],min(num[l][0]+num[r][1],num[l][1]+num[r][0])+1);
		}
	}
}

int main()
{
	int i,j,k;
	int b;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&N);
	for(i=1; i<=N; i++){
		scanf("%d%d",&M,&V);
		b=(M-1)/2;
		for(j=1; j<=b; j++){
			scanf("%d%d",&G,&C);
			a[j][0]=(bool)G;
			a[j][1]=(bool)C;
			num[j][0]=MAXVALUE;
			num[j][1]=MAXVALUE;
		}
		for(; j<=M; j++){
			scanf("%d",&k);
			num[j][k]=0;
			num[j][1-k]=MAXVALUE;
		}
		func(1);
		printf("Case #%d: ",i);
		if(num[1][V]>=MAXVALUE)printf("IMPOSSIBLE\n");
		else printf("%d\n",num[1][V]);
	}
	return 0;
}


