#include <iostream>
#include <cmath>
using namespace std;
#define tiao system("pause")

int x,y,r;
int xx,yy,rr;
int t;
const double PI = acos(-1);

double dist2(double x, double y, double xx, double yy)
{
	return (x-xx)*(x-xx) + (y-yy)*(y-yy);
}

double cosine(double a, double b, double c) //a b是两条夹边，c是角的顶点
{
	return (a*a + b*b - c*c) / 2 / a / b;
}

double crossArea(double x, double y, double r, double xx, double yy, double rr)
{
	if (dist2(x,y,xx,yy) >= (r+rr)*(r+rr)) return 0;
	if (dist2(x,y,xx,yy) <= (r-rr)*(r-rr)) return PI * min(r,rr) * min(r,rr);

	double ans = 0;
	double d = sqrt(dist2(x,y,xx,yy)); //根号不要忘记了

	double c1 = cosine(r,d,rr);
	double c2 = cosine(rr,d,r);
	double angle1 = acos(c1);
	double angle2 = acos(c2);

//	cout << d << ' ' << c1 << ' ' << c2 << ' ' << angle1 << ' ' << angle2 << endl;
	if (c1 >= 0)
	{
		ans += angle1*r*r - (double)1/2*r*r*sin(angle1*2);
	}
	else
	{
		ans += angle1*r*r + (double)1/2*r*r*sin((PI-angle1)*2);
	}

	if (c2 >= 0)
	{
		ans += angle2*rr*rr - (double)1/2*rr*rr*sin(angle2*2);
	}
	else
	{
		ans += angle2*rr*rr + (double)1/2*rr*rr*sin((PI-angle2)*2);
	}

	return ans;
}

int n;
int m;
int main(void)
{
	int i,j,k,ci,cici,cicici;
	
	
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	
	
	for (cicici=1; cicici<=t; cicici++)
	{
//		scanf("%d%d%d%d%d%d",&x,&y,&r,&xx,&yy,&rr);
//		printf("%.3lf\n",PI*r*r + PI*rr*rr - crossArea(x,y,r,xx,yy,rr));

        printf("Case #%d:", cicici);
        
        scanf("%d%d", &n, &m);
        scanf("%d%d%d%d", &x, &y, &xx, &yy);
        for (i=1; i<=m; i++)
        {
            int xxx, yyy;
            scanf("%d%d", &xxx, &yyy);
            double r = sqrt(dist2(x, y, xxx, yyy));
            double rr = sqrt(dist2(xx, yy, xxx, yyy));
            
            printf(" %.7lf", crossArea(x,y,r,xx,yy,rr));
        }
        
        printf("\n");
	}
	
//	tiao;
    return 0;
}
