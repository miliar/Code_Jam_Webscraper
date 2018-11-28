#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <iostream>

using namespace std;

#define SZ(x) ((int)(x).size())
#define MP make_pair
#define PB push_back
#define ALL(x) (x).begin(), (x).end()
#define ZERO(a) memset(a, 0, sizeof(a))
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define FORE(i,a,b) for(int i = (a); i <= (b); ++i)
#define RFOR(i,b,a) for(int i = (b); i >= (a); --i)

typedef long long LL;

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;

char ta[128][128];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);

	int T, N;
	string str;
	cin >> T; 
	FORE(cas, 1, T)
	{
		ZERO(ta);
		cin >> N;
		FOR(i, 0, N)
		{
			cin >> str;
			FOR(j, 0, N)
				ta[i][j] = str[j];
		}

		vd wp(N);
		FOR(i, 0, N)
		{
			int win = 0, tot = 0;
			FOR(j, 0, N) {
				if (ta[i][j] != '.') tot++;
				if (ta[i][j] == '1') win++;
			}
			wp[i] = (double)win / tot;
		}

		vd  owp(N);
		FOR(i, 0, N)
		{
			int cnt = 0; double re = 0.;
			FOR(j, 0, N)
				if (ta[i][j] != '.') {
					cnt++;
					//re += wp[j];
					int tot = 0; int win = 0;
					FOR(k, 0, N)
					{
						if (k == i) continue;
						if (ta[j][k] !='.') tot++;
						if (ta[j][k] == '1') win++;
					}
					re += (double)win / tot;

				}
			owp[i] = re / cnt;
		}

		vd  oowp(N);
		FOR(i, 0, N)
		{
			int cnt = 0; double re = 0.;
			FOR(j, 0, N)
				if (ta[i][j] != '.') {
					cnt++;
					re += owp[j];
				}
			oowp[i] = re / cnt;
		}
		
		cout << "Case #" << cas << ":" << endl;
		FOR(i, 0, N)
			cout << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl;

	}
    return 0;
}