#include<iostream>
#include<cmath>
using namespace std;
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	double pi, s,s_mall, x1,x2,y1,y2,xx1,yy1,xx2,yy2,x1_end,x2_end,y1_end,y2_end,end,   f,R,t,r,g ,s_small,WHOLE ,s_all,dx,dy,th,dis;
	int i,j,k,sn,tn,seq,num;
	pi=acos(-1);
	WHOLE=1;
	cin>>num;
	for(seq=1;seq<=num;seq++)
	{
		cin>>f>>R>>t>>r>>g;
		printf("Case #%d: ",seq);
		s_all=pi*R*R;
		R-=t+f;
		r+=f;
		g-=2*f;
		if(R<=r)
		{
			printf("%.6f\n",WHOLE);
			continue;
		}
		s=0;
		s_small=g*g;
		sn=0;
		end=sqrt(R*R-r*r);
		for(x1=r;x1<end;x1+=g+2*r)
		{
			x2=x1+g;
			y1_end=sqrt(R*R-x1*x1);
			y2_end=sqrt(R*R-x2*x2);

			tn=(int)( (y2_end+r)/(g+2*r) );
			sn+=tn;
			
			
			
			for(y1=r+tn*(g+2*r);y1<y1_end;y1+=g+2*r)
			{
				y2=y1+g;
				x1_end=sqrt(R*R-y1*y1);
				x2_end=sqrt(R*R-y2*y2);
				

				if(y1_end<=y2 && x1_end<=x2)
				{

					xx1=x1;
					yy1=y1_end;
					xx2=x1_end;
					yy2=y1;

					s+=(yy1-y1)*(xx2-x1)/2;
				}
				else if(y1_end<=y2 && x1_end>x2)
				{
					if(y2_end>y2)
						cout<<"ERROR2"<<endl;
					xx1=x1;
					yy1=y1_end;
					xx2=x2;
					yy2=y2_end;

					s+=(yy1+yy2-y1-y1)*g/2;
				}
				else if(y1_end>y2 && x1_end<=x2)
				{
					xx1=x2_end;
					yy1=y2;
					xx2=x1_end;
					yy2=y1;

					s+=(xx1+xx2-x1-x1)*g/2;
				}
				else
				{
					
					xx1=x2_end;
					yy1=y2;
					xx2=x2;
					yy2=y2_end;
					sn++;
					s-=(x2-xx1)*(y2-yy2)/2;
				}
				dx=xx1-xx2;
			
				dy=yy1-yy2;
				

				dis=sqrt(dx*dx+dy*dy);

				th=2*asin(dis/2/R);

				s+=R*R*th/2-R*dis*cos( th/2 )/2
					;
			}
		}
		s+=sn*s_small;
		s*=4;

		//cout<<s<<' '<<s_all<<endl;
		printf("%.6f\n",1-s/s_all);
	}
	return 0;
}












		

