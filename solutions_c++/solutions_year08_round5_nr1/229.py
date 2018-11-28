#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <set>
#include <sstream>

using namespace std;

int N=210;

int main (void) {
	ofstream OUT;
	OUT.open ("OU.txt");
	ifstream FILE("IN.txt");
	vector <vector <int> > dire(4, vector <int> (2,0));
	dire[0][0]=1;
	dire[2][0]=-1;
	dire[1][1]=1;
	dire[3][1]=-1;
	
	int Num;
	FILE>>Num;
	for (int z=1; z<=Num; z++) {
		vector <vector <int> > a(N, vector<int>(N, 0));
		vector <vector <int> > b(N, vector<int>(N, 0));
		vector <vector <bool> > mX(N, vector<bool>(N, false));
		vector <vector <bool> > mY(N, vector<bool>(N, false));
		int x=N/2, y=N/2, dir=0;
		
		int num;
		FILE>>num;
		string S;
		int T;
		for (int i=0; i<num; i++) {
			FILE>>S>>T;
			while (T>0) {
				for (int k=0; k<S.size(); k++) {
					if (S[k]=='F') {
						x+=dire[dir][0];
						y+=dire[dir][1];
//						cout<<x-N/2<<" "<<y-N/2<<"\n";
						if (dir==0) mX[x][y]=true;
						else if (dir==1) mY[x][y-1]=true;
						else if (dir==2) mX[x+1][y]=true;
						else if (dir==3) mY[x][y]=true;
						a[x][y]=1;
						}
					else if (S[k]=='L') {dir++; dir%=4;}
					else if (S[k]=='R') {dir+=3; dir%=4;}
					}
				T--;
				}
			}

/*		for (int i=30; i<150; i++) {
			for (int j=60; j<130; j++) cout<<mX[i][j];
			cout<<"\n";
			}
		for (int i=30; i<150; i++) {
			for (int j=60; j<130; j++) cout<<mY[i][j];
			cout<<"\n";
			}
*/

//		system("PAUSE");
		
		for (int i=2; i<N-2; i++) {
			int minX, maxX;
			bool minXX=true;
			bool maxXX=true;
			bool par;
			for (int j=0; j<N && minXX; j++) if (mX[i][j]) {minX=j; minXX=false;}
			for (int j=N-1; j>=0 && maxXX; j--) if (mX[i][j]) {maxX=j; maxXX=false;}
			if (minXX==false) if (minX!=maxX) {
				par=false;
				for (int j=minX; j<maxX; j++) {
					if (mX[i][j]) par=!par;
					
					if (par) b[i][j]=2;
					else b[i][j]=3;
					}
				}
			}
/*		for (int i=30; i<150; i++) {
			for (int j=60; j<130; j++) cout<<b[i][j];
			cout<<"\n";
			}
*/	//	system("PAUSE");	
		for (int i=2; i<N-2; i++) {
			int minX, maxX;
			bool minXX=true;
			bool maxXX=true;
			bool par;
			for (int j=0; j<N && minXX; j++) if (mY[j][i]) {minX=j; minXX=false;}
			for (int j=N-1; j>=0 && maxXX; j--) if (mY[j][i]) {maxX=j; maxXX=false;}
			if (minXX==false) if (minX!=maxX) {
				par=false;
				for (int j=minX; j<maxX; j++) {
					if (mY[j][i]) par=!par;
					
					if (par) b[j+1][i]=2;
					else b[j+1][i]=3;
					}
				}
			}
		
/*		for (int i=30; i<150; i++) {
			for (int j=60; j<130; j++) cout<<a[i][j];
			cout<<"\n";
			}
		cout<<"\n";
		for (int i=30; i<150; i++) {
			for (int j=60; j<130; j++) cout<<b[i][j];
			cout<<"\n";
			}
*/		
		int res=0;
		for (int i=0; i<N; i++) for (int j=0; j<N; j++) if (b[i][j]==3) res++;
		
	//	system("PAUSE");
		
		
		OUT<<"Case #"<<z<<": "<<res<<"\n";
		}
	FILE.close();
	OUT.close();
	system("PAUSE");
	return 0;
	}
