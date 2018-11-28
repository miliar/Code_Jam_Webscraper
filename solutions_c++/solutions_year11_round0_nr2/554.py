#include<cstdio>
#include<cstring>
#include<vector>

using namespace std;

vector<char> oppose[26] , ans;
char combine[26][26];
char str[1000];
int counter[26];


bool existOpposed(char ch)
{
	for (vector<char>::iterator iter = oppose[ch - 'A'].begin(); iter != oppose[ch - 'A'].end(); ++iter)
		if (counter[(*iter) - 'A']) return true;
	return false;

}


int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt","w",stdout);
	int cases;
	scanf("%d", &cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		memset(combine , 0 , sizeof(combine));
		for (char ch = 'A'; ch <= 'Z'; ++ch) oppose[ch - 'A'].clear();
		int C;
		scanf("%d" , &C);
		for (int i = 0; i < C; ++i)
		{
			scanf("%s" , str);
			combine[str[0] - 'A'][str[1] - 'A'] = str[2];
			combine[str[1] - 'A'][str[0] - 'A'] = str[2];
		}
		int D;
		scanf("%d" , &D);
		for (int i = 0; i < D; ++i)
		{
			scanf("%s" , str);
			oppose[str[0] - 'A'].push_back(str[1]);
			oppose[str[1] - 'A'].push_back(str[0]);
		}
		int N;
		scanf("%d%s" , &N, str);
		ans.clear();
		memset(counter, 0 , sizeof(counter));
		for (int i = 0; i < N; ++i)
		{
			if (!ans.empty())
			{
				size_t last = ans.size() - 1;
				if (combine[ans[last] - 'A'][str[i] - 'A'])
				{
					char ch = combine[ans[last] - 'A'][str[i] - 'A'];
					--counter[ans[last] - 'A'];
					ans.pop_back();
					ans.push_back(ch);
					continue;
				}
				if (existOpposed(str[i]))
				{
					ans.clear();
					memset(counter, 0 , sizeof(counter));
					continue;
				}
			}
			ans.push_back(str[i]);
			++counter[str[i] - 'A'];
		}
		printf("Case #%d: [", ca);
		if (!ans.empty()) putchar(ans[0]);
		for (size_t i = 1; i < ans.size(); ++i)
			printf(", %c", ans[i]);
		puts("]");

	}
}
