#include <iostream>
#include <fstream>

using namespace std;

int main () {
	ofstream out;
	out.open("prob1.out", ios::out);
	ifstream in;
	in.open("prob1.in", ios::in);
	string line;
	if (!in) { cout << "sux in"; }
	if (!out) { cout << "sux out"; }
	int i,l , j, k; 
	long long tempx, tempy, tests, sumx, sumy;
	long long n, A, B, C, D, x0,y0, M;
	in >> tests;
	for (l=0; l<tests; l++) {
		int sol = 0;
		in >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		cout <<n<<A<<B<<C<<D<<x0<<y0<<M<<endl;		
		int p[n][2];
		p[0][0]=x0; p[0][1]=y0;
		cout << p[0][0] << " " << p[0][1] << endl;
		for (i=1; i<n; i++) {
			p[i][0] = (A * p[i-1][0] + B) % M;
			p[i][1] = (C * p[i-1][1] + D) % M;
			cout << p[i][0] << " " << p[i][1] << endl;
		}
		for (i=0; i<n-2; i++) {
			for (j=i+1; j<n-1; j++) {
				for (k=j+1; k<n; k++) {
					sumx = ((p[i][0] % 3) + (p[j][0] % 3)  + (p[k][0]%3));
					tempx = sumx % 3;
					sumy = ((p[i][1] % 3) + (p[j][1] %3) + (p[k][1]%3));
					tempy = sumy % 3;
					if ( (tempx==0) && (tempy==0) ) {
						sol++; 
						//cout <<i<<" "<<j<<" "<<k<<": ";					
						//cout << "sumx=" << sumx << " sumy=" << sumy;
						//cout << "tempx=" << tempx << "tempy=" << tempy <<endl;
					}
				}
			}
		}
		out << "Case #" << l+1 << ": " << sol<< endl;
	}
	return 0;
}
