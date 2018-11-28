#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int N;

int main(){
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	scanf("%d",&N);
	for (int po = 0; po < N; po++){
		__int64 A;
		__int64 B,D,C,x0,y0,M,n;
		cin >> n;
		cin >> A;
		cin >> B;
		cin >> C;
		cin >> D;
		cin >> x0;
		cin >> y0;
		cin >> M;
		__int64 a[3][3];
		__int64 b[3][3];
		a[0][0] = a[0][1] = a[0][2] = a[1][0] = a[1][1] = a[1][2] = a[2][0] = a[2][1] = a[2][2] = 0;
		b[0][0] = b[0][1] = b[0][2] = b[1][0] = b[1][1] = b[1][2] = b[2][0] = b[2][1] = b[2][2] = 0;

		__int64 x = x0;
		__int64 y = y0;

		__int64 rx = x % 3;
		__int64 ry = y % 3;

		a[rx][ry]++;
		for (__int64 i = 0; i < n-1; i++){
			x = ((A * x + B) % M);
			y = ((C * y + D) % M);
			rx = x % 3;
			ry = y % 3;
			a[rx][ry]++;
		}
		__int64 res = 0;

		for (__int64 i = 0; i < 3; i++){
			for (__int64 j = 0; j < 3; j++){
				if (a[i][j] >= 3){
					__int64 k = a[i][j];
					res += (k*(k-1)*(k-2))/6; 
				}
			}
		}
		for (__int64 i1 = 0; i1 < 3; i1++){
			for (__int64 j1 = 0; j1 < 3; j1++){
				for (__int64 i2 = i1; i2 < 3; i2++){
					for (__int64 j2 = 0; j2 < 3; j2++){
						for (__int64 i3 = i2; i3 < 3; i3++){
							for (__int64 j3 = 0; j3 < 3; j3++){
								if ((i1+i2+i3)%3) continue;
								if ((j1+j2+j3)%3) continue;
								if (i1 == i2 && i1 == i3 && j1 == j2 && j1 == j3) continue;
								if (i1 == i2 && i1 == i3 && (j1 > j2 || j1 > j3 || j2 > j3)) continue;
								if (j1 == j2 && j1 == j3 && (i1 > i2 || i1 > i3 || i2 > i3)) continue;
								res += a[i1][j1] * a[i2][j2] * a[i3][j3];
							}
						}
					}
				}
			}
		}

		printf("Case #%d: ", po+1);
		cout << res << "\n";
	}
	return 0;
}
