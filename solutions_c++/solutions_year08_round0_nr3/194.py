#include <cstdio>
#include <cmath>

inline bool check(double r,double x,double y)
{
	if(x*x + y*y < r*r) return true;
	return false;
}

int main()
{
	int N;
	double f,R,t,r,g,x,area;
	scanf("%d\n",&N);
	for(int nn = 1;nn<=N;++nn) {
		scanf("%lf %lf %lf %lf %lf\n",&f,&R,&t,&r,&g);
		area = 0;
		if(2*f < g) {
			// going over all the squares in the quarter
			x = r;
			while(x < R - t) {
				double y = r;
				while(y < R - t) {
					if(check(R-t-f,x+f,y+f)) {
						if(check(R-t-f,x+f,y+g-f) && check(R-t-f,x+g-f,y+g-f) && check(R-t-f,x+g-f,y+f)) 
							area += (g-2*f)*(g-2*f);
						else if(check(R-t-f,x+f,y+g-f) && check(R-t-f,x+g-f,y+f)) {
							double xx = sqrt((R-f-t)*(R-f-t)-(y+g-f)*(y+g-f));
							double theta1 = asin(xx /(R-f-t));
							double theta2 = asin((x+g-f)/(R-f-t));
							area += ((R-f-t)*(R-f-t)/2)*(0.5*sin(2*theta2) + theta2 - 0.5*sin(2*theta1) - theta1);
							area -= (y+f)*(x+g-f-xx);
							area += (g-2*f)*(xx - (x + f));
						}
						else if(check(R-t-f,x+f,y+g-f)) {
							double x1 = sqrt((R-f-t)*(R-f-t)-(y+g-f)*(y+g-f));
							double x2 = sqrt((R-f-t)*(R-f-t)-(y+f)*(y+f));
							double theta1 = asin(x1 /(R-f-t));
							double theta2 = asin((x2)/(R-f-t));
							area += ((R-f-t)*(R-f-t)/2)*(0.5*sin(2*theta2) + theta2 - 0.5*sin(2*theta1) - theta1);
							area -= (y+f)*(x2-x1);
							area += (g-2*f)*(x1 - (x + f));
						}
						else if(check(R-t-f,x+g-f,y+f)) {
							double theta1 = asin((x+f) /(R-f-t));
							double theta2 = asin((x+g-f)/(R-f-t));
							area += ((R-f-t)*(R-f-t)/2)*(0.5*sin(2*theta2) + theta2 - 0.5*sin(2*theta1) - theta1);
							area -= (g-2*f)*(y+f);
						}
						else {
							double xx = sqrt((R-f-t)*(R-f-t)-(y+f)*(y+f));
							double theta2 = asin(xx /(R-f-t));
							double theta1 = asin((x+f)/(R-f-t));
							area += ((R-f-t)*(R-f-t)/2)*(0.5*sin(2*theta2) + theta2 - 0.5*sin(2*theta1) - theta1);
							area -= (y+f)*(xx-(x + f));
						}
					}
					else break;
					y += g + 2*r;
				}
				x += g + 2 * r;
			}
		}
		printf("Case #%d: %lf\n",nn,1 - (area * 4)/(M_PI*R*R));
	}
	return 0;
}
