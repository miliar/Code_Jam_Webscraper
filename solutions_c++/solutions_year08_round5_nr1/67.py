#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstring>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <list>
#include <fstream>
using namespace std;
static const double EPS = 1e-8;
typedef long long ll;

static const int SIZE = 3010;

static const int DIRECTION[4][2] = {
	{1, 0}, {0, 1}, {-1, 0}, {0, -1}
};
bool pocket[SIZE * 2][SIZE * 2];
vector<int> wallHorizontal[SIZE * 2];
vector<int> wallVertical[SIZE * 2];


int main() {
	//ifstream cin("a.in.txt");

	int N;
	cin >> N;

	for (int testCase = 1; testCase <= N; ++testCase){
		int T;
		cin >> T;

		for (int i = 0; i < SIZE * 2; ++i){
			wallHorizontal[i].clear();
			wallVertical[i].clear();
		}

		int answer = 0;

		int x = SIZE;
		int y = SIZE;
		int direction = 0;
		for (int i = 0; i < T; ++i){
			string s;
			int t;
			cin >> s >> t;

			for (int j = 0; j < t; ++j){
				for (int k = 0; k < s.size(); ++k){
					const char c = s[k];

					switch (c) {
						case 'F':
							{
								const int nextX = x + DIRECTION[direction][0];
								const int nextY = y + DIRECTION[direction][1];
								const int minX = min(x, nextX);
								const int minY = min(y, nextY);

								if (direction % 2 == 0){
									//…•½
									wallHorizontal[minX].push_back(minY);
								} else {
									//‚’¼
									wallVertical[minY].push_back(minX);
								}
								x = nextX;
								y = nextY;
							}
							break;
						case 'R':
							++direction;
							direction %= 4;
							break;
						case 'L':
							direction += 3;
							direction %= 4;
							break;
					}
				}
			}
		}

		for (int i = 0; i < SIZE * 2; ++i){
			sort(wallHorizontal[i].begin(), wallHorizontal[i].end());
			sort(wallVertical[i].begin(), wallVertical[i].end());
		}

		memset(pocket, 0, sizeof(pocket));

		//…•½
		for (int x = 0; x < SIZE * 2; ++x){
			for (int i = 1; i + 1 < wallHorizontal[x].size(); i += 2){
				const int from = wallHorizontal[x][i];
				const int to = wallHorizontal[x][i + 1];
				for (int y = from; y < to; ++y){
					pocket[x][y] = true;
					++answer;
				}
			}
		}

		//‚’¼
		for (int y = 0; y < SIZE * 2; ++y){
			for (int i = 1; i + 1 < wallVertical[y].size(); i += 2){
				const int from = wallVertical[y][i];
				const int to = wallVertical[y][i + 1];
				for (int x = from; x < to; ++x){
					if (!pocket[x][y]){
						++answer;
					}
					pocket[x][y] = true;
				}
			}
		}

		printf("Case #%d: %d\n", testCase, answer);
	}
}
