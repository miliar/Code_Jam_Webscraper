#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

typedef long long LL;

LL P, K, L;
vector<LL> fres;

void solve(int id)
{
	sort(fres.begin(), fres.end(), greater<int>());

	LL ans = 0;
	for (size_t i = 0;i < fres.size();++i)
		ans += fres[i] * (i / K + 1);
	
	printf("Case #%d: %lld\n",id, ans);
}

int main()
{
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.txt", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);

	int N;
	scanf("%d", &N);
	for (int i = 0;i < N;++i)
	{
		fres.clear();
		scanf("%d%d%d",&P, &K, &L);
		int temp;
		for (int j = 0;j < L;++j)
		{
			scanf("%d", &temp);
			fres.push_back(temp);
		}

		solve(i + 1);
	}

	return 0;
}