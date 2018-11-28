#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int K, field[102][102];

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int caseN=1;caseN<=t;caseN++)
	{
		memset(field, -1, sizeof(field));

		scanf("%d", &K);
		for(int i=0;i<K*2-1;i++)
		{
			int lim = i+1;
			if(lim>K) lim = K - (lim-K);

			int s = K-1-i;
			if(s<0) s*=-1;
			for(int j=0;j<lim;j++) { scanf("%d", &field[i][s]); s+=2; }
		}

/*		for(int i=0;i<K*2-1;i++)
		{
			for(int j=0;j<K*2-1;j++)
			{
				if(field[i][j]==-1) printf(" ");
				else printf("%d", field[i][j]);
			}
			printf("\n");
		}
*/
		int ans=999999999;

		for(int i=0;i<K*2-1;i++)
		{
			for(int j=0;j<K*2-1;j++)
			{
				bool isAble=true;

				for(int q=0;q<K*2-1;q++)
				{
					for(int w=0;w<K*2-1;w++)
					{
						if(field[q][w]==-1) continue;

						int oppy = i + (i - q);
						int oppx = j + (j - w);

						if(oppy>=0 && oppy<=101 && field[oppy][w]!=-1 && field[q][w]!=field[oppy][w])
						{
							isAble=false;
							break;
						}

						if(oppx>=0 && oppx<=101 && field[q][oppx]!=-1 && field[q][w]!=field[q][oppx])
						{
							isAble=false;
							break;
						}
					}
					if(!isAble) break;
				}

				if(isAble)
				{
					int curLen = K+abs(K-1-i)+abs(K-1-j);
					ans = min(ans, curLen*curLen-K*K);
				}
			}
		}

		printf("Case #%d: %d\n", caseN, ans);
	}

	return 0;
}
