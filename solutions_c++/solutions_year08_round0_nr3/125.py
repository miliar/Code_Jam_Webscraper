#include <iostream>
#include <iomanip>
#include <cmath>
#include <map>
#include <vector>
using namespace std;

typedef long double LD;

bool incir(LD x, LD y, LD rad){
	return ((x*x+y*y)<rad*rad);
}

LD seg(LD R, LD _h){

	LD z=R-_h;

	LD x= sqrt(R*R-z*z);
	LD alfa=atan(x/z);
	LD ci=alfa/2.0*R*R;
	return ci-z*x/2;
}

LD f,R,t,r,g;

void retans(int test, LD ans){
	cout << "Case #" << test << ": " << ans << endl;
}

#define dbg(x) {/*cerr << "\t" #x " = " << x << endl;*/}

int main()
{
	cout << std::setprecision(7);
	int ttt;
	cin >> ttt;
	for(int cutest=1;cutest<=ttt;cutest++){
		cin >> f >> R >> t >> r >> g;
		
		if(R-t-f<0 || f*2.0>=g){
			retans(cutest,1);
			continue;
		}
		
		LD Inner=R-t-f;
		
		LD safe=0;
		for(LD bx=r;bx<R;bx+=g+r*2.0)
		for(LD by=r;by<R;by+=g+r*2.0){

			LD left=bx+f, right=bx+g-f;
			LD bottom=by+f, top=by+g-f;

			if( !incir(left,bottom,Inner) )
				break;
			
			if( incir(right,top,Inner)  ){
				safe+=(right-left)*(top-bottom);
				//cerr << " full hit x=" << bx << " y=" << by << " we add " << (right-left)*(top-bottom) << endl;
				continue;
			}
			
			bool topleft=incir(left,top,Inner);
			bool botright=incir(right,bottom,Inner);
			
			LD ar=M_PI/4.0*Inner*Inner;
			LD fulAR=ar;
			ar-=left*bottom;
			if(topleft){
				ar-=seg(Inner,Inner-top);
				ar-=left*(top-bottom);
			}else{
				ar-=fulAR-seg(Inner,Inner-left);
				ar+=left*bottom;
			}
			
			if(botright){
				ar-=seg(Inner, Inner-right);
				ar-=bottom*(right-left);
			}else{
				ar-=fulAR-seg(Inner,Inner-bottom);
				ar+=left*bottom;
			}
			cerr << " for x=" << bx << " y=" << by << "we add " << ar << endl;
			dbg(left);
			dbg(right);
			dbg(bottom);
			dbg(top);
			dbg(Inner);
			dbg(topleft);
			dbg(botright);
			safe+=ar;
		}

		LD area=R*R*M_PI;

		cerr << " safe= " << safe << endl;
		cerr << " area= " << area << endl;
		
		retans(cutest,1.0-safe*4/area);
	}//endtest
	return 0;
}
