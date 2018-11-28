#include <cstdio>
#include <algorithm>
#include <iostream>
#include <memory>
#include <set>

using namespace std;

int N;
int mas[1100][1100];
int masinv[1100][1100];

int ccount[1100];

set<int> inh[1100];

bool Run()
{
	for (int i=0; i<N; i++)
	{
		int findParrent = -1;
		for (int j=0; j<N; j++)
		{
			if (ccount[j] == 0)
			{
				findParrent = j;
				break;
			}
		}
		if (findParrent == -1)
			return false;

		ccount[findParrent] = -1;

		for (int j=0; j<N; j++)
		{
			if (masinv[findParrent][j] == 1)
			{
				int needSize = inh[findParrent].size()+inh[j].size();
				inh[j].insert(inh[findParrent].begin(),inh[findParrent].end());
				ccount[j]--;
				if (inh[j].size() != needSize)
					return true;
			}
		}
	}
	return false;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		cerr<<"Test: "<<t<<endl;
		memset(mas,0,sizeof(mas));
		memset(masinv,0,sizeof(masinv));
		memset(ccount,0,sizeof(ccount));
		scanf("%d", &N);
		for (int i=0; i<N; i++)
		{
			inh[i].clear();
			inh[i].insert(i);
			int M;
			scanf("%d", &M);
			for (int j=0; j<M; j++)
			{
				int a;
				scanf("%d", &a);
				mas[i][a-1] = 1;
				masinv[a-1][i] = 1;
			}
			ccount[i] = M;
		}

		bool res = Run();
		printf("Case #%d: ", t);
		if (res)
			printf("Yes\n");
		else
			printf("No\n");
	}
	return 0;
}