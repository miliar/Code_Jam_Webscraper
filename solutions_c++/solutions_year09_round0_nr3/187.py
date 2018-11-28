#include <istream>
using namespace std;

const char word[20]="welcome to code jam";
int a[30][600]={0};
char s[1000]={0};
int n,m,i,j,k,t,len,sum;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&n);
	gets(s);

	for (t=1; t<=n; t++)
	{
		gets(s);
		memset(a,0,sizeof(a));
		len = strlen(s);
		a[0][0] = 1;
		for (i=0; i<=18; i++)
			for (j=0; j<len; j++)
				if (s[j]==word[i])
				{
					for (k=-1; k<j; k++)
						a[i+1][j+1]+=a[i][k+1];
					a[i+1][j+1]%=10000;
				}
		sum = 0;
		for (j=0; j<len; j++)
			sum+=a[19][j+1];
		sum%=10000;
		printf("Case #%d: %.4d\n",t,sum);
	}
	return 0;
}