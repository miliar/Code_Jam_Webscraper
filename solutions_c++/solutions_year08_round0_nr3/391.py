#include<cstdio>
#include<cmath>

bool dbg=0;
long double f,R,t,r,g;
long double rad,G;
void readCase()
{
    scanf("%llf%llf%llf%llf%llf",&f,&R,&t,&r,&g);

    if(dbg)printf("f:%llf, R:%llf, t:%llf, r:%llf, g:%llf\n",f,R,t,r,g);
    rad=R-t-f;
    G=g-2*f;
}

inline long double distance(long double x,long double y)
{
    return sqrt(x*x+y*y);
}

inline long double segment(long double x1,long double y1,long double x2,long double y2)
{
    long double sinus=distance(x1-x2,y1-y2)/(2*rad);
    long double alpha=asin(sinus);
    long double result=rad*rad*(2*alpha-sin(2*alpha))/2;
    return result;
}

inline long double computeSquare(long double x1,long double y1,long double x2,long double y2)
{
    long double result=0;
    if(distance(x2,y2)<=rad)
    {
	result=(x2-x1)*(y2-y1);
	if(dbg)printf("OK\n");
    }
    else if(distance(x1,y1)>=rad)
    {
	result=0;
    }
    else
    {
	long double x3=sqrt(rad*rad-y1*y1);	
	long double x4=sqrt(rad*rad-y2*y2);	
	long double y3=sqrt(rad*rad-x1*x1);	
	long double y4=sqrt(rad*rad-x2*x2);	
	if((x3<x2)&&(y3<y2))
	    result=segment(x3,y1,x1,y3)+(x3-x1)*(y3-y1)/2;
	else if((x3<x2)&&(y3>=y2))
	    result=segment(x3,y1,x4,y2)+(x3+x4-2*x1)*(y2-y1)/2;
	else if((x3>=x2)&&(y3<y2))
	    result=segment(x2,y4,x1,y3)+(y4+y3-2*y1)*(x2-x1)/2;
	else if((x3>=x2)&&(y3>=y2))
	    result=segment(x2,y4,x4,y2)+(y4-y1)*(x2-x1)+(x2+x4-2*x1)*(y2-y4)/2;
    if(dbg)printf("computeSquare(%.2llf,%.2llf,%.2llf,%.2llf):%.2llf\n",x1,y1,x2,y2,result);
    }
    return result;    
}

void solveCase(int cas)
{
    if(rad<=0||G<=0)
    {
	printf("Case #%d: 1.000000\n",cas);
    }
    else
    {
	long double area=+0;
	for(long double x=r+f;x<rad;x+=g+2*r)
	    for(long double y=r+f;y<rad;y+=g+2*r)
	    {
		area+=computeSquare(x,y,x+G,y+G);
//		if(dbg)printf("x:%.2llf,y:%.2llf, area:%.2llf\n",x,y,area);
	    }
	if(dbg)printf("area:%llf(/%llf)\n",area,R*R*M_PI/4);
	long double result=1-(area/(R*R*M_PI/4));
	printf("Case #%d: %.6llf\n",cas,result);
    }
}
		
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
	readCase();
	solveCase(i+1);
    }
    return 0;
}
