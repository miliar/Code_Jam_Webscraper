#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <deque>
#include <stack>
#include <sstream>
#include <cstring>
#include <string>
#include <functional>
#include <numeric>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()

const int INF = ((1 << 31) - 1);
const long long LLINF = (((1LL << 63) - 1LL));
const double eps = 1e-9;
const double PI = 3.14159265358979323846;

typedef long long ll;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	cin >> tests;
	for (int it = 0; it < tests; ++it) {
		cerr << it << " from " << tests << " completed\n";
		int n;
		cin >> n;
		vector<int> button_position(n);
		vector<string> button_color(n);
		for (int i = 0; i < n; ++i){
			char buf[1 << 5];
			scanf("%s%d", buf, &button_position[i]);
			button_color[i] = string(buf);
		}
		int completed_quests = 0;
		int blue_goal = -1;
		int orange_goal = -1;
		int blue_pos = 1;
		int orange_pos = 1;
		int time = 0;
		while(completed_quests != n) {
			bool orange_moved = false;
			bool blue_moved = false;
			++time;
			if (button_color[completed_quests] == "O" && button_position[completed_quests] == orange_pos ||
				button_color[completed_quests] == "B" && button_position[completed_quests] == blue_pos) {
				(button_color[completed_quests] == "O"?orange_moved:blue_moved) = true;
				(button_color[completed_quests] == "O"?orange_goal:blue_goal) = -1;
				++completed_quests;
			}
			if (orange_goal == -1) {
				for (int i = completed_quests; i < n; ++i)
					if (button_color[i] == "O") {
						orange_goal = button_position[i];
						break;
					}
			}
			if (blue_goal == -1) {
				for (int i = completed_quests; i < n; ++i)
					if (button_color[i] == "B") {
						blue_goal = button_position[i];
						break;
					}
			}
			if (orange_goal != orange_pos && orange_goal != -1 && !orange_moved) {
				if (orange_goal < orange_pos)
					--orange_pos;
				else
					++orange_pos;
				orange_moved = true;
			}
			if (blue_goal != blue_pos && blue_goal != -1 && !blue_moved) {
				if (blue_goal < blue_pos)
					--blue_pos;
				else
					++blue_pos;
				blue_moved = true;
			}
		}
		cout << "Case #" << it + 1 << ": "<< time << "\n";
	}	
	return 0;
}