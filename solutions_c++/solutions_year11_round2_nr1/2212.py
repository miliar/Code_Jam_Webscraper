#include <stdio.h>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <limits.h>


using namespace std;
int nc() { char a = '\n';while(a == '\n'){ scanf( "%c", &a );} return a; }
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

int T;
int M[100][2],N;
double D[100][4];
bool C[100][100][2];

int main( )
{
	freopen( "D:\\input.txt", "r", stdin );
	freopen( "D:\\output.txt", "w", stdout );
	cout.precision(12);
	T = ni();
	long double result = 0;
	for(int t = 0; t < T; ++ t )
	{
		N = ni();
		for(int i=0;i<N;i++){
			M[i][0] = M[i][1] = 0;		
			D[i][0] = D[i][1] = D[i][2] = D[i][3] = 0;
		}
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				C[i][j][0] = true;
				char temp = nc();
				switch(temp){
				case '.':
					C[i][j][0] = false;
					break;
				case '1':
					M[i][0]++;
					M[i][1]++;
					C[i][j][1] = true;
					break;
				case '0':
					M[i][0]++;
					C[i][j][1] = false;
					break;
				}
			}
			D[i][0] = ((double)M[i][1]) / M[i][0];
			for(int j=0;j<i;j++){
				if(C[i][j][0]){
					D[j][1] += (C[i][j][1]?((M[i][1]-1.)/(M[i][0]-1.)):((M[i][1])/(M[i][0]-1.)));
				}
			}
			for(int j=i+1;j<N;j++){
				if(C[i][j][0]){
					D[j][1] += (C[i][j][1]?((M[i][1]-1.)/(M[i][0]-1.)):((M[i][1])/(M[i][0]-1.)));
				}
			}
		}
		for(int i=0;i<N;i++){
			D[i][1] /= M[i][0];
			for(int j=0;j<i;j++){
				if(C[i][j][0]){
					D[j][2] += D[i][1];
				}
			}
			for(int j=i+1;j<N;j++){
				if(C[i][j][0]){
					D[j][2] += D[i][1];
				}
			}
		}
		for(int i=0;i<N;i++){
			D[i][2] /= M[i][0];
			D[i][3] = (0.25 * D[i][0] + 0.50 * D[i][1] + 0.25 * D[i][2]);
		}
		printf( "Case #%d:\n", t + 1);
		for(int i=0;i<N;i++){
			cout << D[i][3] << endl;
		}
	}
	return 0;
}
