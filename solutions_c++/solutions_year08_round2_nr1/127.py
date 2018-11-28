#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main() {
	ifstream inp("a.in");
	ofstream out("a.out");
	int N;
	inp >> N;
	for (int test=1;test<=N;test++) {
		out << "Case #" << test << ": ";

		int n;
		long long A,B,C,D,x0,y0,M;
		inp >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		int c[3][3] = {0};
		c[x0%3][y0%3]=1;
		for (int i=0; i<n-1; i++) {
			x0=(A*x0+B)%M;
			y0=(C*y0+D)%M;
			c[x0%3][y0%3]++;
		}
		long long sum=0;
		for (int a0=0;a0<3;a0++) {
			for (int b0=0;b0<3;b0++) {
				for (int a1=0;a1<3;a1++) {
					for (int b1=0;b1<3;b1++) {
						for (int a2=0; a2<3; a2++) {
							for (int b2=0; b2<3; b2++) {
								if ((a0+a1+a2)%3==0&&(b0+b1+b2)%3==0) {
									long long t1=c[a0][b0];
									long long t2=c[a1][b1]; if (a0==a1&&b0==b1) t2--;
									long long t3=c[a2][b2]; if (a0==a2&&b0==b2) t3--;
									if (a1==a2&&b1==b2) t3--;
									if (t1>0&&t2>0&&t3>0) {
										sum+=t1*t2*t3;
									}
								}
							}
						}
					}
				}
			}
		}
		out << sum/6;
		out << endl;
	}
}

