#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int a[30],aa,b[30],bb,c[30],cc;
bool cmp(int x[],int xx,int y[],int yy)
{
	int i;
	if(xx>yy)
		return true;
	else if(xx<yy)
		return false;
	for(i=xx-1;i>=0;i--)
		if(x[i]>y[i])
			return true;
		else if(x[i]<y[i])
			return false;
	return false;
}
bool cm(const int &a,const int &b)
{
	return a>b;
}
int main()
{
	int t,i,j,k,dd,cas,best;
	char ccc[30];
	unsigned long long n;
	scanf("%d",&cas);
	for(dd=1;dd<=cas;dd++)
	{
		scanf("%s",ccc);
		bb=aa=strlen(ccc);
		for(j=aa-1;j>=0;j--)
			b[bb-j-1]=a[aa-j-1]=ccc[j]-'0';
		for(i=0;i<bb-1;i++)
			if(b[i]>b[i+1])
				break;
		if(i!=bb-1)
		{
			k=10;
			for(j=0;j<=i;j++)
				if(b[j]>b[i+1]&&b[j]<k)
				{
					k=b[j];
					best=j;
				}
			swap(b[best],b[i+1]);
			sort(b,b+i+1,cm);
		}
		else
		{
			k=10;
			for(j=0;j<bb;j++)
				if(b[j]!=0&&b[j]<k)
				{
					k=b[j];
					best=j;
				}
			b[bb++]=0;
			swap(b[best],b[bb-1]);
			sort(b,b+bb-1,cm);
		}
		printf("Case #%d: ",dd);
		for(i=bb-1;i>=0;i--)
			printf("%d",b[i]);
		printf("\n");
	}
}
