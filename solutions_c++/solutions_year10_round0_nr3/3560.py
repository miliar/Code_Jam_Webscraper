#include<fstream.h>
#include<conio.h>

int main()
{

fstream in, ou;
int k,r,arr[1024];
long sum=0;
int t,i,n,j,val,m=1,max=0;

in.open("C-small.in",ios::in);
clrscr();
if(!in)
{
cout<<"input error";
}
ou.open("C-small.out",ios::out);
if(!ou)
{
cout<<"ouput error";
}
in>>t;

while(m<=t)
{
in>>r>>k>>n;

	for(j=0;j<n;j++)
	in>>arr[j];

	i=0;
	sum=0;
	while(r)
	{       val=0;
		max=0;
		while((val+arr[i])<=k&&max<n)
		{

		val=val+arr[i];

		i++;
		if(i==n)
		i=0;
		max++;
		}

	sum=sum+val;
	r--;
	}
	cout<<"\n";
ou<<"Case #"<<m<<": "<<sum<<"\n";
m++;
}

in.close();
ou.close();
return 0;
}