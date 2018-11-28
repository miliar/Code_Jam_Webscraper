#include<stdio.h>
#include<math.h>
const double Pi = acos(-1);


int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int n;
	double f,R,t,r,g;
	double rr,temp,sinx,jiao;
	double match;
	double i,j;
	double X1,X2,Y1,Y2,y2,x2;
	scanf("%d",&n);
	for(int c=1;c<=n;c++) {
		scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
		if(2*f >= g) {
			printf("Case #%d: 1.000000\n",c);
			continue;
		}
		rr = R - t - f;
		match = 0;
		for(i=r+f;i<rr;i+=g+2*r) {
			y2 = i + g - 2*f;
			X1 = sqrt(rr*rr - i*i);
			X2 = 0.0;
			if(y2<rr) X2 = sqrt(rr*rr - y2*y2);
			j = r + f;
			for(j=r+f;j < X1 || j < X2;j+= g + 2 * r) {
				x2 = j + g - 2*f;
				Y1 =  sqrt(rr*rr - j*j);
				Y2 = 0.0;
				if(x2<rr) Y2 =  sqrt(rr*rr - x2*x2);
				if(y2 <= Y2 && x2 <= X2) {//juxing
					match += (g-2*f)*(g-2*f);
				} else if(x2 >= X2 && y2 >= Y2 && y2 <= Y1 && x2 <= X1) {
					temp = sqrt((X2-x2)*(X2-x2)+(y2-Y2)*(y2-Y2));
					sinx = temp/2/rr;
					jiao = asin(sinx);
					//printf("%lf\n",jiao);
					match+= rr*rr*jiao;
					match-= temp * sqrt(rr*rr-(temp/2)*(temp/2)) / 2;
					match += (g-2*f)*(g-2*f) - (x2-X2)*(y2-Y2)/2;
				} else if(y2 >= Y1 && x2 <= X1) {
					temp = sqrt((Y2-Y1)*(Y2-Y1)+(x2-j)*(x2-j));
					sinx = temp/2/rr;
					jiao = asin(sinx);
					match += rr*rr*jiao;
					match -= temp * sqrt(rr*rr-(temp/2)*(temp/2)) / 2;
					match += (Y2 - i) * (g - 2*f) + (Y1 - Y2) * (g - 2*f) / 2;
				}else if(x2 >= X1 && y2 <= Y1) {
					temp = sqrt((X2-X1)*(X2-X1)+(y2-i)*(y2-i));
					sinx = temp/2/rr;
					jiao = asin(sinx);
					match += rr*rr*jiao;
					match -= temp * sqrt(rr*rr-(temp/2)*(temp/2)) / 2;
					match += (X2 - j) * (g - 2*f) + (X1 - X2) * (g - 2*f) / 2;
				} else if(y2 >= Y1 && x2 >= X1) {
					temp = sqrt((X1-j)*(X1-j)+(i-Y1)*(i-Y1));
					sinx = temp/2/rr;
					jiao = asin(sinx);
					match+= rr*rr*jiao;
					match-= temp * sqrt(rr*rr-(temp/2)*(temp/2)) / 2;
					match += (X1-j)*(Y1-i)/2;
				}			
			}

		}
		double squre = R*R*Pi/4;
		printf("Case #%d: %.6f\n",c,(squre-match)/squre);
	}
	return 0;
}