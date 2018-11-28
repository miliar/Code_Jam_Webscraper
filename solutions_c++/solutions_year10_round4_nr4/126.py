#include<math.h>  
#include<stdio.h>  

#define sqr(x) ((x) * (x))
#define dis2(a, b) (sqrt(sqr(a.x - b.x) + sqr(a.y - b.y)))
double const PI = acos(-1.0);


typedef struct
{
	double x, y;
}point;

typedef struct
{
	point c;
	double r;
}circle;
point goat[10], buck[100];
circle cir[10];

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
    A1 = PI * sqr(cir1.r);  
    A2 = PI * sqr(cir2.r);  
    d = dis2(cir1.c, cir2.c);
      
    if (d >= cir1.r + cir2.r) return 0;  
    if (d <= cir1.r - cir2.r) return A2;  
       
    ang1 = acos((sqr(cir1.r)+ sqr(d) - sqr(cir2.r)) / 2 / cir1.r/ d);  
    ang2 = acos((sqr(cir2.r)+ sqr(d) - sqr(cir1.r)) / 2 / cir2.r/ d);  
    
    ret -= sqr(cir1.r) * ang1 - sqr(cir1.r) * sin(ang1) * cos(ang1);
    ret -= sqr(cir2.r) * ang2 - sqr(cir2.r) * sin(ang2) * cos(ang2); 
    return -ret;
} 

int N, M;
int main()
{
    int T, test, i;
    scanf("%d", &T);
    double ans[50];
    for(test = 1; test <= T; test ++)
    {
        scanf("%d%d", &N, &M);
        for(i = 0; i < N; i ++)
            scanf("%lf%lf", &(goat[i].x), &(goat[i].y));
        for(i = 0; i < M; i ++)
            scanf("%lf%lf", &(buck[i].x), &(buck[i].y));
        
        for(i = 0; i < M; i ++)
        {
            cir[0].c = goat[0]; cir[0].r = dis2(goat[0], buck[i]);
            cir[1].c = goat[1]; cir[1].r = dis2(goat[1], buck[i]);
            ans[i] =  IntersectionArea(cir[0], cir[1]);
        }    
        printf("Case #%d: %.8lf", test, ans[0]);
        for(i = 1; i < M; i ++)
            printf(" %.8lf", ans[i]);
        printf("\n");
    }
	return 0;
}
