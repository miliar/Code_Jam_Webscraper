#include <stdio.h>
#include <math.h>

int x[500];
int y[500];

int main()
{
	int ic,nc,i,w,l,u,g,j,k;
	double a1,a2,p,wi,d1,d2,dl,sq;
	scanf("%d",&nc);
	for (ic=1;ic<=nc;++ic)
	{
		scanf("%d %d %d %d",&w,&l,&u,&g);
		scanf("%d %d",x,y);
		a1=0.0;
		for (i=1;i<l;++i)
		{
			scanf("%d %d",x+i,y+i);
			a1+=(x[i]-x[i-1])*(y[i]+y[i-1]);
		}

		scanf("%d %d",x+l,y+l);
		a2=0.0;
		for (i=1;i<u;++i)
		{
			scanf("%d %d",x+l+i,y+l+i);
			a2+=(x[l+i]-x[l+i-1])*(y[l+i]+y[l+i-1]);
		}

		i=0;
		j=l;

		a2=(a2-a1)/2.0;
		a2/=g;
		a1=0.0;
		p=0.0;
		printf("Case #%d:\n",ic);
		k=0;
		while (1)
		{
			d1=(y[i+1]-y[i])/(double)(x[i+1]-x[i]);
			d2=(y[j+1]-y[j])/(double)(x[j+1]-x[j]);
			wi=(y[j]+d2*(p-x[j]))-(y[i]+d1*(p-x[i]));
			dl=w+1;
			if (fabs(d1-d2)<1e-10)
			{
				dl=(a2-a1)/wi;
			} else
			{
				sq=2*(a2-a1)*(d2-d1)+wi*wi;
				if (sq>=0.0)
				{
					dl=(wi-sqrt(sq))/(d1-d2);
					if (dl<0) dl=w+1;
				}
			}
			if (dl<=x[i+1]-p && dl<=x[j+1]-p)
			{
				p+=dl;
				a1=0.0;
				printf("%.10lf\n",p);
				++k;
				if (k==g-1) break;
			} else
			{
				if (x[i+1]<x[j+1])
				{
					++i;
					dl=x[i]-p;
					p=x[i];
				} else
				{
					++j;
					dl=x[j]-p;
					p=x[j];
				}
				a1+=dl*wi+(d2-d1)*dl*dl*0.5;
			}
		}
	}
	return 0;
}
