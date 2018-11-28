#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
using namespace std;

#define NA_ZEWN(x,y) (((x)*(x)+(y)*(y)) > (Ri*Ri))
#define PRZEC(x) (sqrt((Ri*Ri) - (x)*(x)))

class PKT {
public:
	double x,y;
	PKT() {}
	PKT(double _x,double _y): x(_x), y(_y) {}
	static double cross(const PKT &a, const PKT &b) {
		return a.x*b.y - a.y*b.x;
	}
	PKT operator-(const PKT &o) const {
		return PKT(x-o.x,y-o.y);
	}
};

static double oblicz() {
	double R, t, r, g;
	{
		double f;
		scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
		/* uprość by można f wywalić */
		g -= 2*f; r += f; /* trafienie w odległości f */
		t += f;
	}
	/* jak nie da się spudłować.. */
	if(t>=R || g<=0)
		return 1.0;

	double Ri = R-t;
	double Ppud = 0;
	double Pcalk = M_PI*R*R/4.0;
	double gkwa = g*g;
	double pdelta = r+g+r;

	for(double x=r;x<Ri;x+=pdelta)
	for(double y=r;y<Ri;y+=pdelta) {
		if((x*x+y*y) >= (Ri*Ri))
			break;
		double dx=x+g,dy=y+g;
		if((dx*dx+dy*dy) <= (Ri*Ri)) {
			Ppud += gkwa;
			continue;
		}
		/* dupa - wyliczenie przecięcia konieczne */
		vector<PKT> pL, pR;

		pL.push_back(PKT(x,y));
		if(NA_ZEWN(x,dy)) { // (x,y) - (x,dy)
			pL.push_back(PKT(x,PRZEC(x)));
		} else {
			pL.push_back(PKT(x,dy));
			if(NA_ZEWN(dx,dy)) { // (x,dy) - (dx,dy)
				pL.push_back(PKT(PRZEC(dy),dy));
			} else {
				pL.push_back(PKT(dx,dy));
			}
		}

		pR.push_back(PKT(x,y));
		if(NA_ZEWN(dx,y)) { // (x,y) - (dx,y)
			pR.push_back(PKT(PRZEC(y),y));
		} else {
			pR.push_back(PKT(dx,y));
			if(NA_ZEWN(dx,dy)) { // (dx,y) - (dx,dy)
				pR.push_back(PKT(dx,PRZEC(dx)));
			} else {
				pR.push_back(PKT(dx,dy));
			}
		}

		PKT k1 = pL[(int)pL.size()-1];
		PKT k2 = pR[(int)pR.size()-1];
		double kat = abs(atan2(k1.y,k1.x)-atan2(k2.y,k2.x));
		kat = std::min(kat, 2*M_PI - kat);
		double poleWyc = kat*Ri*Ri/2.0 - abs(PKT::cross(k1,k2))/2.0;
		if(poleWyc<0) {
			//abort();
			//printf("pWyc=%le\n",poleWyc);
			poleWyc = 0;
		}
		Ppud += poleWyc;

		for(int i=(int)pR.size()-1;i>=0;i--)
			pL.push_back(pR[i]);

		PKT c = pL[0];
		double suma = 0;
		for(int i=1;i+1<(int)pL.size();i++) {
			suma += PKT::cross(pL[i]-c,pL[i+1]-c);
		}
		Ppud += abs(suma)/2.0;
	}

	return 1.0-(Ppud/Pcalk);
}

int main() {
	int _N; scanf("%d",&_N);
	for(int _nc=1;_nc<=_N;_nc++) {
		printf("Case #%d: %lf\n", _nc, oblicz());
	}
	return 0;
}

