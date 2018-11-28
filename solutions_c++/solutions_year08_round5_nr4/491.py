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
		int H,W,R;
		FILE>>H>>W>>R;
		vector <vector <int> > a(200, vector <int> (200, 0));
		for (int i=0; i<R; i++) {
			int x, y;
			FILE >>x>>y;
			a[x-1][y-1]=-1;
			}
//		for (int i=0; i<H; i++) {for (int j=0; j<H; j++) cout<<a[i][j]<<" "; cout<<"\n";}
		a[0][0]=1;
		for (int i=0; i<H; i++) {
			for (int j=0; j<W; j++) if (a[i][j]>0) {
				if (i+2<H && j+1<W) if (a[i+2][j+1]!=-1) {a[i+2][j+1]+=a[i][j]; a[i+2][j+1]%=10007;}
				if (i+1<H && j+2<W) if (a[i+1][j+2]!=-1) {a[i+1][j+2]+=a[i][j]; a[i+1][j+2]%=10007;}
				}
			}
		
		OUT<<"Case #"<<z<<": "<<a[H-1][W-1]<<"\n";
		}
	FILE.close();
	OUT.close();
	system("PAUSE");
	return 0;
	}
