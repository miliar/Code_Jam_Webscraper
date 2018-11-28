#include<iostream>
using namespace std;
int i[10000][2],b[10000][4];
int main()
{
	int a,data,cnt,n,v,i1;
	scanf("%d",&data);
	cnt=0;
begin: data--; cnt++; printf("Case #%d: ",cnt);
	scanf("%d%d",&n,&v);
	for(a=0;a<(n-1)/2;a++) scanf("%d %d",&i[a][0],&i[a][1]);
	for(a=(n-1)/2;a<n;a++){ scanf("%d",&i1); b[a][i1]=0; b[a][1-i1]=100000; }
	for(a=(n-1)/2-1;a>=0;a--)
	{
		b[a][0]=min(min(b[2*a+1][0]+b[2*a+2][1],b[2*a+1][1]+b[2*a+2][0]),b[2*a+1][0]+b[2*a+2][0]);
		b[a][1]=b[2*a+1][1]+b[2*a+2][1];
		b[a][2]=b[2*a+1][0]+b[2*a+2][0];
		b[a][3]=min(min(b[2*a+1][0]+b[2*a+2][1],b[2*a+1][1]+b[2*a+2][0]),b[2*a+1][1]+b[2*a+2][1]);
//printf("%d:%d:%d:%d:%d\n",a,b[a][0],b[a][1],b[a][2],b[a][3]);
		if( i[a][1]==0 )
		{
			if( i[a][0]==0 ){ b[a][0]=b[a][2]; b[a][1]=b[a][3]; }
		}
		else
		{
			if( i[a][0]==0 ){ b[a][0]++; b[a][1]++; }
			if( i[a][0]==1 ){ b[a][2]++; b[a][3]++; }
			b[a][0]=min(b[a][0],b[a][2]);
			b[a][1]=min(b[a][1],b[a][3]);
		}
	}
	if( b[0][v]>n ) printf("IMPOSSIBLE\n");
	else printf("%d\n",b[0][v]);
	if( data>0 ) goto begin;
	return 0;
}
