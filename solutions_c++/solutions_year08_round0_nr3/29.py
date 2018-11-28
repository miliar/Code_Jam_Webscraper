#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
#define mp make_pair 
#define pb push_back 
#define eps 0.0000001
#define PI 3.141592653589
FILE *fin=fopen("entrada.in","r");
FILE *fout=fopen("saida.out","w");
bool comp (double a ,double b)
{
    if((a-b)<eps && (b-a)<eps)return true;
    return false;
    
}
double inter(double raio,double x, double y, double lado)
{
     double ponto[10][2];
     int qte=0;
     double z;
     double area=0;
     if(x*x + y*y <raio*raio+eps)
     {
        ponto[qte][0]=x;
        ponto[qte][1]=y;
        qte++;       
     }//1
    
     if(raio*raio-y*y>eps)
     {
        z=sqrt(raio*raio-y*y);
        if(z>x && z<x+lado)
        {
            ponto[qte][0]=z;
            ponto[qte][1]=y;   
            qte++;
        }      
    
     }   //2
     
     if((x+lado)*(x+lado) + y*y <raio*raio+eps)
     {
        ponto[qte][0]=x+lado;
        ponto[qte][1]=y;
        qte++;       
     }//3
     if(raio*raio-(x+lado)*(x+lado)>eps)
     {
        z=sqrt(raio*raio-(x+lado)*(x+lado));
        if(z>y && z<y+lado)
        {
            ponto[qte][0]=x+lado;
            ponto[qte][1]=z;   
            qte++;
        }      
    
     }   //4
     
          if((x+lado)*(x+lado) + (y+lado)*(y+lado) <raio*raio+eps)
     {
        ponto[qte][0]=x+lado;
        ponto[qte][1]=y+lado;
        qte++;       
     }//5
     if(raio*raio-(y+lado)*(y+lado)>eps)
     {
        z=sqrt(raio*raio-(y+lado)*(y+lado));
        if(z>x && z<x+lado)
        {
            ponto[qte][0]=z;
            ponto[qte][1]=y+lado;   
            qte++;
        }      
    
     }   //6
     
     if((x)*(x) + (y+lado)*(y+lado) <raio*raio+eps)
     {
        ponto[qte][0]=x;
        ponto[qte][1]=y+lado;
        qte++;       
     }//7
     if(raio*raio-(x)*(x)>eps)
     {
        z=sqrt(raio*raio-(x)*(x));
        if(z>y && z<y+lado)
        {
            ponto[qte][0]=x;
            ponto[qte][1]=z;   
            qte++;
        }      
    
     }   //8
     for(int i=0;i<qte;i++)
        area+=ponto[i][0]*ponto[(i+1)%qte][1];
     for(int i=0;i<qte;i++)
        area-=ponto[i][1]*ponto[(i+1)%qte][0];
     if(area<0)area=-area;
     double x1,y1,x2,y2;
     int conta=0;
     for(int i=0;i<qte;i++)
     {
         if(comp(ponto[i][0]*ponto[i][0]+ponto[i][1]*ponto[i][1],raio*raio))
         {
            if(conta==0)
            {
                x1=ponto[i][0];
                y1=ponto[i][1];   
                conta++;
            }       
            else
            {
                x2=ponto[i][0];
                y2=ponto[i][1];
                conta++;
                break;
            }
         }  
     }
     area=area/2.0;
    
   if(conta<2)return area;
    
     z=sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
     double angulo=2.0*asin(z/(2.0*raio));
    // fprintf(fout,"%lf\n",angulo);
     z=(angulo/(2.0*PI))*raio*raio*PI - 0.5*raio*raio*sin(angulo);
     
     return z+area;
}
int main ()
{
    int n;
    fscanf(fin,"%d",&n);
    double f,R,t,r,g;
    for(int qw=1;qw<=n;qw++)
    {
      double prob=1;
      
      fscanf(fin,"%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
      double area=PI*R*R;
      if(g>2*f+eps && R>t+f+eps)      
        {
            double pode=0;
            
            for(double x=r+f;x*x<(R-t-f)*(R-t-f);x=x+g+2*r)
            {
                for(double y=r+f;y*y+x*x<(R-t-f)*(R-t-f);y=y+g+2*r)
                {
                    
                    pode=pode+inter(R-t-f,x,y,g-2*f);
                }
            }
            
            prob= 1 - (4.0*pode)/area;
        }
       fprintf(fout,"Case #%d: %.6lf\n",qw,prob);
    }
    
    return 0;   
}
