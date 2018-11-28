#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main()
{   int n,i;
    double f,R,t,r,g,x,y,flyR,h,w,all,ex,ey,yi,wi,area;
    double x1,y1,x2,y2,d,ang,l,ans;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {   area=0;
        scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
        if(g>2*f){
        x=r+f;
        flyR=R-t-f;
        y=x;
        yi=y;
        w=sqrt(flyR*flyR-x*x);
        h=w;
        wi=w;
        while(x<w)
        {   while(y<h)
            {   if((x+g-2*f)*(x+g-2*f)+(y+g-2*f)*(y+g-2*f)<=flyR*flyR)
                    area+=(g-2*f)*(g-2*f);
                else
                {   ey=y+g-2*f;
                    ex=x+g-2*f;
                    if(x+g-2*f<=w&&y+g-2*f<=h)
                    {   x1=sqrt(flyR*flyR-ey*ey);
                        y1=ey;
                        x2=ex;
                        y2=sqrt(flyR*flyR-ex*ex);
                        area+=(g-2*f)*(g-2*f)-(ex-x1)*(ey-y2)/2;
                    }
                    else if(x+g-2*f<=w)
                    {   x1=x;
                        y1=sqrt(flyR*flyR-x*x);
                        x2=ex;
                        y2=sqrt(flyR*flyR-ex*ex);
                        area+=(ex-x)*(y2-y)+(ex-x)*(y1-y2)/2;
                    }
                    else if(y+g-2*f<=h)
                    {   x1=sqrt(flyR*flyR-ey*ey);
                        y1=ey;
                        x2=sqrt(flyR*flyR-y*y);
                        y2=y;
                        area+=(ey-y)*(x1-x)+(ey-y)*(x2-x1)/2;
                    }
                    else
                    {   x1=x;
                        y1=sqrt(flyR*flyR-x*x);
                        x2=sqrt(flyR*flyR-y*y);
                        y2=y;
                        area+=(x2-x)*(y1-y)/2;
                    }
                    d=sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
                    ang=asin((d/2)/flyR);
                    l=sqrt(flyR*flyR-d*d/4);
                    area+=ang*flyR*flyR-d*l/2;
                }
                y+=(g+2*r);
                w=sqrt(flyR*flyR-y*y);
            }
            y=yi;
            w=wi;
            x+=(g+2*r);
            h=sqrt(flyR*flyR-x*x);
        }
        all=M_PI*R*R;
        ans=(all-area*4)/all;
        printf("Case #%d: %.6lf\n",i,ans);
        }
        else printf("Case #%d: 1.000000\n",i);
    }
    //system("pause");
    return 0;
}
