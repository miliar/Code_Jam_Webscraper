#include <cstdio>
#include <string>
#include <vector>
#include <map>

using namespace std;

typedef map<string ,bool> MSB;

vector<string> ses;
vector<string> qs;

void dealstr(char* str)
{
	int n = strlen(str);
	if (str[n - 1] == '\r' || str[n - 1] == '\n') 
		str[n - 1] = '\0';
}

void solve(int id)
{
	int cnt, ans;
	MSB msb;
	for (size_t i = 0;i < ses.size();++i)
	{
		msb.insert(make_pair(ses[i], false));
	}
	ans = 0;
	cnt = 0;
	MSB::iterator pos,p;
	for (size_t i = 0;i < qs.size();++i)
	{
		pos = msb.find(qs[i]);
		if (!msb[qs[i]])
		{
			++cnt;
			if (cnt == ses.size())
			{
				++ans;
				cnt = 1;
				for (p = msb.begin();p != msb.end();++p)
					p->second = false;
			}
			pos->second = true;
		}
	}
	printf("Case #%d: %d\n", id, ans);
}

int main()
{
	//freopen("A-small.in", "r", stdin);
	////freopen("in.txt", "r", stdin);
	//freopen("A-small.txt", "w", stdout);

	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.txt", "w", stdout);

	int N, S, Q;
	char memo[110];
	scanf("%d", &N);
	for (int i = 0;i < N;++i)
	{
		ses.clear();
		qs.clear();

		scanf("%d\n", &S);
		for (int j = 0;j < S;++j)
		{
			fgets(memo, 110, stdin); 
			dealstr(memo);
			ses.push_back(string(memo));
		}
		scanf("%d\n", &Q);
		for (int j = 0;j < Q;++j)
		{
			fgets(memo, 110, stdin); 
			dealstr(memo);
			qs.push_back(string(memo));
		}
		solve(i + 1);
	}
	return 0;
}