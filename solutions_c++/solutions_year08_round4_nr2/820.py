#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;




int main(){
	long long C;
//	ifstream cin("B-sample.txt"); 
	cin >> C;
	int i,j,k;
	long N,M,A;
	for (int q=0;q<C;q++) {
		cin >> N >> M >> A;
		int a=0,b=0,x=0,y=0;
		cout << "Case #" <<  (q+1) << ": " ;
		N++;M++;
		for (i=0;i<N;i++) {
			int x1=i , y1=0;
			for (j=i+1;j<N*M;j++) {
				int x2=j%N-x1 , y2=j/N-y1;
				for (k=j+1;k<N*M;k++) {
					int x3=k%N-x1 , y3=k/N-y1;
					if (abs(x2*y3-x3*y2) == A) {
						cout << x1 << " " << y1 << " "<< x2+y1 << " " << y2+y1 << " "  << x3+y1 << " " << y3+y1 << endl;
						goto OK;
					}

				}
			}
		}
NG:
		cout << "IMPOSSIBLE" << endl;
OK:
;

	}
}

