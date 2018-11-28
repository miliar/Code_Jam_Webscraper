#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

const double pi=3.1415926535897932384626;

long casen,k,i,j;
double f,R,t,r,g;
double areahit,areaav,areatmp;
double xi,ymax2,ymax1,xi2,xi3,xx,tmp2,rr,xj;
long z;
double cita;

int main()
{
	freopen("c2.in","r",stdin);
	freopen("test.out","w",stdout);
	cin>>casen;
	for (k=1;k<=casen;k++)
	{
		cin>>f>>R>>t>>r>>g;
		rr=R-t-f;
		areaav=0.25*pi*R*R;
		areahit=0;
		if (r>0 && g>2*f)
		{
			i=0;
			areatmp=(g-2*f)*(g-2*f);
			xi=(i*(g+2*r)+(r+f));
			while (xi*sqrt(2.0)<rr)
			{
				xi2=xi+g-2*f;
				ymax1=sqrt(rr*rr-xi*xi);
				if (rr>=xi2)
				{
					ymax2=sqrt(rr*rr-xi2*xi2);
					j=long(floor((ymax2+f-r-g)/(g+2*r)));
				}
				else 
				{
					j=i-1;
				}
				if (j>=i) areahit=areahit+(2*(j-i)+1)*areatmp;
				j=j+1;
				xj=j*(g+2*r)+r+f;
				while (xj<=ymax1)
				{
					xi3=(j+1)*(g+2*r)-(r+f);
					if (j==i) z=1;
					else z=2;
					if (xi*xi+xj*xj<rr*rr && j>=i)
					{
						if (ymax1>xi3)
						{
							xx=sqrt(rr*rr-xi3*xi3);
							tmp2=(xx-xi)*(g-2*f);
							tmp2=tmp2+0.5*(xi2-xx)*(xi3+ymax2-2*xj);
							cita=atan2(xi3,xx)-atan2(ymax2,xi2);
							tmp2=tmp2+0.5*cita*rr*rr-0.5*rr*rr*sin(cita);
							areahit=areahit+z*tmp2;
						}
						else
						{
							if (ymax2>xj)
							{
								tmp2=0.5*(ymax1+ymax2-2*xj)*(g-2*f);
								cita=atan2(ymax1,xi)-atan2(ymax2,xi2);
								tmp2=tmp2+0.5*cita*rr*rr-0.5*rr*rr*sin(cita);
								areahit=areahit+z*tmp2;
							}
							else
							{
								xx=sqrt(rr*rr-xj*xj);
								tmp2=0.5*(ymax1-xj)*(xx-xi);
								cita=atan2(ymax1,xi)-atan2(xj,xx);
								tmp2=tmp2+0.5*cita*rr*rr-0.5*rr*rr*sin(cita);
								areahit=areahit+z*tmp2;
							}
						}
					}
					j++;
					xj=j*(g+2*r)+r+f;
				}
				i=i+1;
				xi=(i*(g+2*r)+(r+f));
			}
		}
		else if (r==0)
		{
			areahit=0.25*pi*(R-t-f)*(R-t-f);
		}
		cout<<"Case #"<<k<<": "<<setiosflags(ios::fixed)<<setprecision(6)<<1-areahit/areaav<<endl;
	}
	return 0;
}







			