#include <iostream>
using namespace std;

char	Sen[1000];
char	Dict[20];
int		f[1000][20];
int		n,Len,Ans;

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&n);
	gets(Sen);
	sprintf(Dict,"welcome to code jam");
	for (int Case=1;Case<=n;Case++)
	{
		memset(f,0,sizeof(f));
		gets(Sen);
		Len=strlen(Sen);
		for (int i=0;i<Len;i++)
			if (Sen[i]==Dict[0])
				f[i][1]=1;
		for (int j=2;j<=19;j++)
		for (int i=0;i<Len;i++)
			if (Sen[i]==Dict[j-1])
				for (int k=0;k<i;k++)
					f[i][j]=(f[i][j]+f[k][j-1])%10000;
		Ans=0;
		for (int i=0;i<Len;i++)
			Ans=(Ans+f[i][19])%1000;
		printf("Case #%d: %.4d\n",Case,Ans);
	}
}
