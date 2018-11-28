#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>
#include <sstream>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <complex>
#include <bitset>

#define PI 3.14159265358979
#define EPS 1E-10
#define INF 1000000000

using namespace std;

int state[100][100];
int vec[2][2];

int main()
{
	int N;
	cin >> N;
	for(int t = 1; t <= N; ++t)
	{
		int w, h;
		cin >> w >> h;
		for(int i = 0; i < 2; ++i)
		{
			for(int j = 0; j < 2; ++j) cin >> vec[i][j];
		}
		int start_x, start_y;
		cin >> start_x >> start_y;
		int num = 1;
		queue<int> que;
		que.push(start_x); que.push(start_y);
		memset(state, 0, 100 * 100 * 4);
		state[start_x][start_y] = 1;
		while(que.size())
		{
			int x = que.front(); que.pop();
			int y = que.front(); que.pop();
			for(int i = 0; i < 2; ++i)
			{
				int nx = x + vec[i][0], ny = y + vec[i][1];
				if(nx < 0 || ny < 0 || nx >= w || ny >= h) continue;
				if(state[nx][ny]) continue;
				state[nx][ny] = 1;
				que.push(nx); que.push(ny);
				++num;
			}
		}
		printf("Case #%d: ", t);
		printf("%d\n", num);
	}
	return 0;
}
