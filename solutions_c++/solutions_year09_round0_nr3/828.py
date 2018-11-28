#include<stdio.h>
#include<string>

using namespace std;

const int maxn = 1000;
const int MOD = 10000;
int D[20][maxn],N,NRSOL;
string S1;
char S[maxn];

int main()
{
	freopen("welcome.in","r",stdin);
	freopen("welcome.out","w",stdout);
	scanf("%d\n",&N);
	S1 = " welcome to code jam";
	for(int i = 1;i <= N; ++i)
	{
		memset(S,0,sizeof(S));
		fgets(S + 1,10000,stdin);
		memset(D,0,sizeof(D));
		D[0][0] = 1;
		int lung = strlen(S + 1);
		NRSOL = 0;
		for(int j = 1;j <= lung; ++j)
		{
			for(int k = 1;k < (int)S1.size(); ++k)
				if (S1[k] == S[j])
				{
					for(int l = 0;l < j; ++l)
						D[k][j] = (D[k - 1][l] + D[k][j]) % MOD;
					if (k == (int)S1.size() - 1) NRSOL = (NRSOL + D[k][j]) % MOD;
				}
		}	
		printf("Case #%d: %04d\n",i,NRSOL);
	}
	

	return 0;
}


