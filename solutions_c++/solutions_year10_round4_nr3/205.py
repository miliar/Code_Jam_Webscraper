#include <iostream>
#include <string>
#include <vector>
using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fd(i,m,n) for(int i=n-1; i>=m; i--)

int cells[2][200][200];

int main(void) {
	int C;
	cin >> C;
	fu(tc,1,C+1) {
		int R;
		cin >> R;
		memset(cells,0,sizeof(cells));
		int X=0,Y=0;
		fu(r,0,R) {
			int x1,y1,x2,y2;
			cin >> x1 >> y1 >> x2 >> y2;
			fu(x,x1,x2+1) fu(y,y1,y2+1) {
				cells[0][x][y]=1;
			}
			X=max(X,x2+1);
			Y=max(Y,y2+1);
		}
		int w=0;
		int t=0;
		for(;;) {
			/*fu(x,0,X) {
				fu(y,0,Y) cout << cells[w][x][y];
				cout << endl;
			}*/
			//cout << endl;
			bool done=true;
			fu(x,0,X) fu(y,0,Y) if(x==0 || y==0) cells[1-w][x][y]=0; else {
				int s = cells[w][x-1][y]+cells[w][x][y-1];
				cells[1-w][x][y] = (s==2 || (s==1 && cells[w][x][y]));
				if(cells[1-w][x][y]) done=false;
			}
			w=1-w;
			t++;
			if(done) break;
		}
		cout << "Case #" << tc << ": " << t << endl;
	}
}
