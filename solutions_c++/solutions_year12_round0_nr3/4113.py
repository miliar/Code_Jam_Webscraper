#include<iostream>
#include<fstream>
using namespace std;
int main()
{
int test=0,i,l,l1,l2,j;
cin>>test;
int a,b,z,x,c,t,cnt=0;
fstream fout("output.txt",ios::out);
for(j=1;j<=test;j++)
{
	cnt=0;
	cin>>a>>b;
	
for(i=a;i<=b;i++)
{
	int p=i;
	t=0;
	int q[3]={0,0,0};
	while(t!=3)
	{
	q[t]=p%10;
	p=p/10;
	t++;
	}
	
	if(q[2]==0&&q[1]!=0)
	{
	z=q[1]*10+q[0];
	x=q[1]+q[0]*10;
	if((z>i&&z<=b))
	{cnt++;}
	if((x>i&&x<=b))
	{cnt++;}
	}
	else if(q[2]!=0)
	{
	
	z=q[2]*100+q[1]*10+q[0];
	x=q[1]*100+q[0]*10+q[2];
	c=q[0]*100+q[1]+q[2]*10;
	if((z>i&&z<=b))
	{cnt++;}
	if(x>i&&x<=b)
	{cnt++;}
	if((c>i&&c<=b))
	{cnt++;}
	
	}
	
	
}
fout <<"Case #"<<(j)<<": "<<cnt<< "\n";
}

return 0;
}
	

