#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream filein("c.in");
	ofstream fileout("c.out");
	int T, N, S, p;
	int i,j,k,m,n;
	int a, b, sum;
	filein >> T;

	for (i=1;i<=T;i++) {
		filein >> N >> S >> p;
		p=p*3;
		a=0;b=0;

		for (j=1;j<=N; j++) {
			filein >> m;
			if ((m>=p-2)&&((m>=1)||(p==0))) {
					a++;
				} else {
					if (((m>=2)||(p==0))&&(m>=p-4)){
						b++;
					}
			}
		}
	//	fileout << "a=" << a << " b=" << b;
		if (b>S) b=S;
		sum = a+b;
		fileout << "Case #" << i <<": "
			<< sum;
		if (i<T) fileout << endl;
	}
	return 0;
}