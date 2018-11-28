#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include<math.h>
#include<memory.h>

double const PI = acos(-1.0);
double const eps = 1e-12;

struct point_t {
	double x,y;
};

double dist(point_t a, point_t b) {
	return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}

double getarea(int i, int j, double r, double g, double R) {
	point_t O={0,0};
	point_t ld={r+i*(g+r+r),r+j*(g+r+r)};
	point_t lu={ld.x,ld.y+g};
	point_t rd={ld.x+g,ld.y};
	point_t ru={ld.x+g,ld.y+g};
	if ( dist(O,ld) >= R - eps ) {
		return 0.0;
	}
	if ( dist(O,ru) <= R + eps ) {
		return g*g;
	}
	if ( dist(O,lu) <= R + eps && dist(O,rd) <= R + eps ) {
		point_t uu={sqrt(R*R-lu.y*lu.y),lu.y};
		point_t rr={rd.x,sqrt(R*R-rd.x*rd.x)};
		double area = 0.0;
		double theta = acos((2*R*R-dist(uu,rr)*dist(uu,rr))/(2*R*R));
		area += g*(uu.x-lu.x);
		area += (g+(rr.y-rd.y))*(rd.x-uu.x)*0.5;
		area += 0.5 * R * R * (theta - sin(theta));
		return area;
	}
	if ( dist(O,lu) <= R + eps) {
		point_t uu={sqrt(R*R-lu.y*lu.y),lu.y};
		point_t dd={sqrt(R*R-ld.y*ld.y),ld.y};
		double area = 0.0;
		double theta = acos((2*R*R-dist(uu,dd)*dist(uu,dd))/(2*R*R));
		area += ((uu.x-lu.x)+(dd.x-ld.x))*g*0.5;
		area += 0.5 * R * R * (theta - sin(theta));
		return area;
	}
	if ( dist(O,rd) <= R + eps) {
		point_t ll={ld.x,sqrt(R*R-ld.x*ld.x)};
		point_t rr={rd.x,sqrt(R*R-rd.x*rd.x)};
		double area = 0.0;
		double theta = acos((2*R*R-dist(ll,rr)*dist(ll,rr))/(2*R*R));
		//double cos_theta = (2*R*R-dist(ll,rr))/(2*R*R);
		area += ((ll.y-ld.y)+(rr.y-rd.y))*g*0.5;
		area += 0.5 * R * R * (theta - sin(theta));
		//area += 0.5 * R * R * (theta - (1 - cos_theta*cos_theta) );
		return area;
	}
	// dist(O,lu) >= R - eps && dist(O,rd) >= R - eps 
	{
		//printf("XX %d %d %.3lf %.3lf %.3lf\n", i,j,r,g,R);
		//printf("(%.3lf,%.3lf) (%.3lf,%.3lf)\n", lu.x,lu.y,ru.x,ru.y);
		//printf("(%.3lf,%.3lf) (%.3lf,%.3lf)\n", ld.x,ld.y,rd.x,rd.y);
		
		point_t ll={ld.x,sqrt(R*R-ld.x*ld.x)};
		point_t dd={sqrt(R*R-ld.y*ld.y),ld.y};
		//printf("(%.3lf,%.3lf) (%.3lf,%.3lf)\n", ll.x,ll.y,dd.x,dd.y);
		double area = 0.0;
		double theta = acos((2*R*R-dist(ll,dd)*dist(ll,dd))/(2*R*R));
		area += (ll.y-ld.y)*(dd.x-ld.x)*0.5;
		//area += 0.5 * R * R * (theta - sin(theta));
		area += 0.5 * R * R * (theta - sin(theta) );
		return area;
	}
	return 0.0;
}

int main(int argc, char* argv[]) {
	int N;
	double f, R, t, r, g;
	double sall,snull;
	scanf("%d", &N);
	for ( int nc = 1 ; nc <= N ; ++nc ) {
		scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
		sall = snull = 0;
		t += f;
		r += f;
		g -= 2*f;
		if ( t >= R-eps || r >= R-eps || g <= eps ) {
			printf("Case #%d: 1.000000\n", nc);
			continue;
		}
		//printf("CC");

		for ( int i = 0 ; ; ++i ) {
			int j;
			for (j = 0 ; ; ++j ) {
				double tmp = getarea(i,j,r,g,R-t);
				//printf("%d %d  tmp = %.6lf\n", i,j,tmp);
				if ( tmp <= eps )
					break;
				snull += tmp;
			}
			//printf("i=%d,j=%d\n",i,j);
			if ( j == 0 )
				break;
		}

		sall = PI * R * R;
		snull = 4*snull;
		//printf("%.3lf %.3lf\n", snull, sall);
		printf("Case #%d: %.6lf\n", nc, (sall-snull)/sall);
	}
	return 0;
}
