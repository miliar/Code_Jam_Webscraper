#include <iostream>
#include <cstdio>
#define LL long long
#define LD long double
#define SIZE 987

using namespace std;

LL n, T, z, i, j, b, ans[SIZE], k;
char w[SIZE][SIZE];

int main() {

#if 0
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif
	
	ans[0] = 'O' * 'O' * 'O' * 'O';
	ans[1] = 'O' * 'O' * 'O' * 'T';
	ans[2] = 'X' * 'X' * 'X' * 'X';
	ans[3] = 'X' * 'X' * 'X' * 'T';
	cin>>T;
	for (z = 1; z <= T; z++) {
		b = 0;
		for (i = 0; i < 4; i++) cin>>w[i];
		scanf(" ");
		for (i = 0; i < 4; i++)
			for (j = 0; j < 4; j++)
				if (w[i][j] == '.') 
					b = 1;
			
		for (i = 0; i < 4; i++) {
			k = 1;
			for (j = 0; j < 4; j++) k *= w[i][j];
			for (j = 0; j < 2; j++) if (k == ans[j]) b = 2;
			for (j = 2; j < 4; j++) if (k == ans[j]) b = 3;
			k = 1;
			for (j = 0; j < 4; j++) k *= w[j][i];
			for (j = 0; j < 2; j++) if (k == ans[j]) b = 2;
			for (j = 2; j < 4; j++) if (k == ans[j]) b = 3;
		}
		k = 1;
		for (i = 0; i < 4; i++) k*=w[i][i];
		for (j = 0; j < 2; j++) if (k == ans[j]) b = 2;
		for (j = 2; j < 4; j++) if (k == ans[j]) b = 3;

		k = 1;
		for (i = 0; i < 4; i++) k*=w[3 - i][i];
		for (j = 0; j < 2; j++) if (k == ans[j]) b = 2;
		for (j = 2; j < 4; j++) if (k == ans[j]) b = 3;
		
		cout<<"Case #"<<z<<": ";
		if (b == 1) cout<<"Game has not completed"<<endl;
		if (b == 2) cout<<"O won"<<endl;
		if (b == 3) cout<<"X won"<<endl;
		if (b == 0) cout<<"Draw"<<endl;
	}
	return 0;
}
