#include <algorithm>
#include <cstdio>

using namespace std;

int ntest, nprisoner, nrelease;
int release[100], temp, mini;
pair<int, int> batas[100];

int main()
{
	scanf("%d", &ntest);
	for(int test = 1;test <= ntest;++test)
	{
		scanf("%d %d", &nprisoner, &nrelease);
		for(int i = 0;i < nrelease;++i)
			scanf("%d", &release[i]);
		mini = 1000000000;
		do
		{
			for(int i = 0;i < nrelease;++i)
				batas[i] = pair<int, int>(1, nprisoner);
			temp = 0;
			for(int i = 0;i < nrelease;++i)
			{
				temp += (batas[i].second - batas[i].first);
				for(int j = 0;j < nrelease;++j)
					if(release[j] < release[i])
						batas[j].second = min(batas[j].second, release[i] - 1);
					else
						batas[j].first = max(batas[j].first, release[i] + 1);
			}
			if(temp < mini)
				mini = temp;
		}
		while(next_permutation(release, release + nrelease));
		printf("Case #%d: %d\n", test, mini);
	}
	return 0;
}
