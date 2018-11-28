#include<stdio.h>
#include<string.h>
#include<iostream>
#include<math.h>

using namespace std;

int main()
{
	freopen("r3.in","r",stdin);
	freopen("r3.out","w",stdout);
	long int x,y,z;
	long int fvx[5],fvy[5],fvz[5];
	long int vx,vy,vz,numcases,i,j,num;
	long double dist,ans,t,totx,toty,totz,totvx,totvy,totvz;
	long int temp;
	long int q0,q1,q2;
	
	cin>>numcases;
	for(int n=1;n<=numcases;n++)
	{
		for(i=0;i<5;i++)
		{
			fvx[i]=0;
			fvy[i]=0;
			fvz[i]=0;
		}
		
		
		cin>>num;
		
		for(i=0;i<num;i++)
		{
			cin>>x>>y>>z>>vx>>vy>>vz;
			fvx[0] += x;
			fvy[0] += y;
			fvz[0] += z;
			fvx[1] += vx;
			fvy[1] += vy;
			fvz[1] += vz;
		}
		
		totx = fvx[0];
		totvx = fvx[1];
		toty = fvx[0];
		totvy = fvx[1];
		totz = fvx[0];
		totvz = fvx[1];
		
		temp = fvx[1];
		fvx[1] = fvx[1]*2*fvx[0];
		fvx[0] = fvx[0]*fvx[0];
		fvx[2] = temp*temp;
		//cout<<"fvx[0] = "<<fvx[0]<<"fvx[1] = "<<fvx[1];
		temp = fvy[1];
		fvy[1] = fvy[1]*2*fvy[0];
		fvy[0] = fvy[0]*fvy[0];
		fvy[2] = temp*temp;
		
		temp = fvz[1];
		fvz[1] = fvz[1]*2*fvz[0];
		fvz[0] = fvz[0]*fvz[0];
		fvz[2] = temp*temp;
		
		//cout<<"\n"<<fvx[0]<<fvy[0]<<fvz[0];
		
		q0 = fvx[0]+fvy[0]+fvz[0];
		q1 = fvx[1]+fvy[1]+fvz[1];
		q2 = fvx[2]+fvy[2]+fvz[2];
		//cout<<"\nq0 ="<<q0;
		//cout<<"q1 ="<<q1;
		//cout<<"q2 ="<<q2;
		if(q2)
		{	
			t = (-(float)q1)/((float)q2);
			t=t/2;
		}
		else
			t=0;
		if(t<=0)
			t=0;
		//cout<<" t="<<t;
		//totx+=totvx*t;
		//toty+=totvy*t;
		//totz+= totvz*t;
		dist = q0+q1*t+q2*t*t;
		ans = sqrt(dist);
		ans = ans/num;
		cout<<"Case #"<<n<<": "<<ans<<" "<<t<<"\n";
	}
	return 0;
}
	

