#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int pos[11111];
int length[11111];
int F[11111];

int main(void)
{
	freopen("a-large.in","rt",stdin);
	freopen("a-large.out","wt",stdout);
	int TK = 0;
	int TKN = 0;
	scanf("%d",&TK);
	while(TK--)
	{
		printf("Case #%d: ",++TKN);
		int N = 0;
		scanf("%d",&N);
		for(int i = 1;i <= N;i++) scanf("%d %d",&pos[i],&length[i]);
		N++;
		scanf("%d",&pos[N]);
		length[N] = 258921;
		//if(length[1] < pos[1]) { puts("NO"); continue; }
		memset(F,0,sizeof(F));
		F[1] = pos[1];
		for(int i = 1;i <= N;i++)
		{
			int p = pos[i];
			int r = p+F[i];
			for(int j = i+1;j <= N;j++)
			{
				if(pos[j] > r) break;
				F[j] = max(F[j],min(pos[j]-p,length[j]));
			}
		}
		if(F[N] > 0) puts("YES");
		else puts("NO");
	}
	while(getchar() != EOF);
	return 0;
}
