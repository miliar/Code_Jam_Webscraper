#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include<iostream>
#include<fstream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>
#include<list>
#include<map>
#include<deque>
#include<stack>
#include<queue>
#include<string>
#include<cstring>
#include<bitset>
#include<sstream>
#include<time.h>
#include<numeric>
#include<functional>

using namespace std;
#define _CRT_SECURE_NO_WARNINGS
#define INF  ((1 << 31) - 1)
#define LLINF  ((ll)((1LL << 63) - 1))
#define eps (1e-9)
#define million 1000000
#define PI 3.14159265358979323846
#define sz(v) ((int)(v).size())
#define MP make_pair
#define PB push_back
#define all(v) (v).begin(), (v).end()
typedef long long ll;

const int SIZE = 300;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int C;
	cin >> C;
	for (int test = 0; test < C; ++test) {
		cerr << test << "\n";
		cout << "Case #" << test + 1 << ": ";
		int r;
		cin >> r;
		vector<string> plan(SIZE, string(SIZE, '0'));
		bool live = false;
		if (r > 0)
			live = true;
		for (int i = 0; i < r; ++i) {
			int a,b,c,d;
			cin >> a>>b>>c>>d;
			for (int x = a; x <= c; ++x)
				for (int y = b; y <= d; ++y)
					plan[SIZE / 2 - 50 + x][SIZE / 2 - 50 + y] = '1';
		}
		int round;
		for (round = 1; live; ++round) {
			live = false;
			vector<string> copy_plan(plan);
			for (int x = 0; x < SIZE; ++x)
				for (int y = 0; y < SIZE; ++y) {
					if (plan[x][y] == '1' && 
						(x == 0 && y == 0 || x > 0 && y > 0 && plan[x - 1][y] == '0' && plan[x][y - 1] == '0')) {
						copy_plan[x][y] = '0'; 
						continue;
					}
					if (plan[x][y] == '0' && 
						(x != 0 && y != 0 && plan[x - 1][y] == '1' && plan[x][y - 1] == '1')) {
						copy_plan[x][y] = '1'; 
						continue;
					}
					copy_plan[x][y] = plan[x][y];
				}
			for (int x = 0; x < SIZE; ++x)
				for (int y = 0; y < SIZE; ++y) {
					if (copy_plan[x][y] == '1')
						live = true;
				}
			plan = copy_plan;
		}
		cout << round - 1<< "\n";
	}
	return 0;
}