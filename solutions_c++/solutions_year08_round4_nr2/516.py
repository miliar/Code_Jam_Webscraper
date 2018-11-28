#include<iostream>
using namespace std;

int m,n,s;
int x1,x2,y1,y2;
int search()
{
	int temp;
	for(x1=0;x1<=m;x1++)
	for(y1=0;y1<=n;y1++)
	for(x2=0;x2<=m;x2++)
	for(y2=0;y2<=n;y2++)
	{
		temp=x1*y2-x2*y1;
		if(temp<0)
			temp=-temp;
		if(temp==s)
			return 1;
	}
	return 0;
}


int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	int i,j,k,seq,num;
	scanf("%d",&num);
	for(seq=1;seq<=num;seq++)
	{
		scanf("%d %d %d" ,&m,&n,&s);
		printf("Case #%d:",seq);
		if(m*n<s)
		{
			printf(" IMPOSSIBLE\n");
			continue;
		}
		if(search())
			printf(" 0 0 %d %d %d %d\n",x1,y1,x2,y2);
		else printf(" IMPOSSIBLE\n");
	}
	return 0;
}
