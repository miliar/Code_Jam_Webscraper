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

int C, D, N;
char invoke[110];
char combine[128][128];
bool opposed[128][128];
int E;
char elements[12345678];
int cnt[128];

void read_input()
{
	memset(combine, 0, sizeof combine);
	memset(opposed, 0, sizeof opposed);
	memset(cnt, 0, sizeof cnt);

	char buf[1024];
	scanf("%d", &C);
	for (int i = 0; i < C; ++i) {
		scanf("%s", buf);
		int a = buf[0];
		int b = buf[1];
		int c = buf[2];
		combine[a][b] = c;
		combine[b][a] = c;
	}

	scanf("%d", &D);
	for (int i = 0; i < D; ++i) {
		scanf("%s", buf);
		int a = buf[0];
		int b = buf[1];
		opposed[a][b] = true;
		opposed[b][a] = true;
	}

	scanf("%d %s", &N, invoke);
	E = 0;
}

bool try_combine()
{
	if (E < 2)
		return false;
	int a = elements[E-2];
	int b = elements[E-1];
	int combined = combine[a][b];
	if (combined == 0)
		return false;
	elements[E-2] = combined;
	E -= 1;
	cnt[a] -= 1;
	cnt[b] -= 1;
	cnt[combined] += 1;
	return true;
}

bool is_opposed()
{
	assert(E > 0);
	int a = elements[E-1];
	cnt[a] -= 1;
	bool was_opposed = false;
	for (int b = 'A'; !was_opposed && b <= 'Z'; ++b) {
		was_opposed = (opposed[a][b] && cnt[b] > 0);
	}
	cnt[a] += 1;
	return was_opposed;
}

void solve()
{
	for (int i = 0; i < N; ++i) {
		elements[E++] = invoke[i];
		cnt[(int) invoke[i]] += 1;

		bool opposed = is_opposed();

		int combine_count = 0;
		while (try_combine())
			combine_count += 1;

		if (opposed && combine_count == 0) {
			E = 0;
			memset(cnt, 0, sizeof cnt);
		}
	}
}

void print_output()
{
	printf("[");
	for (int i = 0; i < E; ++i) {
		if (i != 0) printf(", ");
		printf("%c", elements[i]);
	}
	puts("]");
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		read_input();
		solve();
		printf("Case #%d: ", TC);
		print_output();
	}
	return 0;
}
