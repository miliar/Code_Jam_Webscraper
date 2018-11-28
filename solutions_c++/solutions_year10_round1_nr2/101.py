
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int re[110][260];
int da[110];
int d,ii,m,n;
int sjr(int a,int b)
{
	if(re[a][b]!=-1)
		return re[a][b];
	if(a==n)
		return re[a][b]=0;
	re[a][b]=d+sjr(a+1,b);
	int i,j;
	for(i=0;i<256;i++)
	{
		if(abs(b-i)==0)
			j=0;
		else if(m==0)
			continue;
		else
			j=(abs((b-i))-1)/m;
		re[a][b]=min(re[a][b],ii*j+abs(i-da[a])+sjr(a+1,i));
	}
	return re[a][b];
}
int main()
{
	freopen("b2.txt","r",stdin);
	freopen("ob2.txt","w",stdout);
	int y,z,i,j,k,l;
	scanf("%d",&z);
	for(y=1;y<=z;y++)
	{
		scanf("%d%d%d%d",&d,&ii,&m,&n);
		for(i=0;i<n;i++)
			scanf("%d",da+i);
		memset(re,-1,sizeof(re));
		//printf("%d",sjr(1,132));
		j=sjr(0,0);
		for(i=1;i<256;i++)
			j=min(j,sjr(0,i));
		printf("Case #%d: %d\n",y,j);
	}
	return 0;
}
