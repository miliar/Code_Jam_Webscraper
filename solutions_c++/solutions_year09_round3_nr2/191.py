#include<iostream>
#include<string>
#include<cmath>
using namespace std;

long double	ax,ay,az,bx,by,bz;
long double	x,y,z,vx,vy,vz,a,b,c;

double	d,t;

int		main(){
		int tt, T, i, n;
	//	freopen("in.txt","r",stdin);
	//	freopen("out.txt","w",stdout);
		for(cin>>T, tt=1; tt<=T; tt++){
			printf("Case #%d: ",tt);
			cin>>n;
			ax = ay = az = 0.0;
			bx = by = bz = 0.0;
			for(i=0; i<n; i++){
				cin>>x>>y>>z>>vx>>vy>>vz;
				ax += vx; ay += vy; az += vz; 
				bx += x, by += y; bz += z;
			}
			ax /= n; ay /= n; az /= n; 
			bx /= n; by /= n; bz /= n;
			a = (ax*ax + ay*ay + az*az);
			b = (ax*bx + ay*by + az*bz)*2.0; 
			c = (bx*bx + by*by + bz*bz);
			
			if (fabs(a)<1e-10) t = 0.0;
			else {
				t = -b *0.5 / a;
			}
			if (t<0.0) t = 0.0;
			long double ts = a*t*t + b*t + c;
			if (ts<0.00) d = 0; else 
			d = sqrt(ts);

			printf("%0.8lf %0.8lf\n", d + 1e-9, t+1e-9);
		}
		return 0;
}