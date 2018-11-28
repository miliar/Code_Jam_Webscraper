#include<iostream>
#include<cstring>
#define endl '\n'
#define Inf 0xFFFFFFFF

using namespace std;

int h[128][128];
int m, n, m1;
int boss[128*128];
bool used[128*128];
char who[128*128];

int fd(int t){
	int k = t;
	while(boss[k] != k) k = boss[k];
	while(boss[t] != t){
		int tmp = t;
		t = boss[t];
		boss[tmp] = k;
	}

	return k;
}

void uni(int a, int b){
	boss[fd(a)] = fd(b);
}

int main(){
	int tc;

	cin >> tc;
	for(int cs = 1; cs <= tc; ++cs){
		cin >> m >> n;
		m1 = n + 2;

		memset(used, 0, sizeof(used));
		memset(h, 0x7F, sizeof(h));
		for(int i = 1; i <= m; ++i)
			for(int j = 1; j <= n; ++j)
				cin >> h[i][j];

		for(int i = 0; i < m1 * (m+1); ++i)
			boss[i] = i;

		for(int i = 1; i <= m; ++i)
			for(int j = 1; j <= n; ++j){
				int k = h[i][j];
				int t = 0;

				if(h[i-1][j] < k){
					k = h[i-1][j];
					t = 1;
				}
				if(h[i][j-1] < k){
					k = h[i][j-1];
					t = 2;
				}
				if(h[i][j+1] < k){
					k = h[i][j+1];
					t = 3;
				}
				if(h[i+1][j] < k){
					k = h[i+1][j];
					t = 4;
				}

				switch(t){
					case 1:
						uni(i * m1 + j, (i-1) * m1 + j);
						break;
					case 2:
						uni(i * m1 + j, i * m1 + j - 1);
						break;
					case 3:
						uni(i * m1 + j, i * m1 + j + 1);
						break;
					case 4:
						uni(i * m1 + j, (i+1) * m1 + j);
						break;
				}
			}



		for(int i = 1, k = 'a'; i <= m; ++i)
			for(int j = 1; j <= n; ++j){
				int tmp = fd(m1 * i + j);

				if(!used[tmp]){
					used[tmp] = true;
					who[tmp] = k;
					who[m1*i + j] = k++;
				}else
					who[m1*i + j] = who[tmp];

			}


		cout << "Case #" << cs << ":" << endl;
		
		for(int i = 1; i <= m; ++i){
			cout << who[i*m1 + 1];
			for(int j = 2; j <= n; ++j)
				cout << ' ' << who[i*m1 + j];
			cout << endl;
		}
		
	}

	return 0;
}
