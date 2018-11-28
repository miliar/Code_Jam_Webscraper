#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
const   double   INF=1e100;  
const   double   ZERO=1e-6;  
const   double   PI=2*asin(1.0);  
 struct   XYpoint{     //(x,y)  
        double   x;  
        double   y;  
  };  
 struct   XYline{       //   Ax+By+C=0;  
        double   A;  
        double   B;  
        double   C;  
  };  
   
 /********************************************/  
 /*                         两点确定一条直线                             */  
 /********************************************/  
  XYline   makeLine(double   x1,double   y1,double   x2,double   y2)  
  {  
        XYline   line;  
        line.A=(y2-y1);  
        line.B=(x1-x2);  
        line.C=y1*(x2-x1)+x1*(y1-y2);  
        return   line;  
  } 
 /********************************************/  
 /*                             判断直线相交                                 */  
 /*         1   -   有交点     0   -   无交点     -1   -   重合           */  
 /********************************************/  
  int   inter_LL(   XYline   line1   ,   XYline   line2   ,   XYpoint   &point   )  
  {  
        if(line1.A*line2.B   ==   line1.B*line2.A)  
        {  
              if(line1.A*line2.C   ==   line1.C*line2.A   &&   line1.B*line2.C   ==   line1.C*line2.B)  
                    return   -1;//   重合  
              else  
                    return   0;//   平行  
        }  
        else  
        {  
              point.x=   -1   *   (line1.C*line2.B-line2.C*line1.B)   /   (line1.A*line2.B-line2.A*line1.B);  
              point.y=   -1   *   (line1.C*line2.A-line2.C*line1.A)   /   (line1.B*line2.A-line2.B*line1.A);  
              //   交点  
              return   1;  
        }  
  }
  bool in(double y,double y1,double y2)
  {
	  if(y1>y2)swap(y1,y2);
	  return y>y1&&y<y2;
  }
  int n;
  double b1[1000],b2[1000];
  bool check(int i,int j)
  {
	  XYline line1=makeLine(0,b1[i],1e4,b2[i]);
	  XYline line2=makeLine(0,b1[j],1e4,b2[j]);
	  XYpoint p;
	  int res=inter_LL(line1,line2,p);
	  if(res!=1) return false;
	  if(in(p.y,b1[i],b2[i])) return true;
	  return false;
  }
  
  int main()
  {
	  int T;
	  scanf("%d",&T);
	  int ans;
	  for(int q=1;q<=T;q++)
	  {     
		    ans=0;
			scanf("%d",&n);
			for(int i=0;i<n;i++)
			{
				scanf("%lf%lf",b1+i,b2+i);
			}
			for(int i=0;i<n;i++)
				for(int j=i+1;j<n;j++)
				{
					if(check(i,j)) ans++;
				}
			printf("Case #%d: %d\n",q,ans);
	  }
  }