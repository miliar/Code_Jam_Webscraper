#include<cassert>
#include<algorithm>
#include<cstring>
#include<cctype>
#include<cmath>
#include<functional>
#include<cerrno>
#include<iomanip>
#include<iostream>
#include<map>
#include<numeric>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<utility>
#include<vector>
//#include<gmpxx.h>
using namespace std;
#define sz(x) ((int)(x.size()))
#define mp make_pair
#define pb push_back
#define fr(k,y,z) for(int k=(y);k<=(z);k++)
#define fo(k,z) for(int k = 0;k<(z);k++)
#define foa(k,x) fo(k,sz(x))
#define all(x) (x).begin(),(x).end()
#define iall(I,x) for(typeof((x).begin()) I = (x).begin(); I != (x).end();++I)

typedef long double num;

struct Fly{
	num f,R,t,r,g;
	num rp,rp2;

	num Eval(num x){
		assert(rp > x);
		num sq = sqrtl(rp2 - x*x);
		return .5 * (atanl(x / sq) * rp2 + x * sq);
	}

	num Eval(num sx,num ex,num sy){
		return Eval(ex) - Eval(sx) - sy * (ex - sx);
	}

	bool PointIn(num x,num y){
		return x*x + y*y <= rp2;
	}

	void Go(){
		num n = ceil((R - r - t) / (g + 2*r))+2;
		num res = .0;

		rp = (R - t - f);
		rp2 = rp*rp;
		assert(rp >= .0);

		for(int k = 0;(double)k <= n;++k)
			for(int j = 0;(double)j <= n;++j){

				num sx = r + k*(g + 2*r);
				num sy = r + j*(g + 2*r);
				num ex = sx + g;
				num ey = sy + g;
				sx += f; sy += f;
				ex -= f; ey -= f;
 				if(ex <= sx || ey <= sy) continue;

				if(!PointIn(sx,sy)) continue;

				num tmp=.0;
				if(PointIn(ex,ey)){
					tmp += (ex-sx) * (ey-sy);
				}else{
					bool a = PointIn(ex,sy);
					bool b = PointIn(sx,ey);
					if(a && b){
						assert(rp > ey);
						num hx = sqrtl(rp2-ey*ey);
						tmp += (hx - sx) * (ey - sy);
						tmp += Eval(hx,ex,sy);
					}else if(!a && !b){
						assert(rp > sy);
						num hx = sqrtl(rp2-sy*sy);
						tmp += Eval(sx,hx,sy);
					}else if(!a){
						assert(rp > ey);
						num hx1 = sqrtl(rp2-ey*ey);
						assert(rp > sy);
						num hx2 = sqrtl(rp2-sy*sy);
						tmp += (hx1-sx) * (ey - sy);
						tmp += Eval(hx1,hx2,sy);
					}else if(!b){
						assert(rp > ex);
						num hy1 = sqrtl(rp2-ex*ex);
						assert(rp > sx);
						num hy2 = sqrtl(rp2-sx*sx);
						tmp += (hy1-sy) * (ex - sx);
						tmp += Eval(hy1,hy2,sx);
					}
				}
				res += tmp;
			}

		num area = M_PI * R*R / 4;
		res /= area;
		cout << 1. - res;
	}
};

int main()
{
	string line;
	getline(cin,line);
	int ca=0;
	while(++ca,getline(cin,line)){
		istringstream iss(line);
		Fly f;
		iss >> f.f >> f.R >> f.t >> f.r >> f.g;
		cout << "Case #" << ca << ": ";
		f.Go();
		cout << endl;
	}
}
