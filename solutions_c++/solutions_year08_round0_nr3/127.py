#include<stdio.h>
#include<math.h>
const double PI = 3.1415926535897932;
int main()
{
	FILE *in = freopen("C-large.in","r",stdin);
	FILE *out = freopen("C-large.out","w",stdout);
	int n,N;
	double f,R,t,r,g;
	scanf("%d",&N);
	for(n=0;n<N;n++) {
		scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
		if(2*f >= g) {
			printf("Case #%d: 1.000000\n",n+1);
			continue;
		}
		double R2 = R - t - f;
		double blank = 0.0;
		double x,y;
		for(y=r+f;y<R2;y+=g+2*r) {
			double y2 = y + g - 2*f;
			double X1 = sqrt(R2 * R2 - y * y);
			double X2 = 0.0;
			if(y2<R2) X2 = sqrt(R2 * R2 - y2 * y2);
			x = r + f;
			while(x < X1 || x < X2) {
				double x2 = x + g - 2*f;
				double Y1 =  sqrt(R2 * R2 - x * x);
				double Y2 = 0.0;
				if(x2<R2) Y2 =  sqrt(R2 * R2 - x2 * x2);
				if(y2 <= Y2 && x2 <= X2) {
					blank += (g-2*f)*(g-2*f);
				}else if(x2 >= X1 && y2 <= Y1) {
					double xuan = sqrt((X2-X1)*(X2-X1)+(y2-y)*(y2-y));
					double sina = xuan/2/R2;
					double a = asin(sina);
					double sanxin = PI*R2*R2*a/PI;
					double sanjiao = xuan * sqrt(R2*R2-(xuan/2)*(xuan/2)) / 2;
					blank += sanxin - sanjiao;
					blank += (X2 - x) * (g - 2*f) + (X1 - X2) * (g - 2*f) / 2;
				} else if(y2 >= Y1 && x2 <= X1) {
					double xuan = sqrt((Y2-Y1)*(Y2-Y1)+(x2-x)*(x2-x));
					double sina = xuan/2/R2;
					double a = asin(sina);
					double sanxin = PI*R2*R2*a/PI;
					double sanjiao = xuan * sqrt(R2*R2-(xuan/2)*(xuan/2)) / 2;
					blank += sanxin - sanjiao;
					blank += (Y2 - y) * (g - 2*f) + (Y1 - Y2) * (g - 2*f) / 2;
				} else if(x2 >= X2 && y2 >= Y2 && y2 <= Y1 && x2 <= X1) {
					double xuan = sqrt((X2-x2)*(X2-x2)+(y2-Y2)*(y2-Y2));
					double sina = xuan/2/R2;
					double a = asin(sina);
					double sanxin = PI*R2*R2*a/PI;
					double sanjiao = xuan * sqrt(R2*R2-(xuan/2)*(xuan/2)) / 2;
					blank += sanxin - sanjiao;
					blank += (g-2*f)*(g-2*f) - (x2-X2)*(y2-Y2)/2;
				} else if(y2 >= Y1 && x2 >= X1) {
					double xuan = sqrt((X1-x)*(X1-x)+(y-Y1)*(y-Y1));
					double sina = xuan/2/R2;
					double a = asin(sina);
					double sanxin = PI*R2*R2*a/PI;
					double sanjiao = xuan * sqrt(R2*R2-(xuan/2)*(xuan/2)) / 2;
					blank += sanxin - sanjiao;
					blank += (X1-x)*(Y1-y)/2;
				}
				x += g + 2 * r;
			}

		}
		double re = 1.0-blank*4/(R*R*PI);
		printf("Case #%d: %.6f\n",n+1,re);

	}

	return 0;
}