#include <stdio.h>
#include <math.h>
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T, n;
	double x, y, z, vx, vy, vz;
	double tx,ty,tz, tvx,tvy,tvz;
	double a, b, c;
	double t1, t2, t;
	scanf("%d",&T);
	int tt;
	for(tt=1;tt<=T;tt++){
		scanf("%d",&n);
		int i;
		x = y = z = vx = vy = vz = 0;
		for(i=0;i<n;i++){
			scanf("%lf %lf %lf %lf %lf %lf",&tx,&ty,&tz,&tvx,&tvy,&tvz);
			x += tx; y += ty; z += tz;
			vx += tvx; vy += tvy; vz += tvz;
		}
		x /= n; y /= n; z /= n;
		vx /= n; vy /= n; vz /= n;
		a = vx * vx + vy * vy + vz * vz;
		b = (vx * x + vy * y + vz * z)*2;
		c = x * x + y * y + z * z;
		if(a <= 1e-8){
			if(b <= 1e-8){
				t = 0;
			}
			else{
				t = c / b;
				if(t < 0) t = 0;
			}
		}
		else{
			if(b*b-4*a*c >= 0){
				t1 = (-b-sqrt(b*b-4*a*c))/(2*a);
				t2 = (-b+sqrt(b*b-4*a*c))/(2*a);
				if(t1>t2){
					double temp;
					temp = t1; t1=t2; t2=temp;
				}
				if(t1 >= 0){
					t = t1;
				}
				else if(t2 >= 0){
					t = t2;
				}
				else {
					t = 0;
				}
			}
			else{
				t = -b/(a*2);
				if(t < 0) t = 0;
			}
		}
		printf("Case #%d: %.8lf %.8lf\n",tt, sqrt( (x + vx*t)*(x + vx*t) + (y + vy*t)*(y + vy*t) + (z + vz*t)*(z + vz*t) ), t);
	}

	return 0;
}