#include <cstdio>
#include <algorithm>

using namespace std;

int  T[10001];
bool C[10001];
int  F[10001];

int main()
{
	int lw;
	scanf("%d",&lw);

	for (int Lc=1;Lc<=lw;Lc++)
	{
		int n,v;
		scanf("%d%d",&n,&v);
		for(int i=1;i<=n;i++)
		{
			scanf("%d",&T[i]);
			if (i*2+1<=n)
			{
				int P;
				scanf("%d",&P);
				C[i] = (P==1);
			}
		}
		int pv;
		if (v) pv=0; else pv=1;
		for (int i=n;i>=1;i--)
		{
			if (i*2+1>n)
			{
				if (T[i] == v)
					F[i] = 0;
				else
					F[i] = -1;
			}
			else
			{
				int L = F[i*2];
				int P = F[i*2+1];
				if ( (L == -1) && (P == -1) )
				{
					F[i] = -1;
					continue;
				}
				if ( ( L == -1 ) || ( P == -1) )
				{
					if (T[i] == pv)
					{
						F[i] = max(L,P);
						continue;
					}
					else
					{
						if (C[i])
						{
							F[i] = max(L,P)+1;
							continue;
						}
						else
						{
							F[i] = -1;
							continue;
						}
					}
				}
				if (T[i] == pv)
				{
					F[i] = min(L,P);
				}
				else
				{
					F[i] = L+P;
					if (C[i])
					{
						F[i] = min(F[i], min(L,P)+1);
					}
				}
			}
		}
		if (F[1] == -1)
			printf("Case #%d: IMPOSSIBLE\n",Lc);
		else
			printf("Case #%d: %d\n",Lc,F[1]);
	}

	return 0;
}
