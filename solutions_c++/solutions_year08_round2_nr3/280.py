#include <iostream>
#include <fstream>
#include <vector>
#include <complex>
using namespace std;

typedef complex<double> P;

#define EQ(x,y) (abs((x)-(y))<1E-10)


int table[1000010];

int main(){
	long N,K,n;
//	ifstream cin("C-sample.txt"); 
	cin >> N;
	int i,j,k;
	for (int q=0;q<N;q++) {
		vector<P> tree;
		cin >> K >> n;

		int pos=1;
		for (i=1;i<=K;i++) table[i]=0;
		for (i=1;i<=K;i++) {
			for (j=1;;) {
				if (table[pos]==0) {
					j++;
					if (j>i) break;
				}
				pos=(pos)%K+1;
			}
			table[pos]=i;
		}

		cout << "Case #" <<  (q+1) << ":";
		for (i=0;i<n;i++) {
			cin >> j;
			cout << " " << table[j] ;
		}
		cout << endl;
	}
}

