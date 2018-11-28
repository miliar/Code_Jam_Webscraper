#include <iostream.h>
int main()
{
int t,t1,n,i,j,om=0;
long a[1000],b[1000],c,d;
cin>>t;
for(t1=1;t1<=t;t1++)
{

cin>>n;
for(i=0;i<n;i++)
{
	cin>>a[i];
	cin>>b[i];
}

for(i=0;i<n;i++)
{
	for(j=i+1;j<n;j++)
	{
		c=a[i]-a[j];
		d=b[i]-b[j];
		if((c*d)<0)
		om++;
	}
}
cout<<"Case #"<<t1<<": "<<om<<"\n";	
om=0;
}
}
