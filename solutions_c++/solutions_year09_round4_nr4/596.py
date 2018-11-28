//written on C++ (compatible with DevC++ / MS Visual C++ 6)
#include<math.h>
#include<stdio.h>

double r[40],x[40],y[40];

double dist(int a,int b){return sqrt(((x[a]-x[b])*(x[a]-x[b]))+((y[a]-y[b])*(y[a]-y[b])));}

int main()
{
    double aa,bb,cc,zz;
    int c,i,k,n,z;
    freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	scanf("%d",&c);
	for(z=1;z<=c;z++)
	{scanf("%d",&n,&k);
	 for(i=0;i<n;i++)scanf("%lf %lf %lf",&x[i],&y[i],&r[i]);
	 if(n==1)zz=r[0];
     if(n==2){zz=r[0];if(r[1]>zz)zz=r[1];}
     if(n==3)
     {aa=dist(0,1)+r[0]+r[1];if(aa<r[2])aa=r[2];
      bb=dist(0,2)+r[0]+r[2];if(bb<r[1])bb=r[1];
      cc=dist(1,2)+r[1]+r[2];if(cc<r[0])cc=r[0];
      zz=aa;if(bb<zz)zz=bb;if(cc<zz)zz=cc;
      zz/=2.0;
     }
     printf("Case #%d: %.6lf\n",z,zz);
    }
    return 0;
}
