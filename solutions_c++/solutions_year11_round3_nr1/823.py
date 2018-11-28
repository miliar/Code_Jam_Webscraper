#include <iostream>
using namespace std;

char a[55][55];

void process(int x , int y)
{
	a[x][y] = '/';
	a[x + 1][y + 1] = '/';
	a[x + 1][y] = '\\';
	a[x][y + 1] = '\\';
}

bool check(int x , int y , int n , int m)
{
	if (x + 1 < n && y + 1 < m) {
		if (a[x][y] == '#' && a[x + 1][y] == '#' && a[x][y + 1] == '#' && a[x + 1][y + 1] == '#')
			return true;
		
		return false;
	}

	return false;
}

bool solve(int n , int m)
{
	for (int i=0 ; i<n ; i++) {
		for (int j=0 ; j<m ; j++) {
			if (a[i][j] == '#') {
				if (check(i , j , n , m)) {
					process(i , j);
				}
				else
					return false;
			}
		}
	}

	return true;
}

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	
	int t;
	int n , m;
	int cas = 0;

	scanf("%d" , &t);
	while (t--) {
		
		cas++;

		scanf("%d %d" , &n , &m);
		for (int i=0 ; i<n ; i++) {
			scanf("%s" , a[i]);
		}

		printf("Case #%d:\n" , cas);
		if (solve(n , m)) {
			for (int i=0 ; i<n ; i++) {
				printf("%s\n" , a[i]);
			}
		}
		else {
			printf("Impossible\n");
		}
	}

	return 0;
}