#include<iostream>
#include<cmath>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
int test,cnt,i,j,k,t,n,s,p,flag1=0,flag=0,num,q;
fstream fout("output.txt",ios::out);
cin>>test;
for(q=1;q<=test;q++)
{
	cin>>n>>s>>p;
	cnt=0;
	int a[n];
	for(i=0;i<n;i++)
	cin>>a[i];
sort(a,a+n);
	t=n;
	int w=0;
	while(t--)
	{
		num=a[w];
		flag1=0;
		if(s==0)
		flag=0;
		else
		flag=1;
	if(flag==0)
	{
		for(i=0;i<=10;i++)
		{	
			for(j=0;j<=10;j++)
			{
				k=num-i-j;
				if(k>=0&&k<=10&&(abs(k-i)<=1&&abs(k-j)<=1&&abs(i-j)<=1)&&max(max(i,j),k)>=p)
				{cnt++;flag1=1;cout<<i<<" "<<j<<" "<<k<<" "<<endl;break;}
			}
			if(flag1==1)
			break;
		}
}
flag1=0;
	if(flag==1)
	{
	
		for(i=0;i<=10;i++)
		{	
			for(j=0;j<=10;j++)
			{
				k=num-i-j;
				if(k>=0&&k<=10&&abs(k-i)<=2&&abs(k-j)<=2&&abs(i-j)<=2&&max(max(i,j),k)>=p)
				{cnt++;flag1=1;
				if(abs(k-i)==2||abs(k-j)==2)
				{s--;}	
				cout<<i<<" "<<j<<" "<<k<<" "<<num<<endl;			
				break;}
			}
if(flag1==1)
break;
		}
}
w++;
}
fout <<"Case #"<<(q)<<": "<<cnt<< "\n";
}
return 0;
}

