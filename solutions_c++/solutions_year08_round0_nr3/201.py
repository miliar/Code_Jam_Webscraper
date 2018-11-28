/*
TASK: C_swatter
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define epsi (1e-8)
#define YY(x) (sqrt(ar*ar-(x)*(x)))

FILE *fin,*fout;
double f, R, t, r, g;
double ar,sd;
double p;

inline double ABS(double x) {if(x<-epsi) return (-x); return x;}
inline double DISS(double x,double y) {return x*x+y*y;}

int main()
{
    int sos,ss,i,j,uguu;
    double limu,mx,my,nx,ny,lx,ly,ma,na;
    fin = fopen("C-large.in","r");
    fout = fopen("C-large.out","w");
    fscanf(fin,"%d",&ss);
    for(sos=1;sos<=ss;sos++)
    {
        printf("---%d---\n",sos);
        fscanf(fin,"%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
        ar = R-t-f;
        sd = g-2*f;
        if(ar<epsi || sd<epsi) p = 1;
        else
        {
            i = 0;
            p = 0; r = r + f; g = sd;
            while(true)
            {
                limu = YY(r);
                if((2*r+g)*i+r > limu) break;
                limu = YY((2*r+g)*i+r);
                j = 0;
                while(limu > (2*r+g)*j+r)
                {
                    lx = (2*r+g)*i+r; ly = (2*r+g)*j+r;
                    if(DISS(lx+g,ly+g) <= ar*ar)
                    {
                        p = p + g*g;
                    }
                    else
                    {
                        uguu = 0;
                        if(DISS(lx+g,ly) <= ar*ar)
                        {
                            uguu += 1;
                            nx = lx+g; ny = YY(nx);
                        }
                        else
                        {
                            ny = ly; nx = YY(ny);
                        }
                        if(DISS(lx,ly+g) <= ar*ar)
                        {
                            uguu += 2;
                            my = ly+g; mx = YY(my);
                        }
                        else
                        {
                            mx = lx; my = YY(mx);
                        }
                        //add the segment = sector - triangle
                        ma = atan2(my,mx);
                        na = atan2(ny,nx);
                        p = p + (ar*ar/2)*((ma-na)-sin(ma-na));
                        //add the remainder
                        if(uguu==0) p = p + ((my-ly)*(nx-lx)/2);
                        else if(uguu==1) p = p + ((my-ly+ny-ly)*g/2);
                        else if(uguu==2) p = p + ((mx-lx+nx-lx)*g/2);
                        else p = p + g*g - ((lx+g-mx)*(ly+g-ny)/2);
                    }
                    j++;
                }
                //printf("%d ",j);
                i++;
            }
            p = 1-(p*4/(M_PI*R*R));
        }
        fprintf(fout,"Case #%d: %lf\n",sos,p);
        printf("Case #%d: %lf\n",sos,p);
    }
    system("PAUSE");
    return 0;
}
