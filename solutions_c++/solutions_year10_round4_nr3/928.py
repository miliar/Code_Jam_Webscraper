#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

bool rec[105][105],rec2[105][105];

int main() {
	int T,R,x1,y1,x2,y2,ct,t,xm,ym;
	cin >> T;
	for(int cs=1;cs<=T;cs++) {
		xm=0;ym=0;
		ct=0;
		for(int i=1;i<=100;i++) {
			for(int j=1;j<=100;j++) {
				rec[i][j] = false;
			}
		}
		cin >> R;
		for(int i=1;i<=R;i++) {
			cin >> x1 >> y1 >> x2 >> y2;
			xm = max(xm,x2); ym = max(ym,y2);
			for(int x=x1;x<=x2;x++) {
				for(int y=y1;y<=y2;y++) {
					if(rec[x][y]==false)
						ct++;
					rec[x][y]=true;
				}
			}
		}
		t=0;
		while(ct>0) {
			t++;
			for(int x=1;x<=xm;x++) {
				for(int y=1;y<=ym;y++) {
					if(rec[x][y]==false && rec[x-1][y]==true && rec[x][y-1]==true) {
						ct++;
						rec2[x][y]=true;
						continue;
					}
					if(rec[x][y]==true) {
						if (rec[x-1][y]==true || rec[x][y-1]==true) {
							rec2[x][y]=true;
							continue;
						}
						ct--;
					}
					rec2[x][y]=false;
				}
			}
			for(int y=ym;y>=1;y--) {
					for(int x=1;x<=xm;x++) {
					rec[x][y] = rec2[x][y];
				}
			}
		}	
			
		
		
		cout << "Case #" << cs << ": " << t << '\n';
	}
	return 0;
}
