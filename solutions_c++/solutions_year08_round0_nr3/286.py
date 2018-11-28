#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
#define PI 3.1415926537

int main(){
	int n;
	cin >> n;
	for( int m=0; m<n; m++ ){
		double f,R,t,r,g;
		cin >> f >> R >> t >> r >> g;
		
		int num_of_holes = (int)(R / ( g + 2*r )) + 1;
		double hr = g/2 - f;
		double hole = 0;
		if( hr > 0.000000001 ){
			for( int i = 0; i < num_of_holes; i++ ){
				for( int j = 0; j < num_of_holes; j++ ){
					double hx1 = i*(g+2*r) + r + f;
					double hy1 = j*(g+2*r) + r + f;
					double hx2 = i*(g+2*r) + r + g - f;
					double hy2 = j*(g+2*r) + r + g - f;
					double hp0 = sqrt( hx1*hx1 + hy1*hy1 );
					double hp1 = sqrt( hx2*hx2 + hy2*hy2 );

					double hx1_y = sqrt( (R-t-f)*(R-t-f) - hx1 * hx1 );
					double hy1_x = sqrt( (R-t-f)*(R-t-f) - hy1 * hy1 );
					double hx2_y = sqrt( (R-t-f)*(R-t-f) - hx2 * hx2 );
					double hy2_x = sqrt( (R-t-f)*(R-t-f) - hy2 * hy2 );

					if( hp1 < (R - t - f) ){
						double temp = hr*hr*4;
						hole += temp;
					}else if( hp0 > (R - t - f) ){
						hole += 0;
					}else{
						double temp = 0;
						double triS = 0;
						double p1x;
						double p1y;
						double p2x;
						double p2y;
						if( hy1 <= hx1_y && hx1_y <= hy2 && hx1 <= hy1_x && hy1_x <= hx2 ){
							p1x = hx1;
							p1y = hx1_y;
							p2x = hy1_x;
							p2y = hy1;

							triS = (p1y-hy1)*(p2x-hx1)/2;
						}
						if( hy1 <= hx1_y && hx1_y <= hy2 && hx2 < hy1_x ){
							p1x = hx1;
							p1y = hx1_y;
							p2x = hx2;
							p2y = hx2_y;

							triS = (hx2-hx1)*(p1y-p2y)/2 + (hx2-hx1)*(p2y-hy1);
						}
						if( hy2 < hx1_y && hx2 < hy1_x ){
							p1x = hy2_x;
							p1y = hy2;
							p2x = hx2;
							p2y = hx2_y;

							triS = (hy2-hy1)*(hx2-hx1) - (hy2-p2y)*(hx2-p1x)/2;
						}
						if( hy2 < hx1_y && hx1 <= hy1_x && hy1_x <= hx2 ){
							p1x = hy2_x;
							p1y = hy2;
							p2x = hy1_x;
							p2y = hy1;

							triS = (hy2-hy1)*(p2x-p1x)/2 + (hy2-hy1)*(p1x-hx1);
						}

						double arc = abs( acos( p1x / (R-t-f) ) - acos( p2x / (R-t-f) ) );
						double arcS = (R-t-f)*(R-t-f)*(arc/2 - cos(arc/2)*sin(arc/2));
						temp += triS + arcS;
						hole += temp;
					}
				}
			}
			hole *= 4;
		}

		double racquet = R*R*PI;

		double ans =1-hole/racquet;
		if( ans < 0.0000001 ) ans = 0;
		cout << "Case #" << (m+1) << ": " << ans << endl;
	}
}


