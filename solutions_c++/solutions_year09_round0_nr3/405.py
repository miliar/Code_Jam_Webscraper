#include<iostream>

using namespace std;

const char* pattern = "welcome to code jam";
const int L = 19;

#define MAXLEN 500

char s[MAXLEN+1];
int d[MAXLEN+1][L];
int len;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int N,nn,ans;
	scanf("%d",&N);
	while(getchar()!='\n') ;
	for(nn=0;nn<N;nn++)
	{
		ans = len = 0;
		while((s[len++]=getchar())!='\n') ;
		s[len--]=0;
		memset(d,0,sizeof(d));
		//d[0][0]=s[0]==pattern[0];
		for(int i=0;i<len;i++)
			for(int j=0;j<L;j++)
			{
				if (s[i]==pattern[j])
					if (j==0) d[i][0]=1;
					else
					{
						for(int k=0;k<i;k++)
							d[i][j]=(d[i][j]+d[k][j-1])%10000;
						if (j==L-1) ans=(ans+d[i][j])%10000;
					}
			}

		printf("Case #%d: %04d\n",nn+1,ans);
	}

	return 0;
}
