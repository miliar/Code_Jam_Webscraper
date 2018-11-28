#include <iostream>
#include <cmath>
#define count 50000000.0

using namespace std;

double dk,dj,dm,dn,dy,dx,dz,d1,d2,f,r,R,t,g,qq;

int tt,i,u,k,j,m,n,x,z,jj,ttt;
double a1,a2,pig,a3,b2,b1;
bool yes;

int main()
{
	ttt=0;
	freopen("C-small-attempt4.in","r",stdin);
	freopen("1.txt","w",stdout);
	cin>>z;
	
	while (z--)
	{
		ttt++;
		printf("Case #%d: ",ttt);

		scanf("%llf%llf%llf%llf%llf",&f,&R,&t,&r,&g);

		dk=R;
		dj=count/dk;
		f*=dj;
		R*=dj;
		t*=dj;
		r*=dj;
		g*=dj;
	
		a1=a2=1e-20;
		n=count;
		for (i=0;i<n;i++)
		{
			dx=i;
			
			dy=sqrt(count*count-dx*dx);
		
			if (dx+f>R-t+1e-20) 
			{
				a1+=dy;
				a2+=dy;
				continue;
			}

			k=dx/(g+r+r);
			dk=k;
			dx-=dk*(g+r+r);
			while (dx<1e-20) dx+=g+r+r;
			while (dx>g+r+r+1e-20) dx-=g+r+r;

			a1+=dy;
		
			if (dx-f>r+1e-20&&dx+f<g+r+1e-20) 
			{
				a3=i;
				pig=1e-20;
				b1=R-t-f;
				b1*=b1;
				if (b1-a3*a3>1e-20)
					pig+=dy-sqrt(b1-a3*a3);
				else pig+=dy;
				if (dy>pig+1e-20)
				{
					a2+=pig;
					dy-=pig;
					k=dy/(g+r+r);
					dk=k;
					a2+=dk*(r+r+f+f);
					dy-=dk*(g+r+r);
					while (dy<1e-20) 
					{
						dy+=g+r+r;
						a2-=r+r+f+f;
					}
					while (dy>g+r+r+1e-20) 
					{
						dy-=g+r+r;
						a2+=r+r+f+f;
					}
					if (dy+f<g+r+1e-20&&dy-f>r+1e-20) a2+=r+f;
					else if (dy+f>g+r+1e-20) a2+=dy-g+f+f;
					else a2+=dy;
				}
				else
				{
					a2+=pig;
				}
			}
			else a2+=dy;
		}
		printf("%.6llf\n",a2/a1);
	}
	return 0;
}


	



