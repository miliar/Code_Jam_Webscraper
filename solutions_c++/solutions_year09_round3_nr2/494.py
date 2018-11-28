#include<iostream>
#include<math.h>

using namespace std;
int main()
{
 double q,tmin,dmin,a,b,c,d,e,f,tempa,tempb,tempc,tempd,tempe,tempf,num,den;
int i,ctr,t;
cin>>t;
for(ctr=1;ctr<=t;ctr++)
{
cin>>q;
a=0.0;
b=0.0;
c=0.0;
d=0.0;
e=0.0;
f=0.0;


for(i=0;i<q;i++)
{
cin>>tempa>>tempc>>tempe>>tempb>>tempd>>tempf;
a += tempa;
b += tempb;
c += tempc;
d += tempd;
e += tempe;
f += tempf;
}
num=0;
//if(b!=0)
//	num += a;
//if(d!=0)
//	num += c;
//if(f!=0)
//	num += e;
	
//if((b!=0)||(d!=0)||(f!=0))
//		tmin=-num/(b+d+f);
//else
//		tmin=0;

num=a*b+c*d+e*f;
den=pow(b,2)+pow(d,2)+pow(f,2);
if((den!=0)&&(num!=0))
	tmin=-num/den;
else
	tmin=0;
if(tmin < 0)
	tmin=0;

//cout<<a<<c<<e<<b<<d<<f<<endl;
dmin = sqrt(pow((a+b*tmin),2)+pow((c+d*tmin),2)+pow((e+f*tmin),2))/double(q);

printf("Case #%d: %.8f %.8f\n",ctr,dmin,tmin);
}
}
