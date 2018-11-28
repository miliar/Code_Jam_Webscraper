#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <string>
#include <vector>
#include <string.h>
using namespace std;

int n;

    double param;
    
    
#include<math.h>  
#include<stdio.h>  


//template from blog 
//http://onchf.spaces.live.com/blog/cns!C1747339B0D46E11!298.entry
#define pi acos(-1.0)
#define sqr(x) ((x) * (x))
#define dis2(a, b) (sqrt(sqr(a.x - b.x) + sqr(a.y - b.y)))

struct point
{
	double x, y;
};

struct circle
{
	point c;
	double r;
};

double IntersectionArea(circle cir1, circle cir2)
{  
	double A1, A2, d, ang1, ang2;
	circle ctmp;
	if (cir1.r < cir2.r)  
    {  
		ctmp = cir1;
		cir1 = cir2;
		cir2 = ctmp;	
    }
    double ret = 0;  
    A1 = pi * sqr(cir1.r);  
    A2 = pi * sqr(cir2.r);  
    d = dis2(cir1.c, cir2.c);
      
    if (d >= cir1.r + cir2.r) return 0;  
    if (d <= cir1.r - cir2.r) return A2;  
       
    ang1 = acos((sqr(cir1.r)+ sqr(d) - sqr(cir2.r)) / 2 / cir1.r/ d);  
    ang2 = acos((sqr(cir2.r)+ sqr(d) - sqr(cir1.r)) / 2 / cir2.r/ d);  
    
    ret -= sqr(cir1.r) * ang1 - sqr(cir1.r) * sin(ang1) * cos(ang1);
    ret -= sqr(cir2.r) * ang2 - sqr(cir2.r) * sin(ang2) * cos(ang2); 
    return -ret;
} 



    
int main() {
	int test;
	circle cir1, cir2;
double x1,y1,x2,y2;
double x3,y3,r1,r2;
    int T;
    scanf("%d", &T);
    int c, i, j, k;
    int res;
    int R;
    int n1, n2;
    int start = 0;
    int j1,k1,j2,k2;
    int ax, bx;int m;

    for (c = 1; c <= T; c++) {
        scanf("%d", &n);
        scanf("%d", &m);
        scanf("%lf%lf%lf%lf", &x1,&y1,&x2,&y2);
        printf("Case #%d:", c);
        while (m--) {
            scanf("%lf%lf", &x3,&y3);
            r1 = (x1-x3)*(x1-x3)+(y1-y3)*(y1-y3);
            r2 = (x2-x3)*(x2-x3)+(y2-y3)*(y2-y3);
            cir1.c.x = x1;
            cir1.c.y = y1;
            cir2.c.x = x2;
            cir2.c.y = y2;
            cir1.r = sqrt(r1);
            cir2.r = sqrt(r2);
            printf(" %.7lf", IntersectionArea(cir1, cir2));
        }
        putchar(10);
    }
    return 0;
}
