/*
Nguyen Tran Nam Khanh
microsoft
*/
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cmath>
#include <cstdio>

using namespace std;

#define Clear(t) memset((t),0,sizeof(t))
#define For(i,a,b) for (int i=(int)(a),_t = (int)(b);i<=_t;i++)
#define Ford(i,a,b) for (int i=(int)(a), _t = (int)(b);i>=_t;i--)
#define Rep(i,n) for (int i=0, _t = (int)(n);i<_t;i++)
#define tr(it, c) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define SZ(t) ((int)((t).size()))
#define All(v) (v).begin(),(v).end()
#define Sort(v) sort(All(v))
#define pb push_back
#define PI 3.141592653589

typedef vector<int> VI;
typedef long long ll;
typedef vector<ll> VL;
typedef vector<string> VS;

string i2s(int x) { ostringstream o; o<<x; return o.str(); }
int s2i(string s) { int x; istringstream i(s); i>>x; return x; }

double ri,ro,r,g,f,t;

double kc(double x, double y, double xx, double yy) {
	double dx = x-xx, dy = y-yy;
	return sqrt(dx*dx+dy*dy);
}

double dtcung(double len) {
	double c = (ri*ri*2-len*len)/(2*ri*ri);
	double goc = acos(c);
	//cout<<c<<' '<<goc<<endl;
	
	double dttron = ri*ri;
	double cung = dttron*goc/2;
	double tamgiac = 0.5*ri*ri*sin(goc);
	//cout<<cung-tamgiac<<endl;
	return cung-tamgiac;
}

bool inside(double x, double y) {
	return x*x + y*y <=ri*ri;
}

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	int st;
	cin>>st;
	For(ts,1,st) {
		cin>>f>>ro>>t>>r>>g;
		ri = ro-t-f;
		g-=2*f;
		if (g<=0) {
			printf("Case #%d: 1.000000\n",ts);
			continue;
		}
		
		double x = r+f, y = r+f;
		double ret = 0;
		
		while (y<ri) {
			x = r+f;
			while (inside(x,y)) {
				//cout<<x<<' '<<y<<' '<<ret<<endl;
				if (inside(x+g,y+g)) {
					ret+=g*g;
					//cout<<"--"<<x<<' '<<2*r<<' '<<g<<' '<<2*f<<' '<<x+2*r+g+2*f<<endl;
					//cout<<1000+0.00001-1000<<endl;
					x+=2*r+g+2*f;
					//cout<<"--"<<x<<endl;
					//printf("%.6f\n",x);
					continue;
				}
				if (inside(x+g,y) && inside(x,y+g)) {
					double xx = sqrt(ri*ri-(y+g)*(y+g));
					double yy = sqrt(ri*ri-(x+g)*(x+g));
					
					double tmp1 = g*(xx-x);
					double tmp2 = (g+yy-y)*(x+g-xx)/2;
					double len = kc(xx,y+g,x+g,yy);
					double tmp3 = dtcung(len);
					ret+=tmp1+tmp2+tmp3;
					x+=2*r+g+2*f;
					continue;
				}
				
				if (inside(x+g,y)) {
					double yy1 = sqrt(ri*ri-(x+g)*(x+g));
					double yy2 = sqrt(ri*ri-x*x);
					
					double tmp1 = (yy2-y+yy1-y)*g/2;
					double len = kc(x,yy2,x+g,yy1);
					double tmp2 = dtcung(len);
					ret+=tmp1+tmp2;
					x+=2*r+g+2*f;
					continue;
				}

				if (inside(x,y+g)) {
					double xx1 = sqrt(ri*ri-(y+g)*(y+g));
					double xx2 = sqrt(ri*ri-y*y);

					double tmp1 = (xx2-x+xx1-x)*g/2;
					double len = kc(xx2,y,xx1,y+g);
					double tmp2 = dtcung(len);
					ret+=tmp1+tmp2;
					x+=2*r+g+2*f;
					continue;
				}
				
				double xx = sqrt(ri*ri-y*y);
				double yy = sqrt(ri*ri-x*x);
				double tmp1 = (xx-x)*(yy-y)/2;
				double len = kc(x,yy,xx,y);
				double tmp2 = dtcung(len);
				//cout<<xx-x<<' '<<yy-y<<' '<<tmp1<<' '<<tmp2<<' '<<len<<endl;
				ret+=tmp1+tmp2;
				x+=2*r+g+2*f;
			}
			//cout<<'-'<<x<<' '<<y<<' '<<inside(x,y)<<endl;
			y+=2*r+g+2*f;
		}

		double dt = ro*ro*PI;
		//cout<<ret<<' '<<dt<<endl;
		ret*=4;
		ret = dt-ret;
		//cout<<dt<<' '<<ret<<endl;
		double res = ret/dt;
		printf("Case #%d: %.6f\n",ts,res);
	}

	return 0;
}
