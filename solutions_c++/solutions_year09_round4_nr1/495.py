#include<stdio.h>
#include<string.h>
#include<vector>
#define pb push_back
using namespace std;

vector<int> VECT;
char S[100];
int N;

int main()
{
	int nrt;
	freopen("crazy.in","r",stdin);
	freopen("crazy.out","w",stdout);
	scanf("%d\n",&nrt);
	for(int nr = 1;nrt;++nr,--nrt)
	{
		scanf("%d\n",&N);
		VECT.clear();
		int sol = 0;
		VECT.pb(0);
		for(int i = 1;i <= N; ++i)
		{
			memset(S,0,sizeof(S));
			scanf("%s\n",S + 1);
			int cur = 0;
			for(int j = 1;j <= N; ++j)
				if (S[j] == '1') cur = j;
			VECT.pb(cur);
		}
		for(int i = 1;i <= N; ++i)
		{
			for(int j = i;j <= N; ++j)
			{
				if (VECT[j] <= i)
				{
					for(int k = j;k > i; --k)
						VECT[k] = VECT[k - 1];
					sol += j - i;
					break;
				}
			}

		}
		printf("Case #%d: %d\n",nr,sol);
	}

	return 0;
}



