#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long lInt;

struct point{
	lInt x, y;
	void set (lInt x_, lInt y_){ x = x_; y = y_;}
};

point operator + (const point & p1, const point & p2){
	point r;
	r.set (p1.x+p2.x, p1.y+p2.y);
	return r;
}

point operator - (const point & p1, const point & p2){
	point r;
	r.set (p1.x-p2.x, p1.y-p2.y);
	return r;
}

typedef long double lDouble;

int main(){
	int nCases, iCases;
	cin >> nCases;

	for (iCases=1; iCases<=nCases; iCases++){
		int rows, cols, d;
		
		scanf("%d %d %d", &rows, &cols, &d);
		
		int i, j;
		lInt m;
		lInt mass[rows+1][cols+1], massSum[rows+1][cols+1];
		point pointSum[rows+1][cols+1];
		char c;
		point p;
		
		for (i=0; i<rows+1; i++){
			mass[i][0] = 0;
			massSum[i][0] = 0;
			pointSum[i][0].set(0,0);
		}
		
		for (j=0; j<cols+1; j++){
			mass[0][j] = 0;
			massSum[0][j] = 0;
			pointSum[0][j].set(0,0);
		}
		
		for (i=1; i<=rows; i++){
			for (j=1; j<=cols; j++){
				c = '\0';
				while (c<'0' or c>'9')
					scanf("%c", &c);
				
				mass[i][j] = d + (c-'0');
				//cout << mass[i][j] << ' ';
				
				pointSum[i][j] = pointSum[i][j-1] + pointSum[i-1][j] - pointSum[i-1][j-1];
				massSum[i][j] = massSum[i][j-1] + massSum[i-1][j] - massSum[i-1][j-1];
				
				p.set(mass[i][j]*i, mass[i][j]*j);
				pointSum[i][j] = pointSum[i][j] + p;
				massSum[i][j] += mass[i][j];
			}
		}
		//cout << endl;
		
		int maxk = 2;
		
		int xi, yi, xf, yf ,k;
		for (xi=0; xi<=rows; xi++) {
			for (yi=0; yi<=cols; yi++) {
				for (k = maxk+1; ;k++){
					xf = xi + k;
					yf = yi + k;
					if (xf > rows or yf > cols)
						break;
						
					p = pointSum[xf][yf] - pointSum[xf][yi] - pointSum[xi][yf] + pointSum[xi][yi];
					p.x -= mass[xf][yf]*xf + mass[xf][yi+1]*xf + mass[xi+1][yf]*(xi+1) + mass[xi+1][yi+1]*(xi+1);
					p.y -= mass[xf][yf]*yf + mass[xf][yi+1]*(yi+1) + mass[xi+1][yf]*yf + mass[xi+1][yi+1]*(yi+1);
		
					m = massSum[xf][yf] - massSum[xf][yi] - massSum[xi][yf] + massSum[xi][yi];
					m -= mass[xf][yf] + mass[xf][yi+1] + mass[xi+1][yf] + mass[xi+1][yi+1];
					
					//if (xi == 1 and yi==1 and k==5)
					//	cout << (p.x) << ' ' << (p.y) << ' ' << m;
					if ((2*p.x) % m == 0 and (2*p.x) / m == xi+xf+1 and
						(2*p.y) % m == 0 and (2*p.y) / m == yi+yf+1)
						maxk = k;
				}
			}
		}
			
		printf("Case #%d: ", iCases);
		
		if (maxk>=3)
			printf("%d\n", maxk);
		else
			printf("IMPOSSIBLE\n");
	}
	
	return 0;
}
