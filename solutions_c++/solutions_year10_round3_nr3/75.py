#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>

using namespace std;

int main() 
{
    freopen("A-small.in", "r", stdin);
    ofstream fp("A-small.out");

	char chess[512][512];
	int count[513];

	int T;
	scanf("%d", &T);

	for(int i = 0; i < T; i++)
	{
		int M, N;
		scanf("%d%d", &M, &N);

		int n = N / 4;

		for(int j = 0; j < M; j++) {
			for(int k = 0; k < n; k++) {
				char c;
				cin >> c;
				int m = k * 4;
				switch(c) {
					case '0':
						chess[j][m] = '0';
						chess[j][m+1] = '0';
						chess[j][m+2] = '0';
						chess[j][m+3] = '0';
						break;
					case '1':
						chess[j][m] = '0';
						chess[j][m+1] = '0';
						chess[j][m+2] = '0';
						chess[j][m+3] = '1';
						break;
					case '2':
						chess[j][m] = '0';
						chess[j][m+1] = '0';
						chess[j][m+2] = '1';
						chess[j][m+3] = '0';
						break;
					case '3':
						chess[j][m] = '0';
						chess[j][m+1] = '0';
						chess[j][m+2] = '1';
						chess[j][m+3] = '1';
						break;
					case '4':
						chess[j][m] = '0';
						chess[j][m+1] = '1';
						chess[j][m+2] = '0';
						chess[j][m+3] = '0';
						break;
					case '5':
						chess[j][m] = '0';
						chess[j][m+1] = '1';
						chess[j][m+2] = '0';
						chess[j][m+3] = '1';
						break;
					case '6':
						chess[j][m] = '0';
						chess[j][m+1] = '1';
						chess[j][m+2] = '1';
						chess[j][m+3] = '0';
						break;
					case '7':
						chess[j][m] = '0';
						chess[j][m+1] = '1';
						chess[j][m+2] = '1';
						chess[j][m+3] = '1';
						break;
					case '8':
						chess[j][m] = '1';
						chess[j][m+1] = '0';
						chess[j][m+2] = '0';
						chess[j][m+3] = '0';
						break;
					case '9':
						chess[j][m] = '1';
						chess[j][m+1] = '0';
						chess[j][m+2] = '0';
						chess[j][m+3] = '1';
						break;
					case 'A':
						chess[j][m] = '1';
						chess[j][m+1] = '0';
						chess[j][m+2] = '1';
						chess[j][m+3] = '0';
						break;
					case 'B':
						chess[j][m] = '1';
						chess[j][m+1] = '0';
						chess[j][m+2] = '1';
						chess[j][m+3] = '1';
						break;
					case 'C':
						chess[j][m] = '1';
						chess[j][m+1] = '1';
						chess[j][m+2] = '0';
						chess[j][m+3] = '0';
						break;
					case 'D':
						chess[j][m] = '1';
						chess[j][m+1] = '1';
						chess[j][m+2] = '0';
						chess[j][m+3] = '1';
						break;
					case 'E':
						chess[j][m] = '1';
						chess[j][m+1] = '1';
						chess[j][m+2] = '1';
						chess[j][m+3] = '0';
						break;
					case 'F':
						chess[j][m] = '1';
						chess[j][m+1] = '1';
						chess[j][m+2] = '1';
						chess[j][m+3] = '1';
						break;
				}
			}
		}

		/*cout << M << endl << N << endl;
		for(int j = 0; j < M; j++) {
			for(int k = 0; k < N; k++) {
				cout << chess[j][k];
			}
			cout << endl;
		}
		cout <<endl;*/

		memset(count, 0, sizeof(count));
		for(int j = min(M, N); j >= 1; --j) {
			int cnt = 0;
			for(int p = 0; p <= M-j; p++) {
				for(int q = 0; q <= N - j; q++) {

					bool mark = true;

					for(int a = p; a < p + j; a++) {
						for(int b = q; b < q + j; b++) {
							if(chess[a][b] == '2') {
								mark = false;
								break;
							}
							if(a > p && chess[a][b] == chess[a-1][b]) {
								mark = false;
								break;
							}
							if(b > q && chess[a][b] == chess[a][b-1]) {
								mark = false;
								break;
							}
						}
						if(!mark) break;
					}

					if(mark) {
						cnt++;
						for(int a = p; a < p + j; a++) {
							for(int b = q; b < q + j; b++) {
								chess[a][b] = '2';
							}
						}
						
					}

				}
			}

			count[j] = cnt;
		}

		int res = 0;
		for(int j = 1; j <= min(M,N); j++) {
			if(count[j] > 0) {
				res++;
			}
		}
		
		fp << "Case #" << i+1 << ": " << res << endl;
		for(int j = min(M, N); j >= 1; --j) {
			if(count[j] > 0) {
				fp << j << " " << count[j] << endl;
			}
		}
	}

    fp.close();
    return 0;
}