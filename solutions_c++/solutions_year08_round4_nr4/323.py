#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int Perm[20];
char In[50001];
char Out[50001];

int main()
{
	int lw;
	scanf("%d",&lw);

	for (int Lc=1;Lc<=lw;Lc++)
	{
		int k;
		scanf("%d",&k);
		for (int i=0;i<k;i++)
			Perm[i] = i;
		scanf("%s",In);
		int n = strlen(In);
		int Best = n;
		do
		{
			for (int i=0,j;i<n;i+=k)
				for (j=0;j<k;j++)
					Out[i+j] = In[i+Perm[j]];
			int N=1;
			for (int i=1;i<n;i++)
				if (Out[i]!=Out[i-1])
					N++;
			Best = min(Best,N);
		}while (next_permutation(Perm,Perm+k));
		printf("Case #%d: %d\n",Lc,Best);
	}

	return 0;
}
