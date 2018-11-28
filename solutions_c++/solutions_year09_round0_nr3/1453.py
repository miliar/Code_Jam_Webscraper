#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const char S[]="welcome to code jam";

int res[20];
char s[1000];
int n;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d\n",&T);
	for (int test=0;test<T;test++)
	{
		gets(s);
		n=strlen(s);
		memset(res,0,sizeof(res));
		for (int i=0;i<n;i++)
		{
			for (int j=0;j<=18;j++)
				if (s[i]==S[j])
				{
					if (j!=0)
						res[j]=(res[j]+res[j-1])%10000; else
						res[j]=(res[j]+1)%10000;
				}
		}
		printf("Case #%d: %04d\n",test+1,res[18]);
	}
	return 0;
}