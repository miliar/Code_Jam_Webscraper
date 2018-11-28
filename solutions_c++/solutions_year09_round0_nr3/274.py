#include<stdio.h>
#include<algorithm>
using namespace std;
const int mod=10000;
int z[512][20];
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	char our[]="welcome to code jam";
	char str[512];
	int c,o,i,j,len;
	scanf("%d",&c);
	gets(str);
	for(o=1;o<=c;o++)
	{
		gets(str);
		len=strlen(str);
		memset(z,0,sizeof(z));
		for(i=0;i<len;i++)
			for(j=0;j<19;j++)
			{
				if(i)
					z[i][j]=(z[i][j]+z[i-1][j])%mod;
				if(str[i]==our[j])
				{
					if(j)
					{
						if(i)
							z[i][j]=(z[i][j]+z[i-1][j-1])%mod;
					}
					else
						z[i][j]=(z[i][j]+1)%mod;
				}
			}
		printf("Case #%d: %04d\n",o,z[len-1][18]);
	}
	return 0;
}
				
