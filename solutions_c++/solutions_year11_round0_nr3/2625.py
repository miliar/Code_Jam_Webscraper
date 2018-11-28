#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
using namespace std;
int t;
int n;
int vet[10000];
int melhorSol;
void achaSol(string s)
{
	if(s.size() == n)
	{
		int z = -1, u = -1;
		int sz = 0, su = 0;
		for(int i = 0; i < n; i++)
		{
			if(s[i] == '0')
			{
				sz += vet[i];
				if(z == -1)
					z = vet[i];
				else
					z = z ^ vet[i];
			}
			else
			{
				su += vet[i];
				if(u == -1)
					u = vet[i];
				else
					u = u ^ vet[i];
			}
		}
		if(z == u)
		{
			melhorSol = max(melhorSol, max(sz, su));
		}
	}
	else
	{
		achaSol(s + '0');
		achaSol(s + '1');
	}
}
int main()
{
	scanf("%d",&t);
	for(int i = 0; i < t; i++)
	{
		melhorSol = 0;
		scanf("%d",&n);
		int parcial = 0;
		for(int j = 0; j < n; j++)
		{
			scanf("%d",&vet[j]);
			if(!j)
				parcial = vet[j];
			else
				parcial = parcial ^ vet[j];
		}
		if(parcial)
		{
			printf("Case #%d: NO\n",i+1);
		}
		else
		{
			printf("Case #%d: ",i+1);
			int solEsq[10000];
			int solDir[10000];
			solEsq[0] = vet[0];
			for(int i = 1; i < n; i++)
				solEsq[i] = solEsq[i-1] ^ vet[i];
			solDir[n-1] = vet[n-1];
			for(int i = n-2; i >= 0; i--)
				solDir[i] = solDir[i+1] ^ vet[i];
			for(int j = 0; j < n; j++)
				melhorSol += vet[j];
			int men = 0x7fffffff;
			for(int j = 0; j < n; j++)
			{
				if(vet[j] < men)
					men = vet[j];
			}
			melhorSol -= men;
			printf("%d\n",melhorSol);
		}
	}
	return 0;
}
