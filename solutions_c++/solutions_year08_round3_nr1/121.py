#include <cstdio>
#include <set>
#include <queue>
#define LLD long long int
using namespace std;

int main()
{
	int lw;
	scanf("%d",&lw);

	for (int L=1;L<=lw;L++)
	{
		int LP,LLK,LK;
		scanf("%d%d%d",&LLK,&LP,&LK);
		priority_queue<int> Z;
		while (LK--)
		{
			int A;
			scanf("%d",&A);
			Z.push(A);
		}
		queue<int> T[1001];
		LLD All = 0;
		while (!Z.empty())
		{
			int X = Z.top();
			Z.pop();
			LLD Cost = 1200000000001ll;
			int Best = -1;
			for (int i=0;i<LP;i++)
				if ( (T[i].size() < LLK) && ( (LLD)(T[i].size()+1)*(LLD)X < Cost ) )
				{
					Cost = (LLD)(T[i].size()+1)*(LLD)X;
					Best = i;
				}
				if (Best==-1) {All=-1; break;}
			T[Best].push(X);
			All += Cost;
		}
		if (All==-1) printf("Case #%d: Impossible\n",L); else
		printf("Case #%d: %lld\n",L,All);
	}

	return 0;
}
