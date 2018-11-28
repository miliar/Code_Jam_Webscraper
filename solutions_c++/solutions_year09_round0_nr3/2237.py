#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
const int N=505;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	char ch[20]={"welcome to code jam"};
	
	
	char p[N];
	int i,j,k,len;
	int a[N][20];
	int n;
	scanf("%d",&n);
	getchar();
	for(int ca=1;ca<=n;ca++)
	{
		cin.getline(p,N);
		memset(a,0,sizeof(a));
		len=strlen(p);
		if(p[0]==ch[0]) a[0][0]=1;
		else a[0][0]=0;
		int sum;

		for(i=1; i<len ;i++)
		{
			if(ch[0]==p[i]) a[i][0]=1;
			else a[i][0]=0;

			for(j=1;j<=i&&j<19;j++)
			{
				sum=0;
				if(ch[j]==p[i])
				{
					for(k=0;k<i;k++)
					{
						sum+=a[k][j-1];
						sum%=10000;
					}
				}
				a[i][j]=sum;
			}
		}
		sum=0;
		for(i=18;i<len;i++)
		{
			sum+=a[i][18];
			sum%=10000;
		}
		printf("Case #%d: %04d\n",ca,sum);
	}
	return 0;
}
