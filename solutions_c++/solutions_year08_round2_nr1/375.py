#include <iostream>
#include <fstream>
#include <vector>
#include <complex>
using namespace std;

typedef complex<double> P;

#define EQ(x,y) (abs((x)-(y))<1E-10)



int main(){
	long long N,n,A,B,C,D,x,y,M;
	//ifstream cin("A-sample.txt"); 
	cin >> N;
	int i,j,k;
	for (int q=0;q<N;q++) {
		vector<P> tree;
		cin >> n >> A >> B >> C >> D >> x >> y >> M;
		for (i=0;i<n;i++) {
			tree.push_back(P(x,y));
			//cout << x << "," << y << endl;
			x = (A*x+B)%M;
			y = (C*y+D)%M;
		}
		int a=0;
		for (k=0;k<n-2;k++) {
			for (j=k+1;j<n-1;j++) {
				for (i=j+1;i<n;i++) {
					P c = (tree[i]+tree[j]+tree[k])/3.0;
					if (EQ(c.real() , (int)c.real()) && EQ(c.imag() , (int)c.imag()))
						a++;
				}
			}
		}
		cout << "Case #" <<  (q+1) << ": " << a << endl;
	}
}

