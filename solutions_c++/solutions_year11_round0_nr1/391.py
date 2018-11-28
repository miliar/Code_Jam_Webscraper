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

int N;
int bot[200];
int button[200];
int solved_at[200];

void read_input()
{
	scanf("%d", &N);
	char buf[4];
	for (int i = 0; i < N; ++i) {
		scanf("%s %d", buf, &button[i]);
		bot[i] = (buf[0] == 'O');
	}
}

void solve()
{
	int bot_pos[2] = {1, 1};
	int bot_free[2] = {0, 0};

	for (int i = 0; i < N; ++i) {
		int b = bot[i];
		int but = button[i];
		int time_needed_to_move_and_press = abs(bot_pos[b] - but) + 1;
		int time_arrival = bot_free[b] + time_needed_to_move_and_press;
		int time_at_press = time_arrival;
		if (i > 0 && time_arrival <= solved_at[i-1])
			time_at_press = solved_at[i-1] + 1;
		solved_at[i] = time_at_press;
		bot_pos[b] = but;
		bot_free[b] = time_at_press;
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		read_input();
		solve();
		printf("Case #%d: %d\n", TC, solved_at[N-1]);
	}
	return 0;
}
