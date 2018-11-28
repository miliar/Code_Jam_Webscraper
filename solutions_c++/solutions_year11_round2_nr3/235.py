#include <iostream>

using namespace std;

int ans = 0;

void cal(int node, int min, int color[], int n, int m, int region[100][9]) {
	if (node > n) {
		int colors[9] = {0};
		int sum = 0;
		for(int i = 1; i<= n; i++) colors[color[i]] = 1;
		for(int i = 1; i<= n; i++) sum += colors[i];
		for (int i = 0; i <= m; i++) {
			int cc[9] = {0};
			for(int j = 1; j <= n; j++) {
				if (region[i][j]) {
					cc[color[j]] = 1;
				}
			}
			int t = 0;
			for(int j = 1; j <= n; j++) {
				t += cc[j];
			}
			if (t != sum) return;
		}
		if (ans < sum) ans = sum;
	} else {
		for(int i = 1; i <= min; i++) {
			color[node] = i;
			cal(node+1, min, color, n, m, region);
			if (ans == min) return;
		}
	}
}

int main (int argc, char const *argv[])
{
	int t;
	cin >> t;
	for(int index = 1; index <= t; index++) {
		int n, m;
		cin >> n >> m;
		int u[8];
		int v[8];
		for(int i = 0; i < m; i++) cin >> u[i];
		for(int i = 0; i < m; i++) cin >> v[i];
		int region[100][9] = {0};
		for(int i = 1; i <= n; i++) region[0][i] = 1;
		for(int i = 0; i < m; i++) {
			for(int j = 0; j <=i; j++) {
				if (region[j][u[i]] && region[j][v[i]]) {
					region[i+1][u[i]] = region[i+1][v[i]] = 1;
					int min = u[i] > v[i]?v[i]:u[i];
					int max = u[i] < v[i]?v[i]:u[i];
					for(int k = min+1; k < max; k++) {
						region[i+1][k] = region[j][k];
						region[j][k] = 0;
					}
					break;
				}
			}
		}
		int min = 1000;
		for(int i = 0; i <= m; i++) {
			for(int j = 1; j <= n; j++) {
				region[i][0] += region[i][j];
			}
			min = min < region[i][0]? min:region[i][0];
		}
		ans = 0;
		int color[9] = {0};
		cal(1, min, color, n, m, region);
		cout<<"Case #"<< index << ": " << ans << endl;
		for(int i = 1; i < n; i++) cout << color[i] << " ";
		cout << color[n] << endl;
			
	}
	return 0;
}