#include <stdio.h>
#include <conio.h>
#include <iostream>
#include <math.h>
using namespace std;

struct xyz{
	double x,y,z;
	void zero(){ x=0; y=0; z=0; }
};
#define sqr(a) ((a)*(a))
int main(){	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w+",stdout);
	double dmin,tmin;
	xyz st;
	int T,TT;
	cin >> T;
	xyz srxt,srvk;
	for(int i=1;i<=T;i++){
		srxt.zero();
		srvk.zero();
		cin >> TT;
		for(int j=0;j<TT;j++)
		{
			cin >> st.x;
			cin >> st.y;
			cin >> st.z;
			srxt.x+=st.x/TT;
			srxt.y+=st.y/TT;
			srxt.z+=st.z/TT;
			cin >> st.x;
			cin >> st.y;
			cin >> st.z;
			srvk.x+=st.x/TT;
			srvk.y+=st.y/TT;
			srvk.z+=st.z/TT;
		}/*
		srxt.x/=TT;
		srxt.y/=TT;
		srxt.z/=TT;
		srvk.x/=TT;
		srvk.y/=TT;
		srvk.z/=TT;*/
		//math
		double alfa;
		if(srvk.x*srvk.x<1e-12 && srvk.y*srvk.y<1e-12 && srvk.z*srvk.z<1e-12){
			tmin=0;
			dmin=sqrt(srxt.x*srxt.x+srxt.y*srxt.y+srxt.z*srxt.z);
			printf("Case #%d: %.8lf %.8lf\n",i,dmin,tmin);
			continue;
		}
		else alfa=-(srvk.x*srxt.x+srvk.y*srxt.y+srvk.z*srxt.z)/(srvk.x*srvk.x+srvk.y*srvk.y+srvk.z*srvk.z);
		xyz prM;
		prM.x=srxt.x+alfa*srvk.x;
		prM.y=srxt.y+alfa*srvk.y;
		prM.z=srxt.z+alfa*srvk.z;
		dmin=sqrt(prM.x*prM.x+prM.y*prM.y+prM.z*prM.z);

		tmin=sqrt(sqr(srxt.x-prM.x)+sqr(srxt.y-prM.y)+sqr(srxt.z-prM.z))/sqrt(sqr(srvk.x)+sqr(srvk.y)+sqr(srvk.z));
	//	if(srvk.x>1e-10) tmin=(prM.x-srxt.x)/srvk.x;
		//if(srvk.x<1e-10 && srvk.y>1e-10) tmin=(prM.y-srxt.y)/srvk.y;
		//if(srvk.x<1e-10 && srvk.y<1e-10 && srvk.z>1e-10) tmin=(prM.z-srxt.z)/srvk.z;
		if(alfa<0){
			tmin=0;
			dmin=sqrt(srxt.x*srxt.x+srxt.y*srxt.y+srxt.z*srxt.z);
		}
		printf("Case #%d: %.8lf %.8lf\n",i,dmin,tmin);
	}

	return 0;
}