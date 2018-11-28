#include<iostream> 
#include<cstdio> 
#include<cmath> 
#include<algorithm>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<ctime>
#include<cassert>
#include<queue>

#define LL long long
#define mp make_pair
#define f first
#define s second
#define pii pair<int, int>
#define pb push_back

using namespace std;

const int N = (int) 4, M = (int) 10;

int t, sum[M], f[N][N];

int main() {
	freopen("a.in", "r", stdin);
	freopen(".out", "w", stdout);

    cin >> t;

    for (int i = 0; i < t; i++) {
    	bool o = false, x = false, fin = false;
		for (int j = 0; j < M; j++)
			sum[j] = 0;
								
    	for (int j = 0; j < N; j++) 
    		for (int k = 0; k < N; k++) {
    			char ch;
    			cin >> ch;
    							  			
				if (ch == 'X')
					f[j][k] = 2;
				if (ch == 'O')
					f[j][k] = 0;
				if (ch == 'T')
					f[j][k] = 1;
				if (ch == '.')
					f[j][k] = 200;

				sum[j] += f[j][k];
				sum[4 + k] += f[j][k];
				if (k == j)
					sum[8] += f[j][k];
				if (k == N - 1 - j)
					sum[9] += f[j][k];												
			}
		for (int j = 0; j < M; j++) {
			if (sum[j] == 0 || sum[j] == 1)
				o = true;
			if (sum[j] == 8 || sum[j] == 7)
				x = true;
			if (sum[j] >= 200)
				fin = true;
		}

/*		for (int j = 0; j < N; j++, cout << endl)
			for (int k = 0; k < N; k++)
				cout << f[j][k] << ' ';
		cout << endl;*/

		cout << "Case #" << i + 1 << ": ";
//		cout << x << ' ' << o << ' ' << fin << ' ';

		if (x && o || !x && !o && !fin)
			cout << "Draw";
		else
			if (x)
				cout << "X won";
			else
				if (o)
					cout << "O won";
				else
					cout << "Game has not completed";
		cout << endl;
	}
	return 0;
}