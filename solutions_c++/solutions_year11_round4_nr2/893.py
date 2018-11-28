#include <iostream>
#include <cmath>
using namespace std;

const int MaxN= 500 + 10;
const double eps= 1e-7;
int r, c;
int ms[MaxN][MaxN];
double cmX[MaxN][MaxN], cmY[MaxN][MaxN];
int m[MaxN][MaxN];


inline void setDyn(){
	ms[0][0]= m[0][0];
	cmX[0][0]= cmY[0][0]= 0;
	
	for (int i=1 ; i<r ; i++){
		ms[i][0]= ms[i-1][0] + m[i][0];
		cmX[i][0]= (cmX[i-1][0] * ms[i-1][0] + i*m[i][0]) / ms[i][0];
		cmY[i][0]= (cmY[i-1][0] * ms[i-1][0] + 0*m[i][0]) / ms[i][0];
		
	}
	
	for (int i=1 ; i<c ; i++){
		ms[0][i]= ms[0][i-1] + m[0][i];
		cmX[0][i]= (cmX[0][i-1] * ms[0][i-1] + 0*m[0][i]) / ms[0][i];
		cmY[0][i]= (cmY[0][i-1] * ms[0][i-1] + i*m[0][i]) / ms[0][i];
	}
	
	
	for (int i=1 ; i<r ; i++)
		for (int j=1 ; j<c ; j++){
			ms[i][j]= ms[i-1][j] + ms[i][j-1] - ms[i-1][j-1] + m[i][j];
			
			cmX[i][j]= (i*m[i][j] + cmX[i-1][j]*ms[i-1][j] + cmX[i][j-1]*ms[i][j-1] - cmX[i-1][j-1]*ms[i-1][j-1])/ms[i][j];
			cmY[i][j]= (j*m[i][j] + cmY[i-1][j]*ms[i-1][j] + cmY[i][j-1]*ms[i][j-1] - cmY[i-1][j-1]*ms[i-1][j-1])/ms[i][j];
		}
}
/****************************/
inline bool good(int x, int y){
	return x>=0 && y>=0 && x<r && y<c;
}
/****************************/
inline bool eq(double a, double b){
	return abs(a-b)<eps;
}
/*****************************/
inline double mass(int x1, int y1, int x2, int y2){
	double S1= 0;
	double S2= 0;
	double S3= 0;
	double S4= 0;
	
	S1= ms[x2][y2];
	if (good(x1-1, y2))
		S2= ms[x1-1][y2];
	if (good(x2, y1-1))
		S3= ms[x2][y1-1];
	if (good(x1-1, y1-1))
		S4= ms[x1-1][y1-1];
	
	double res= S1-S2-S3+S4;
	res-= m[x1][y1] + m[x1][y2] + m[x2][y1] + m[x2][y2];
	
	return res;
}
/****************************/
inline double CmX(int x1, int y1, int x2, int y2){
	double S1= 0;
	double S2= 0;
	double S3= 0;
	double S4= 0;

	S1= cmX[x2][y2] * ms[x2][y2];
	if (good(x1-1, y2))
		S2= cmX[x1-1][y2] * ms[x1-1][y2];
	if (good(x2, y1-1))
		S3= cmX[x2][y1-1] * ms[x2][y1-1];
	if (good(x1-1, y1-1))
		S4=  cmX[x1-1][y1-1] * ms[x1-1][y1-1];
	
	double res= S1-S2-S3+S4;
	res-= x1*m[x1][y1] + x1*m[x1][y2] + x2*m[x2][y1] + x2*m[x2][y2];
	
	return res / mass(x1, y1, x2, y2);
}
/****************************/
inline double CmY(int x1, int y1, int x2, int y2){
	double S1= 0;
	double S2= 0;
	double S3= 0;
	double S4= 0;
	
	S1= cmY[x2][y2] * ms[x2][y2];
	if (good(x1-1, y2))
		S2= cmY[x1-1][y2] * ms[x1-1][y2];
	if (good(x2, y1-1))
		S3= cmY[x2][y1-1] * ms[x2][y1-1];
	if (good(x1-1, y1-1))
		S4=  cmY[x1-1][y1-1] * ms[x1-1][y1-1];
	
	double res= S1-S2-S3+S4;
	res-= y1*m[x1][y1] + y2*m[x1][y2] + y1*m[x2][y1] + y2*m[x2][y2];
	
	return res / mass(x1, y1, x2, y2);
}
/******************************************/
int main(){
	int test;
	cin >> test;
	for (int t=1 ; t<=test ; t++){
		cout << "Case #" << t << ": ";
		int d;
		cin >> r >> c >> d;
		
		for (int i=0 ; i<r ; i++)
			for (int j=0 ; j<c ; j++){
				char ch;
				scanf(" %c", &ch);
				m[i][j]= (ch-'0') + d;
			}
		setDyn();
		int max= -1;
		for (int i=0 ; i<r ; i++)
			for (int j=0 ; j<c ; j++)
				for (int k=2 ; k+i<r && k+j<c ; k++){
					double X= CmX(i, j, i+k, j+k);
					double Y= CmY(i, j, i+k, j+k);
					double x= i + (double)k/2;
					double y= j + (double)k/2;
					if (eq(X, x) && eq(Y, y) && k>max)
						max= k;
				}
		if (max==-1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << max+1 << endl;
	}
	return 0;
}