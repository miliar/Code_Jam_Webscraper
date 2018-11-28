#include <algorithm> 
#include <bitset> 
#include <cassert>
#include <cmath> 
#include <complex>
#include <cstdio> 
#include <cstdlib> 
#include <cstring>
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iomanip> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <valarray>
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

int N, M;
char words[120][16];
int lengths[120];
char letters[11][30];

int lettercount[128];
bool choosable[128];

void remove(int n)
{
	assert(choosable[n]);
	choosable[n] = false;
	for (int j = 0; j < lengths[n]; ++j) {
		lettercount[(int)words[n][j]] -= 1;
	}
}

int get_score(int n, int m)
{
	int len = lengths[n];
	memset(lettercount, 0, sizeof lettercount);
	memset(choosable, true, sizeof choosable);
	for (int i = 0; i < N; ++i) {
		if (lengths[i] != len) {
			choosable[i] = false;
			continue;
		}
		for (int j = 0; j < lengths[i]; ++j) {
			lettercount[(int)words[i][j]] += 1;
		}
	}

	int score = 0;
	for (int k = 0; k < 26; ++k) {
		int ch = letters[m][k];
		assert(lettercount[ch] >= 0);
		if (lettercount[ch] == 0)
			continue;

		bool found_chars = false;
		for (int j = 0; j < len; ++j) {
			if (words[n][j] == ch)
				found_chars = true;
		}

		if (!found_chars) {
			score += 1;
		}

		for (int i = 0; i < N; ++i) {
			if (!choosable[i])
				continue;
			for (int j = 0; j < len; ++j) {
				if (words[n][j] == ch && words[i][j] != ch) {
					remove(i);
					break;
				}
				if (words[n][j] != ch && words[i][j] == ch) {
					remove(i);
					break;
				}
			}
		}
	}

	return score;
}

void solve_for_m(int m)
{
	int mx_score = -1;
	int mx_n = -1;
	for (int i = 0; i < N; ++i) {
		int s = get_score(i, m);
		//printf("'%s' => %2d\n", words[i], s);
		if (s > mx_score) {
			mx_score = s;
			mx_n = i;
		}
	}
	printf(" %s", words[mx_n]);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		scanf("%d %d", &N, &M);
		for (int i = 0; i < N; ++i) {
			scanf("%s", words[i]);
			lengths[i] = (int) strlen(words[i]);
		}
		for (int i = 0; i < M; ++i) {
			scanf("%s", letters[i]);
			assert(strlen(letters[i]) == 26);
		}

		printf("Case #%d:", TC);
		for (int i = 0; i < M; ++i)
			solve_for_m(i);
		puts("");
	}
	return 0;
}
