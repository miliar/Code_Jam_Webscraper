#include <iostream>
#include <string>
#include <vector>
using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fd(i,m,n) for(int i=n-2; i>=m; i--)
#define fu2(i,m,n) for(int i=m; i<n; i+=2)
#define fd2(i,m,n) for(int i=n-2; i>=m; i-=2)

int diamond[500][500];

int main(void) {
	int T;
	cin >> T;
	fu(tc,1,T+1) {
		int k;
		cin >> k;
		memset(diamond,0,sizeof(diamond));
		fu(i,0,k) fu(j,0,i+1) {
			cin >> diamond[i][k-i-1+2*j];
			diamond[i][k-i-1+2*j]++;
		}
		fu(i,1,k) fu(j,0,k-i) {
			cin >> diamond[k+i-1][i+2*j];
			diamond[k+i-1][i+2*j]++;
		}
		/*fu(i,0,2*k-1) {
			fu(j,0,2*k-1) cout << diamond[i][j] << " ";
			cout << endl;
		}*/

		int bestn = 1000000;
		fu2(m,2*k-2,4*k-3) {
			bool good=true;
			for(int i=0; good && i<2*k-1; i++)
			for(int j=m-(2*k-2); j<2*k-1; j++)
				if(diamond[j][i] != diamond[m-j][i] && (diamond[j][i]&&diamond[m-j][i])) {
					good=false;
					break;
				}
			if(good) {
				bestn=m-(2*k-2);
				break;
			}
		}
		//cout << bestn << endl;
		fd2(m,(2*k-2)-bestn,2*k-2) {
			bool good=true;
			for(int i=0; good && i<2*k-1; i++)
			for(int j=0; j<=m; j++)
				if(diamond[j][i] != diamond[m-j][i] && (diamond[j][i] && diamond[m-j][i])) {
					good=false;
					break;
				}
			if(good) {
				bestn=(2*k-2)-m;
				break;
			}
		}
		//cout << bestn << endl;


		int bestm = 1000000;
		fu2(m,2*k-2,4*k-3) {
			bool good=true;
			for(int i=0; good && i<2*k-1; i++)
			for(int j=m-(2*k-2); j<2*k-1; j++)
				if(diamond[i][j] != diamond[i][m-j] && (diamond[i][j]&&diamond[i][m-j])) {
					good=false;
					break;
				}
			if(good) {
				bestm=m-(2*k-2);
				break;
			}
		}
		//cout << bestm << endl;
		fd2(m,(2*k-2)-bestm,2*k-2) {
			bool good=true;
			for(int i=0; good && i<2*k-1; i++)
			for(int j=0; j<=m; j++)
				if(diamond[i][j] != diamond[i][m-j] && (diamond[i][j]&&diamond[i][m-j])) {
					good=false;
					break;
				}
			if(good) {
				bestm=(2*k-2)-m;
				break;
			}
		}
		//cout << bestm << endl;

		int k2 = k+(bestm+bestn)/2;
		cout << "Case #" << tc << ": " << k2*k2-k*k << endl;

	}
}
