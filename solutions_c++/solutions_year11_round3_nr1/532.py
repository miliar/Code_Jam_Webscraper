#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

const int maxn = 55;
int T, R, C;
char data[maxn][maxn];
bool vis[maxn][maxn];
int sum, count;

void Output();

void Proc() {
    count = 0;
    for (int i=0; i<R-1; ++i) {
	for (int j=0; j<C-1; ++j) {
	    if (vis[i][j]) continue;
	    if (data[i][j] == '#' &&
		data[i][j+1] == '#' &&
		data[i+1][j] == '#' &&
		data[i+1][j+1] == '#') {
		vis[i][j] = vis[i][j+1] = vis[i+1][j] = vis[i+1][j+1] = true;
		data[i][j] = '/';
		data[i][j+1] = '\\';
		data[i+1][j] = '\\';
		data[i+1][j+1] = '/';
		count += 4;
	    }
	}
    }
}

void Output() {
    for (int i=0; i<R; ++i,cout<<endl)
	for (int j=0; j<C; ++j)
	    cout << data[i][j];
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    cin >> T;
    for (int m=0; m<T; ++m) {
	cin >> R >> C;
	memset(vis, 0, sizeof(vis));
	sum = 0;
	for (int i=0; i<R; ++i)
	    for (int j=0; j<C; ++j) {
		cin >> data[i][j];
		if (data[i][j] == '#') sum++;
	    }

	cout << "Case #" << m+1 << ":" << endl;
	if (sum % 4 != 0) {
	    cout << "Impossible" << endl;
	} else if (sum == 0) {
	    Output();
	} else {
	    Proc();
	    if (count == sum) {
		Output();
	    } else {
		cout << "Impossible" << endl;
	    }
	}
    }
    

    return 0;
}
