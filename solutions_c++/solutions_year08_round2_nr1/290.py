#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <set>
#include <sstream>

using namespace std;

int main (void) {
	ofstream OUT;
	OUT.open ("OU.txt");
	ifstream FILE("IN.txt");
	int Num;
	FILE>>Num;
	for (int z=1; z<=Num; z++) {
		long long n, A, B, C, D, x0, y0, M;
		FILE>>n>>A>>B>>C>>D>>x0>>y0>>M;
		long long X=x0, Y=y0;
		
		vector <vector <long long> > w(3, vector <long long> (3,0));
		
		w[X%3][Y%3]++;
		for (int i=1; i<n; i++) {
			X=(A * X + B)%M;
			Y=(C * Y + D)%M;
			w[X%3][Y%3]++;
			}
		
		long long res=0;
	//	cout<<z<<"\n";
	//	cout<<res<<"\n";
		for (int i=0; i<3; i++) for (int j=0; j<3; j++) if (w[i][j]>=3) res+=(w[i][j]*(w[i][j]-1)*(w[i][j]-2))/6;
		for (int i=0; i<3; i++) res+=w[i][0]*w[i][1]*w[i][2];
		for (int i=0; i<3; i++) res+=w[0][i]*w[1][i]*w[2][i];
		res+=w[0][0]*w[1][1]*w[2][2];
		res+=w[1][0]*w[2][1]*w[0][2];
		res+=w[2][0]*w[0][1]*w[1][2];
		res+=w[0][2]*w[1][1]*w[2][0];
		res+=w[1][2]*w[2][1]*w[0][0];
		res+=w[2][2]*w[0][1]*w[1][0];
		
		long long R,r;
		R=res/10000000;
		r=res%10000000;
		cout<<res<<"\n"<<R<<" "<<r<<"\n\n\n";
		OUT<<"Case #"<<z<<": "<<res<<"\n";
		}
	FILE.close();
	OUT.close();
	system("PAUSE");
	return 0;
	}
