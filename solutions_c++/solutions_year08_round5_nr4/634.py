#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <stack>

using namespace std;

int B[200][200];
int H, W, R;

int xx(int x, int y) {
	int ans = 0;
	
	if (B[x][y] == -1) return 0;
	else if (B[x][y] >= 0) return B[x][y];
	
	if (x > H || y > W) return 0;
	
	if (x == H && y == W) return 1;
	
	ans = xx(x + 2, y + 1) + xx(x + 1, y + 2);
	
	ans = ans % 10007;
	
	B[x][y] = ans;
	
	return ans;
}
	
	
void calc(int no)
{
	int i, j;
	int ans;
	
	
	cin >> H >> W >> R;
	
	int x, y;
	
	
	for (i = 0; i < 200; i++) for (j = 0; j < 200; j++) B[i][j] = -2;
	
	while (R-- > 0) {
		cin >> x >> y;
		B[x][y] = -1;
	}
	
	ans = xx(1, 1);
	ans = ans % 10007;
	
	printf("Case #%d: %d\n", no, ans);
	
	return;
}

int main()
{
	int n;
	int i;
	
	cin >> n;
	
	for (i = 0; i < n; i++) {
		calc(i + 1);
	}
	
	return 0;
}
