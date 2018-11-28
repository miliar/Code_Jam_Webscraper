#include <iostream>

using namespace std;

const int lmax=5001;

char s[lmax];
char v[]="welcome to code jam@";
int ans[lmax][20];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t,T;
	scanf("%d",&T);
	gets(s);
	for(t=1;t<=T;t++)
	{
		int i,j;
		gets(s);
		memset(ans,0,sizeof(ans));
		ans[0][0]=1;
		for(i=0;s[i];i++)
			for(j=0;v[j];j++)
			{
				if (s[i]==v[j]) ans[i+1][j+1]=(ans[i+1][j+1]+ans[i][j])%10000;
				ans[i+1][j]=(ans[i+1][j]+ans[i][j])%10000;
			}
		printf("Case #%d: %04d\n",t,ans[i][19]);
	}


	return 0;
}