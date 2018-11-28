#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <map>

#define y0 y63475625
#define y1 y28435
#define sqr(x) ((x)*(x))

using namespace std;

typedef long long ll;
typedef long double ld;

const double pi = acos(-1.0);

int a[500][500];
int xo=250,yo=250;

int main()
{
	int T;
	cin >> T;
	
	for (int I=0;I<T;I++){
		memset(a,255,sizeof(a));
		int k;
		cin >> k;
		//cerr << k << endl;
		int lx=xo-k+1,rx=xo+k-1,ly=yo-k+1,ry=yo+k-1;
		for (int i=0;i<k;i++){
			for (int j=0;j<=i;j++){
				int x;
				cin >> x;
				a[xo-k+1+i][yo-i+2*j]=x;
			}
		}
		for (int i=1;i<k;i++){
			for (int j=0;j<k-i;j++){
				int x;
				cin >> x;
				a[xo+i][yo-k+1+i+2*j]=x;
			}
		}
		/*for (int i=lx;i<=rx;i++){
			for (int j=ly;j<=ry;j++)if (a[i][j]>=0)cerr << a[i][j]; else cerr << " ";
			cerr << endl;
		}*/
		int sx=-1;
		int sy=-1;
		for (int i=lx;i<=rx;i++){
			bool kpyto=true;
			for (int x=lx;x<=rx;x++){
				for (int y=ly;y<=ry;y++){
					if (a[x][y]>=0&&a[i+(i-x)][y]>=0&&a[x][y]!=a[i+(i-x)][y]){
						kpyto=false;
						break;
					}
				}
			}
			if (kpyto&&abs(sx-xo)>abs(i-xo))sx=i;
		}
		for (int i=ly;i<=ry;i++){
			bool kpyto=true;
			for (int x=lx;x<=rx;x++){
				for (int y=ly;y<=ry;y++){
					if (a[x][y]>=0 && a[x][i+(i-y)]>=0 &&a[x][y]!=a[x][i+(i-y)]){
						kpyto=false;
						break;
					}
				}
			}
			if (kpyto&&abs(sy-yo)>abs(i-yo))sy=i;
		}
		sx=abs(sx-xo);sy=abs(sy-yo);
		//cerr << sx << ' ' << sy << endl;
		cout << "Case #" << I+1 << ": " << sqr(k+sx+sy)-sqr(k) << endl;
	}
	return 0;
}
