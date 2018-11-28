#include<iostream>


using namespace std;

int const maxN = 1000;
struct T {
	int st, en, belong;
};
struct T_less {
	bool operator () (const T& a, const T& b) const
	{
		return a.en < b.en;
	}
};

T data[maxN];
int n, t, na, nb;
int Turn(string const &s);
int ans[20];
bool used[maxN];
int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	cin >> n;
	for (int cases = 0; cases != n; ++cases) {
		cin >> t;
		cin >> na >> nb;
		for (int i(0); i < na; ++i) {
			string s1, s2;
			cin >> s1 >> s2;
			data[i].st = Turn(s1);
			data[i].en = Turn(s2);
			data[i].belong = 0;
		}
		for (int i(0); i < nb; ++i) {
			string s1, s2;
			cin >> s1 >> s2;
			data[i + na].st = Turn(s1);
			data[i + na].en = Turn(s2);
			data[i + na].belong = 1;
		}
		sort(data, data + na + nb, T_less());
		memset(used, 0, sizeof(used));
		memset(ans, 0, sizeof(ans));
		for (int i = 0; i < na + nb; ++i) {
			bool chk = 0;
			for (int j = i - 1; j >= 0; --j)
			    if (!used[j] && data[j].belong + data[i].belong == 1 && data[j].en + t <= data[i].st) {
					chk = 1;
					used[j] = 1;
					break;
				}
			if (!chk) ++ans[data[i].belong];
		}
		printf("Case #%d: %d %d\n", cases + 1, ans[0], ans[1]);
	}
}
int Turn(string const &s)
{
	int ret = 0;
	ret = (s[3] - '0') * 10 + s[4] - '0';
	ret += ((s[0] - '0') * 10 + s[1] - '0') * 60;
	return ret;
}
