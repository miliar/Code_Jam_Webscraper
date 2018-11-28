#include<cstdio>
#include<vector>
#include<algorithm>


using namespace std;
long long p, k ,l;
vector<long long> letters;
void input()
{
	letters.clear();
	scanf("%lld %lld %lld", &p, &k, &l);
	long long tmp;
	for(int i = 0; i < l; i++)
	{
		scanf("%lld",&tmp);
		letters.push_back(tmp);
	}
}

long long solve()
{
	long long ans = 0;
	if (p*k<l) return -1;

	sort(letters.begin(), letters.end());
	reverse(letters.begin(), letters.end());
	
	for(long long  i = 0; i < letters.size(); i++)
	{
		ans+=(letters[i]*((i/k)+1));
	}

	return ans;
}

int main()
{
	freopen("input.inp","r",stdin);
	freopen("output.out","w", stdout);

	int tests;
	long long ans;
	scanf("%d",&tests);

	for(int test = 0; test < tests; test++)
	{
		input();
		ans = solve();
		if(ans == -1)
		{
			printf("Case #%d: Impossible\n", test + 1);
		}
		else
		{
			printf("Case #%d: %lld\n", test + 1, ans);
		}
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}