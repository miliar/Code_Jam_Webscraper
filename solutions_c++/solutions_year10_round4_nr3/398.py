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

#define FS 110

struct FIELD {
	char field[FS][FS];
};

void print(const FIELD &f)
{
	for (int r = 0; r < 6; ++r) {
		for (int c = 0; c < 6; ++c) {
			if (f.field[r][c])
				printf("*");
			else
				printf(" ");
		}
		puts("");
	}
}

int step(FIELD &out, const FIELD &in)
{
	int cnt = 0;
	memset(&out, 0, sizeof out);
	for (int r = 1; r < FS; ++r) {
		for (int c = 1; c < FS; ++c) {
			bool was = in.field[r][c] && (in.field[r-1][c] || in.field[r][c-1]);
			bool created = in.field[r-1][c] && in.field[r][c-1];
			out.field[r][c] = was || created;
			cnt += out.field[r][c];
		}
	}
	//print(out);
	return cnt;
}

int main()
{
	int TC;
	scanf("%d", &TC);
	for (int T = 1; T <= TC; ++T) {
		FIELD state;
		memset(&state, 0, sizeof state);
		int R;
		scanf("%d", &R);
		while (R--) {
			int r1, c1, r2, c2;
			scanf("%d %d %d %d", &c1, &r1, &c2, &r2);
			for (int r = r1; r <= r2; ++r)
				for (int c = c1; c <= c2; ++c)
					state.field[r][c] = 1;
		}
		FIELD newstate;
		int step_count = 0;
		while (step(newstate, state)) {
			state = newstate;
			step_count += 1;
		}
		printf("Case #%d: %d\n", T, step_count+1);
	}
	return 0;
}
