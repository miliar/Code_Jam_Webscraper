#include <cstdio>
#include <cmath>
#define eps 1e-8

int main()
{
	int t,tst;
	double P,f,r,R,T,g;
	double X,Y,Stotal,Sescape,x1,x2,y1,y2,qx,qy,cosa,qx1,qx2,qy1,qy2,x,y;
	double pi=atan(1.0)*4.0;
	bool left,right,top,bottom;

	int tmp;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&tst);
	for(t=1;t<=tst;t++)
	{
		scanf("%lf%lf%lf%lf%lf",&f,&R,&T,&r,&g);
		Stotal=pi*R*R;
		Sescape=0;

		if (g<f+f+eps || R<T+f+eps) 
		{
			printf("Case #%d: %lf\n",t,1.0);
			continue;
		}

		r+=f;
		g-=f+f;
		R-=T+f;

		for(X=r;;X+=g+r+r)
		{
			if (X*X+r*r>R*R-eps) break;
			for(Y=r;;Y+=g+r+r)
			{
				if (X*X+Y*Y>R*R-eps) break;

				x1=X; y1=Y;
				x2=X+g; y2=Y+g;
				if (x2*x2+y2*y2<R*R+eps)
				{
					Sescape+=g*g;
					continue;
				}

				x=sqrt(R*R-y1*y1);
				if (x>x1+eps && x<x2-eps) bottom=true; else bottom=false;
				if (R<y2+eps) top=false; else
				{
					x=sqrt(R*R-y2*y2);
					if (x>x1+eps && x<x2-eps) top=true; else top=false;
				}
				y=sqrt(R*R-x1*x1);
				if (y>y1-eps && y<y2+eps) left=true; else left=false;
				if (R<x2+eps) right=false; else
				{
					y=sqrt(R*R-x2*x2);
					if (y>y1-eps && y<y2+eps) right=true; else right=false;
				}

				/* Check
				tmp=0;
				tmp+=left;
				tmp+=right;
				tmp+=top;
				tmp+=bottom;
				if (tmp!=2) printf("WRONG\nWRONG\nWRONG1\nTEST#%d\n",t);
				 End Check*/

				if (left&&bottom)
				{
					qx=sqrt(R*R-y1*y1);
					qy=sqrt(R*R-x1*x1);
					qx-=x1;
					qy-=y1;
					cosa=(2*R*R-qx*qx-qy*qy)/(2*R*R);
					Sescape+=qx*qy/2+R*R*acos(cosa)/2-R*R*sin(acos(cosa))/2;
					continue;
				}

				if (left&&right)
				{
					qy1=sqrt(R*R-x1*x1);
					qy2=sqrt(R*R-x2*x2);
					qy1-=y1;
					qy2-=y1;
					if (qy1<qy2) printf("WRONG\nWRONG\nWRONG2\nTEST#%d\n",t);
					cosa=(2*R*R-g*g-(qy1-qy2)*(qy1-qy2))/(2*R*R);
					Sescape+=g*qy2+(qy1-qy2)*g/2+R*R*acos(cosa)/2-R*R*sin(acos(cosa))/2;
				}
				
				if (top&&bottom)
				{
					qx1=sqrt(R*R-y2*y2);
					qx1-=x1;
					qx2=sqrt(R*R-y1*y1);
					qx2-=x1;
					if (qx1>qx2) printf("WRONG\nWRONG\nWRONG3\nTEST#%d\n",t);
					cosa=(2*R*R-g*g-(qx1-qx2)*(qx1-qx2))/(2*R*R);
					Sescape+=qx1*g+(qx2-qx1)*g/2+R*R*acos(cosa)/2-R*R*sin(acos(cosa))/2;
				}

				if (top&&right)
				{
					qx=sqrt(R*R-y2*y2);
					qx-=x1;
					qy=sqrt(R*R-x2*x2);
					qy-=y1;
					cosa=(2*R*R-(g-qx)*(g-qx)-(g-qy)*(g-qy))/(2*R*R);
					Sescape+=g*g-(g-qx)*(g-qy)/2+R*R*acos(cosa)/2-R*R*sin(acos(cosa))/2;
				}

			}
		}
		Sescape*=4;

		P=1-Sescape/Stotal;
		printf("Case #%d: %lf\n",t,P);
	}
	return 0;
}