#include<stdio.h>
#include<stdlib.h>
#include<math.h>
double lx[201];
double ly[201];
double ux[201];
double uy[201];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out","w",stdout);
	int t,tt;
	scanf("%d",&tt);
	for(t=1;t<=tt;t++)
	{
		printf("Case #%d:\n",t);
		int w,nl,nu,g;
		scanf("%d %d %d %d",&w,&nl,&nu,&g);
		for(int i=0;i<nl;i++)
		{
			scanf("%lf %lf",&lx[i],&ly[i]);
		}
		for(int i=0;i<nu;i++)
		{
			scanf("%lf %lf",&ux[i],&uy[i]);
		}
		int ll,uu;
		double nowx=lx[0];
		double area=0.0;
		ll=uu=0;
		
		while(ll<nl || uu<nu)
		{
//			printf("%d %d %lf %lf %lf\n",ll,uu,area,lx[ll+1],ux[uu+1]);
			if(uu==nu-1 && ll==nl-1) break;
			if(uu==nu-1 || lx[ll+1]<ux[uu+1])
			{
				area+=(( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(nowx-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(nowx-lx[ll])) )+
				       ( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(lx[ll+1]-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(lx[ll+1]-lx[ll])) ))*(lx[ll+1]-nowx)/2;
//				printf("+ %lf + %lf * %lf\n",( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(nowx-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(nowx-lx[ll])) ),
	//			       ( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(lx[ll+1]-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(lx[ll+1]-lx[ll])) ),(lx[ll+1]-nowx));
				nowx=lx[ll+1];
				ll++;
			}
			else
			{
				area+=(( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(nowx-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(nowx-lx[ll])) )+
				       ( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(ux[uu+1]-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(ux[uu+1]-lx[ll])) ))*(ux[uu+1]-nowx)/2;
//				printf("+ %lf + %lf * %lf\n",( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(nowx-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(nowx-lx[ll])) ),
	//			       ( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(ux[uu+1]-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(ux[uu+1]-lx[ll])) ),(ux[uu+1]-nowx));
				nowx=ux[uu+1];
				uu++;
			}
		}
		
		ll=uu=0;
//		printf("%lf\n",area);
		double aa=0.0;
		double aaa=0.0;
		nowx=0.0;
		for(int i=0;i<g-1;i++)
		{
aacc:		aa=area*(i+1)/g;
			double a=(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])-(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll]);
			double b= (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(nowx-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(nowx-lx[ll]));
			double c = aa-aaa;
			double x = (-b+sqrt(b*b+2*a*c))/a;
			if(fabs(a)<1e-8) x=c/b;
			if(b*b+2*a*c<0.0)
			{
				if(uu==nu-1 && ll==nl-1) break;
				if(uu==nu-1 || lx[ll+1]<ux[uu+1])
				{
					aaa+=(( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(nowx-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(nowx-lx[ll])) )+
					       ( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(lx[ll+1]-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(lx[ll+1]-lx[ll])) ))*(lx[ll+1]-nowx)/2;
	//				printf("+ %lf + %lf * %lf\n",( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(nowx-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(nowx-lx[ll])) ),
		//			       ( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(lx[ll+1]-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(lx[ll+1]-lx[ll])) ),(lx[ll+1]-nowx));
					nowx=lx[ll+1];
					ll++;
				}
				else
				{
					aaa+=(( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(nowx-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(nowx-lx[ll])) )+
					       ( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(ux[uu+1]-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(ux[uu+1]-lx[ll])) ))*(ux[uu+1]-nowx)/2;
	//				printf("+ %lf + %lf * %lf\n",( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(nowx-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(nowx-lx[ll])) ),
		//			       ( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(ux[uu+1]-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(ux[uu+1]-lx[ll])) ),(ux[uu+1]-nowx));
					nowx=ux[uu+1];
					uu++;
				}
				goto aacc;
			}
			double xx = nowx+x;
//			printf("!!%lf %lf (%lf %lf %lf) %d %d\n",nowx,x,a,b,c,ll,uu);
			while(ll<nl || uu<nu)
			{
				if(uu==nu-1 && ll==nl-1) break;
				if((ll==nl-1 || xx<lx[ll+1]) && (uu==nu-1 || xx<ux[uu+1])) break;
				if(uu==nu-1 || lx[ll+1]<ux[uu+1])
				{
					aaa+=(( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(nowx-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(nowx-lx[ll])) )+
					       ( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(lx[ll+1]-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(lx[ll+1]-lx[ll])) ))*(lx[ll+1]-nowx)/2;
	//				printf("+ %lf + %lf * %lf\n",( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(nowx-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(nowx-lx[ll])) ),
		//			       ( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(lx[ll+1]-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(lx[ll+1]-lx[ll])) ),(lx[ll+1]-nowx));
					nowx=lx[ll+1];
					ll++;
				}
				else
				{
					aaa+=(( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(nowx-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(nowx-lx[ll])) )+
					       ( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(ux[uu+1]-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(ux[uu+1]-lx[ll])) ))*(ux[uu+1]-nowx)/2;
	//				printf("+ %lf + %lf * %lf\n",( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(nowx-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(nowx-lx[ll])) ),
		//			       ( (uy[uu]+(uy[uu+1]-uy[uu])/(ux[uu+1]-ux[uu])*(ux[uu+1]-ux[uu])) - (ly[ll]+(ly[ll+1]-ly[ll])/(lx[ll+1]-lx[ll])*(ux[uu+1]-lx[ll])) ),(ux[uu+1]-nowx));
					nowx=ux[uu+1];
					uu++;
				}
				goto aacc;
			}
			printf("%lf\n",xx);
		}
	}
	return 0;
}
