#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define fr(i, N) for(i = 0; i < (int)N; i++)
#define setContains(i,j) (((1<<j)&i) != 0)
#define MP make_pair
#define F first
#define S second
#define pb push_back
#define Eps 1e-11

typedef pair<int, int> pi;
typedef long long ll;

int R, C;
ll S[30][30], W[30][30], T[30][30];
ll Ans[60][60];

void input()
{
	int i, j;
	ll sum;
	scanf("%d%d", &R, &C);

	fr (i, R) fr (j, C) {
		scanf("%lld%lld%lld", &S[i][j], &W[i][j], &T[i][j]);
		sum = S[i][j] + W[i][j];
		T[i][j] %= sum;
	}
}

bool isValid(int r, int c) {
	return 1 <= r && r < (R*2+1) && 1 <= c && c < (C*2+1);
}

ll getNext(pi from, pi to, ll t) {
	if (from > to) swap(from, to);

	if (from.F%2 == 0 && from.S%2 == 0) {
		return t + 2;
	} else if (from.F%2 == 0 && from.S == to.S) {
		return t + 2;
	} else if (from.S%2 == 0 && from.F == to.F) {
		return t + 2;
	}

	int r = (from.F-1) / 2;
	int c = (from.S-1) / 2;
	ll tt = t%(S[r][c] + W[r][c]);
	ll sum = S[r][c] + W[r][c];
	if (tt < T[r][c]) tt += sum;

	if ((T[r][c] <= tt && tt < (T[r][c] + S[r][c])) || 
		(T[r][c] + sum) <= tt && (tt < T[r][c] + S[r][c] + sum)) {
		if (from.S == to.S) return t + 1;
		else {
			if (tt < T[r][c] + S[r][c]) return t + (T[r][c] + S[r][c] - tt) + 1;
			else return t + (sum + T[r][c] + S[r][c] - tt) + 1;
		}
	} else {
		if (from.F == to.F) return t + 1;
		else {
			if (tt < T[r][c]) return t + (T[r][c] - tt) + 1;
			else return t + (T[r][c] + sum - tt) + 1;
		}
	}
}

void process()
{
	int i, j;
	set<pair<ll, pi> > Data;
	int dr[4] = {-1, 0, 1, 0};
	int dc[4] = {0, 1, 0, -1};
	fr (i, R*2+2) fr (j, C*2+2) Ans[i][j] = -1;

	Ans[R*2][1] = 0;
	Data.insert(MP(0, MP(R*2, 1)));

	while(Data.size()) {
		int r = Data.begin()->S.F;
		int c = Data.begin()->S.S;
		Data.erase(Data.begin());

		fr (j, 4) if (isValid(r+dr[j], c+dc[j])) {
			ll next = getNext(MP(r, c), MP(r+dr[j], c+dc[j]), Ans[r][c]);
			if (Ans[r+dr[j]][c+dc[j]] > next) {
				Data.erase(MP(Ans[r+dr[j]][c+dc[j]], MP(r+dr[j], c+dc[j])));
				Ans[r+dr[j]][c+dc[j]] = -1;
			}

			if (Ans[r+dr[j]][c+dc[j]] == -1) {
				Data.insert(MP(next, MP(r+dr[j], c+dc[j])));
				Ans[r+dr[j]][c+dc[j]] = next;
			}
		}
	}

	printf("%lld\n", Ans[1][C*2]);
}

int main()
{
	int t, T;
	scanf("%d", &T);

	fr(t, T)
	{
		input();
		printf("Case #%d: ", t+1);
		process();
	}

	return 0;
}
