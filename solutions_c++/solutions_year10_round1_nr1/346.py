#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
const int BIG=0x3f3f3f3f;
#define cc(x) cout<<#x<<':'<<x<<endl;
#define MAX 51
char c[MAX][MAX],c2[MAX][MAX];
int dx[4]={1,0,1,-1},dy[4]={0,1,1,1};
bool ok(int x,int y,int n)
{
	return x>=0&&x<n&&y>=0&&y<n;
}
int main()
{
	int cs,i,j,i2,j2,xx,n,k,is,dd;
	scanf("%d",&cs);
	for(dd=1;dd<=cs;dd++)
	{
		memset(c2,'.',sizeof(c2));
		scanf("%d%d",&n,&k);
		for(is=i=0;i<n;i++)
			scanf("%s",c[i]);
		for(i=0;i<n;i++)
			for(xx=0,j=n-1;j>=0;j--)
				if(c[i][j]!='.')
					c2[i][xx++]=c[i][j];
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				if(c2[i][j]!='.')
					for(i2=0;i2<4;i2++)
					{
						for(j2=0;j2<k;j2++)
							if((!ok(i+j2*dx[i2],j+j2*dy[i2],n))||c2[i+j2*dx[i2]][j+j2*dy[i2]]!=c2[i][j])
								break;
						if(j2==k)
						{
							if(c2[i][j]=='B')
								is|=1;
							else
								is|=2;
						}
					}
		if(is==0)
			printf("Case #%d: Neither\n",dd);
		else if(is==1)
			printf("Case #%d: Blue\n",dd);
		else if(is==2)
			printf("Case #%d: Red\n",dd);
		else
			printf("Case #%d: Both\n",dd);
	}
}