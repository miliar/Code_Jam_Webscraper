#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

vector<int> v1, v2;

void input()
{
	int n;
	int tmp;
	v1.clear();
	v2.clear();
	scanf("%d",&n);
	for(int i = 0; i != n; i++)
	{
		scanf("%d",&tmp);
		v1.push_back(tmp);
	}
	for(int i = 0; i != n; i++)
	{
		scanf("%d",&tmp);
		v2.push_back(tmp);
	}
}

long long solve()
{
	long long ans = 0;
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());
	reverse(v1.begin(), v1.end());
	for(int i = 0; i < v1.size(); i++)
		ans+=v1[i]*v2[i];

	return ans;
}
int main()
{
	int tests;
	int br=1;
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	scanf("%d", &tests);

	while(tests--)
	{
		input();
		printf("Case #%d: %lld\n",br, solve());
		br++;
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}