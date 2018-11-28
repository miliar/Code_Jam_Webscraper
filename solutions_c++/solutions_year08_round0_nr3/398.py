#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846

double f, R, t, r, g;

inline double sgn(double x) {
	if(x<0) { return -1; }
	return 1;
}

inline double abs(double x) {
	if(x<0) { return -x; }
	return x;
}

int intersect(double r, double x1, double y1, double x2, double y2, double &r1x, double &r1y, double &r2x, double &r2y) {
	double dx = x2 - x1;
	double dy = y2 - y1;
	double dr = sqrt(dx*dx + dy*dy);
	double D = x1*y2 - x2*y1;
	
	double delta = r*r*dr*dr - D * D;
	if(delta < 0) {
		return 0;
	}
	r1x = (D * dy + sgn(dy) * dx * sqrt(r*r*dr*dr - D*D)) / (dr * dr);
	r1y = (- D * dx + abs(dy) * sqrt(r*r*dr*dr - D*D)) / (dr * dr);

	r2x = (D * dy - sgn(dy) * dx * sqrt(r*r*dr*dr - D*D)) / (dr * dr);
	r2y = (- D * dx - abs(dy) * sqrt(r*r*dr*dr - D*D)) / (dr * dr);
	return 1;
}

int my_intersect(double r, double x1, double y1, double x2, double y2, double &rx, double &ry) {
	double t1x,t1y, t2x,t2y;
	int res = intersect(r, x1,y1, x2,y2, t1x,t1y, t2x,t2y);
	if(res == 0) {
		return 0;
	}
	if(t1x >=0 && t1y >= 0) {
		rx = t1x;
		ry = t1y;
	} else {
		rx = t2x;
		ry = t2y;
	}
}

double get_angle_between_in_radians(double ax, double ay, double bx, double by) {
	double dotproduct = (ax * bx) + (ay * by);
	double result = acos( dotproduct / (sqrt(ax * ax + ay * ay) * sqrt(bx * bx + by * by)) );

	if(dotproduct < 0) {
		if(result > 0) {
			result += M_PI;
		} else {
			result -= M_PI;
		}
	}
	return result;
}

double get_triangle_area(double xa, double ya, double xb, double yb, double xc, double yc) {
	return abs((xb*ya-xa*yb)+(xc*yb-xb*yc)+(xa*yc-xc*ya))/2;
}

double get_triangle_circle_area(double r, double Ax,double Ay, double Mx,double My, double Nx,double Ny) {
	double angle = get_angle_between_in_radians(Mx,My, Nx,Ny);
	double pizza_area = angle/2 * r * r;
	double triangle1_area = get_triangle_area(Ax,Ay, Mx,My, 0,0);
	double triangle2_area = get_triangle_area(Ax,Ay, Nx,Ny, 0,0);
	return pizza_area - triangle1_area - triangle2_area;
}

void solve(int case_number) {
	r += f;
	g -= 2*f;
	double real_R = R - t - f;
	double square_length = g+2*r;
	double double_max_squares = real_R / square_length;
	int int_max_squares = (int)(double_max_squares + 1 );
	
	int i,j;
	double Ax, Ay, Bx, By, Cx, Cy, Dx, Dy;
	double ABx,ABy, ACx,ACy, BDx,BDy, CDx,CDy;
	int Boutside = 0, Coutside = 0, Doutside = 0;
	double total_region_area = 0;
	for(i=0; i<int_max_squares; i++) {
		for(j=0; j<int_max_squares; j++) {
			Ax = r + square_length * i;
			Ay = r + square_length * j;
			
			if(Ax*Ax + Ay*Ay >= real_R*real_R) {
				j = int_max_squares;
			} else {
				Bx = Ax;
				By = Ay + g;
				Cx = Ax + g;
				Cy = Ay;
				Dx = Ax + g;
				Dy = Ay + g;
				
				ABx=0; ABy=0;
				ACx=0; ACy=0;
				BDx=0; BDy=0;
				CDx=0; CDy=0;
				Boutside = 0;
				Coutside = 0;
				Doutside = 0;
				
				if(Bx*Bx + By*By >= real_R*real_R) {
					Boutside = 1;
				}
				
				if(Cx*Cx + Cy*Cy >= real_R*real_R) {
					Coutside = 1;
				}

				if(Dx*Dx + Dy*Dy >= real_R*real_R) {
					Doutside = 1;
				}
				
				double region_area = 0;
				if(Boutside && Coutside) {
					my_intersect(real_R, Ax,Ay, Bx,By, ABx,ABy);
					my_intersect(real_R, Ax,Ay, Cx,Cy, ACx,ACy);
					
					region_area = get_triangle_circle_area(real_R, Ax,Ay, ABx,ABy, ACx,ACy);
				} else if(Boutside) {
					my_intersect(real_R, Ax,Ay, Bx,By, ABx,ABy);
					my_intersect(real_R, Ax,Ay, Cx,Cy, ACx,ACy);
					my_intersect(real_R, Cx,Cy, Dx,Dy, CDx,CDy);

					region_area = get_triangle_circle_area(real_R, Ax,Ay, ABx,ABy, ACx,ACy);
					region_area -= get_triangle_circle_area(real_R, Cx,Cy, CDx,CDy, ACx,ACy);
				} else if(Coutside) {
					my_intersect(real_R, Ax,Ay, Bx,By, ABx,ABy);
					my_intersect(real_R, Ax,Ay, Cx,Cy, ACx,ACy);
					my_intersect(real_R, Bx,By, Dx,Dy, BDx,BDy);

					region_area = get_triangle_circle_area(real_R, Ax,Ay, ABx,ABy, ACx,ACy);
					region_area -= get_triangle_circle_area(real_R, Bx,By, ABx,ABy, BDx,BDy);
				} else if(Doutside) {
					my_intersect(real_R, Ax,Ay, Bx,By, ABx,ABy);
					my_intersect(real_R, Ax,Ay, Cx,Cy, ACx,ACy);
					my_intersect(real_R, Bx,By, Dx,Dy, BDx,BDy);
					my_intersect(real_R, Cx,Cy, Dx,Dy, CDx,CDy);
					
					region_area = get_triangle_circle_area(real_R, Ax,Ay, ABx,ABy, ACx,ACy);
					region_area -= get_triangle_circle_area(real_R, Bx,By, ABx,ABy, BDx,BDy);
					region_area -= get_triangle_circle_area(real_R, Cx,Cy, CDx,CDy, ACx,ACy);
				} else {
					region_area = g * g;
				}
				
				total_region_area += region_area;
			}
		}
	}
	double circle_area = (PI * R * R);
	total_region_area *= 4;
	
	printf("Case #%d: %.6lf\n", case_number, (1.0 - total_region_area/circle_area));
}

int main(void) {
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C.out", "wt", stdout);
	
	int i,N;
	scanf("%d\n",&N);
	for(i=0; i<N; i++) {
		scanf("%lf %lf %lf %lf %lf\n",&f, &R, &t, &r, &g);
		solve(i+1);
	}
	
	return 0;
}