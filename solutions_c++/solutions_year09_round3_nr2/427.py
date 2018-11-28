#include<iostream>
#include<cmath>
#include<iomanip>
#define eps 1e-6
using namespace std;
int aa[500][6];int n;
int main()
{
    freopen("B-small-attempt11.in","r",stdin);//B-large.in
	freopen("1.txt","w",stdout);
	int t,i,j;
	cin>>t;
	for(int cas=1;cas<=t;cas++)
	{
	    cin>>n;
		for(i=0;i<n;i++)
		for(j=0;j<6;j++)
		cin>>aa[i][j];
		double x1,y1,x2,y2,x3,y3;
		x1=y1=x2=y2=x3=y3=0;
		double mt,minn;
		for(i=0;i<n;i++)
		{
		    x1+=aa[i][0];
			y1+=aa[i][3];
			x2+=aa[i][1];
			y2+=aa[i][4];
			x3+=aa[i][2];
			y3+=aa[i][5];	
		}x1/=n;x2/=n;x3/=n;y1/=n;y2/=n;y3/=n;
		double a,b,c;
		a=y1*y1+y2*y2+y3*y3;
		b=2*x1*y1+2*x2*y2+2*x3*y3;
		c=x1*x1+x2*x2+x3*x3;
		if(a==0){mt=0;minn=c;}
		else{
		    if(b/(2*a)<=0){
			    mt=-b/(2*a);
			    minn=mt*mt*a+mt*b+c;	
			}
			else 
			{
			    mt=0;
		    	minn=c;	
			}	
		}minn=sqrt(minn+1e-10);
		cout<<"Case #"<<cas<<": "<<fixed<<setprecision(8)<<minn<<" "<<fixed<<setprecision(8)<<mt+eps<<endl;
			
	}
	
}
