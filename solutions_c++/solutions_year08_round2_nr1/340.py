#include <cstdio>
#include <string>
#include <iostream>
#include <fstream>

using namespace std ;

//#define	FILE_IN			"A-small.in"
//#define	FILE_OUT		"A-small.out"
#define	FILE_IN			"A-large.in"
#define	FILE_OUT		"A-large.out"
#define	INF					1000000
#define MIN(a, b)	((a) < (b) ? (a) : (b))
#define MAXN				10005
#define ok(a, b, c) (((a) + (b) + (c)) % 3 == 0)
#define smaller(x1, y1, x2, y2) (((x1) < (x2) || ((x1) == (x2) && ((y1) <= (y2)))))

int num_tests, n ;
long long A, B, C, D, x0, y0, M ;
long long t [3] [3], best ;

int main(int argc, char **argv) {
	ifstream in(FILE_IN) ;
	ofstream out(FILE_OUT) ;
	
	in >> num_tests ;
	for (int test = 1 ; test <= num_tests ; test ++) {
		in >> n >> A >> B >> C >> D >> x0 >> y0 >> M ;
		best = 0 ;
		for (int i1 = 0 ; i1 < 3 ; i1 ++) 
			for (int j1 = 0 ; j1 < 3 ; j1 ++) t [i1] [j1] = 0 ;
		t [x0 % 3] [y0 % 3] ++ ; 
		for (int i = 1 ; i < n ; i ++) {
			x0 = (A * x0 + B) % M ;
			y0 = (C * y0 + D) % M ;
			t [x0 % 3] [y0 % 3] ++ ;
		}
		
		for (int i1 = 0 ; i1 < 3 ; i1 ++) {
			for (int j1 = 0 ; j1 < 3 ; j1 ++) if (t [i1] [j1] > 0) {
				for (int i2 = 0 ; i2 < 3 ; i2 ++) {
					for (int j2 = 0 ; j2 < 3 ; j2 ++) if (smaller(i1, j1, i2, j2) && t [i2] [j2] > 0) {												
						int i3 = (6 - i1 - i2) % 3 ;
						int j3 = (6 - j1 - j2) % 3 ;
						if (t [i3] [j3] > 0 && smaller(i2, j2, i3, j3)) {
							if (i3 != i2 || j3 != j2) {
								if (i2 != i1 || j2 != j1) {
									if (i3 != i1 || j3 != j1)
										best += t [i1] [j1] * t [i2] [j2] * t [i3] [j3] ;
									else
										if (t [i1] [j1] > 1)
											best += t [i1] [j1] * (t [i1] [j1] - 1) * t [i2] [j2] / 2 ;
								}
								else
									if (t [i1] [j1] > 1) 
										best += t [i1] [j1] * t [i3] [j3] * (t [i1] [j1] - 1) / 2 ;
							}
							else {
								if (i3 != i1 || j3 != j1) {
									if (t [i2] [j2] > 1)
										best += t [i1] [j1] * t [i2] [j2] * (t [i2] [j2] - 1) / 2 ;
								}
								else {
									if (t [i1] [j1] > 2) 
										best += t [i1] [j1] * (t [i1] [j1] - 1) * (t [i1] [j1] - 2) / 6 ;
								}
							}
						}
					}
				}
			}

		}
		
		out << "Case #" << test << ": " << best << endl ;
	}
//	int tmp ;
//	cin >> tmp ;
		
	return 0 ;
}


