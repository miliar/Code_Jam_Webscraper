#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>

using namespace std;

int main() {
	int T;

	cin >> T;

	for (int t=1;t<=T;t++) {
		int W, L, U, G;
		cin >> W >> L >> U >> G;
		vector<int> lx, ly, ux, uy;
		int x,y;
		for (int n=0;n<L;n++) {
			cin >> x >> y;
			lx.push_back(x);
			ly.push_back(y);
		}
		for (int n=0;n<U;n++) {
			cin >> x >> y;
			ux.push_back(x);
			uy.push_back(y);
		}
		double area=0;
		for (int n=1;n<L;n++) {
			area-=double(lx[n]-lx[n-1])*double(ly[n]+ly[n-1])/double(2);
		}
		for (int n=1;n<U;n++) {
			area+=double(ux[n]-ux[n-1])*double(uy[n]+uy[n-1])/double(2);
		}
		area=area/G;

		cout << "Case #" << t << ": " << endl;

		double cursor=0;

		int Li=1, Ui=1;
		double Lg=double(ly[1]-ly[0])/double(lx[1]-lx[0]);
		double Ug=double(uy[1]-uy[0])/double(ux[1]-ux[0]);
		double height=uy[0]-ly[0];
		int g=1;
		double arealeft=area;
		
		while (g<G) {
			//clog << arealeft << endl;
			// distance to get area
			double det=height*height+2*(Ug-Lg)*arealeft;
			double w;
			if ((Ug-Lg)==0) {
				if (height==0) w=2000;
				else w=arealeft/height;
			}
			else if (det<0) {
				w=2000;
			}
			else {
				w=((-height)+sqrt(det))/(Ug-Lg);
			}
			//clog << "w: " << w << endl;
			double newpos=cursor+w;
			if (newpos>lx[Li] || newpos>ux[Ui]) {
				double pos=min(lx[Li],ux[Ui]);
				w=pos-cursor;
				//clog << w << " " << height << " " << g << " " << w*double(height+height+w*(Ug-Lg))/2 << endl;
				arealeft-=w*double(height+height+w*(Ug-Lg))/2;
				height=height+w*(Ug-Lg);
				if (pos==lx[Li]) {
					Li++;
					Lg=double(ly[Li]-ly[Li-1])/double(lx[Li]-lx[Li-1]);
				}
				if (pos==ux[Ui]) {
					Ui++;
					Ug=double(uy[Ui]-uy[Ui-1])/double(ux[Ui]-ux[Ui-1]);
				}
				cursor=pos;
			}
			else {
				// draw slice at w
				//cout << cursor+w << endl;
				printf("%.6lf\n",cursor+w);
				cursor+=w;
				height=height+w*(Ug-Lg);

				arealeft=area;
				g++;
			}
		}


		//printf("%lf",time);
		
		//cout << endl;
	}
	return 0;
}