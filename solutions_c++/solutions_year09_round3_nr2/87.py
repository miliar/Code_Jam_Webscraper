#include<iostream>
#include<cmath>
using namespace std;

#define X *(long long)
#define F /(long double)n

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		long x=0,y=0,z=0,vx=0,vy=0,vz=0,n;
		cin>>n;
		for(int j=0;j<n;j++){
			int tx,ty,tz,tvx,tvy,tvz;
			cin>>tx>>ty>>tz>>tvx>>tvy>>tvz;
			x+=tx;y+=ty;z+=tz;vx+=tvx;vy+=tvy;vz+=tvz;
		}
		cout.setf(ios_base::fixed);
		cout.precision(8);
		cout<<"Case #"<<i<<": ";
		long double dist2=x X x+y X y+z X z;
		long double vdist2=vx X vx+vy X vy+vz X vz;
		if(x X vx+y X vy+z X vz>=0)
			cout<<sqrt(dist2/n/n)<<" "<<0.0<<endl;
		else{
			long double area2=pow((x X vy-y X vx)F,2)+pow((y X vz-z X vy)F,2)+pow((z X vx-x X vz)F,2);
			long double dmin2=area2/vdist2;
			long double tmin2=dist2-dmin2*n*n;
			cout<<sqrt(dmin2)<<" "<<sqrt(tmin2/vdist2)<<endl;
		//	cerr<<area2<<" "<<dist2<<" "<<dmin2<<" "<<tmin2<<" "<<vdist2<<endl;
		}
		//cerr<<x<<" "<<y<<" "<<z<<" "<<vx<<" "<<vy<<" "<<vz<<endl;
	}
	return 0;
}