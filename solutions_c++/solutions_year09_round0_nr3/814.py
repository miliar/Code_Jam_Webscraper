#include<iostream>
using namespace std;

#define M 10000

int a[20];
char c[600];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("c.out","w",stdout);
	int t,T=0,i;
	char ch;
	scanf("%d",&t);
	while((ch=getchar())!='\n');
	while(t--)
	{
		scanf("%[^\n]%*c",c);
		memset(a,0,sizeof(a));
		for(i=0;c[i];i++)
		{
			if(c[i]=='w')
				a[0]=(a[0]+1)%M;
			else if(c[i]=='e')
			{
				a[1]=(a[0]+a[1])%M;
				a[6]=(a[5]+a[6])%M;
				a[14]=(a[13]+a[14])%M;
			}
			else if(c[i]=='l')
			{
				a[2]=(a[1]+a[2])%M;
			}
			else if(c[i]=='c')
			{
				a[3]=(a[2]+a[3])%M;
				a[11]=(a[10]+a[11])%M;
			}
			else if(c[i]=='o')
			{
				a[4]=(a[3]+a[4])%M;
				a[9]=(a[8]+a[9])%M;
				a[12]=(a[11]+a[12])%M;
			}
			else if(c[i]=='m')
			{
				a[5]=(a[4]+a[5])%M;
				a[18]=(a[17]+a[18])%M;
			}
			else if(c[i]==' ')
			{
				a[7]=(a[6]+a[7])%M;
				a[10]=(a[9]+a[10])%M;
				a[15]=(a[14]+a[15])%M;
			}
			else if(c[i]=='t')
			{
				a[8]=(a[7]+a[8])%M;
			}
			else if(c[i]=='d')
			{
				a[13]=(a[12]+a[13])%M;
			}
			else if(c[i]=='j')
			{
				a[16]=(a[15]+a[16])%M;
			}
			else if(c[i]=='a')
			{
				a[17]=(a[16]+a[17])%M;
			}
		}
		printf("Case #%d: ",++T);
		printf("%04d\n",a[18]);

	}
	return 0;
}