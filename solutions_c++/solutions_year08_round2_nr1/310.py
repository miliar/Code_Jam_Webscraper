#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <set>
#include <iterator>
#include <iomanip>

using namespace std;

int main()
{
	int C;
	cin >> C;
	for (int c=0;c<C;c++) {

		long long int n, A, B, C, D, x0, y0, M;

		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

		long long int X = x0, Y=y0;

		int p[3][3]={{0,0,0},{0,0,0},{0,0,0}};

		p[X%3][Y%3]++;

	//	cout <<  X << " "	 << Y << endl;
		for (int i=1; i<n;i++) {
			X = (A*X+B)%M;
			Y = (C*Y+D)%M;
		//	cout <<  X << " "	 << Y << endl;

			p[X%3][Y%3]++;
		}

		long long int possible = 0;
		for (int i1=0;i1<3;i1++) {
			for (int i2=0;i2<3;i2++) {
				for (int j1=0;j1<3;j1++) {
					for (int j2=0;j2<3;j2++) {
						for (int k1=0;k1<3;k1++) {
							for (int k2=0;k2<3;k2++) {
								long long int a = p[i1][i2], b=p[j1][j2], c=p[k1][k2];
								if (j1==i1 && j2==i2) b--;
								if (k1==i1 && k2==i2) c--;
								if (k1==j1 && k2==j2) c--;
								if ((((i1+j1+k1) % 3) == 0) && (((i2+j2+k2) % 3) == 0))
									possible += a*b*c;
							}
						}
					}
				}
			}
		}

		cout << "Case #" << c+1 << ": " << possible/6 << endl;
	}
}
