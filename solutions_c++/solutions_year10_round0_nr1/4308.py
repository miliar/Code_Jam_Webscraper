#include<fstream.h>
#include<conio.h>

int main()
{

ifstream in;
ofstream ou;
long int i,k;
int arr[2][30],n,m=1,t,j;
clrscr();

in.open("A-small.in",ios::in);
if(!in)
{
cout<<"input File error";
return 0;
}
ou.open("A-small.out",ios::out);
if(!ou)
{
cout<<"ouput File error";
return 0;
}
in>>t;

while(m<=t)
{
ou<<"Case #"<<m<<": ";
m++;
in>>n;
in>>k;

if(k%2==0||k==0)
{
ou<<"OFF"<<'\n';
continue;
}
for(i=1;i<n;i++)
arr[0][i]=arr[1][i]=0;

arr[1][0]=1,arr[0][0]=0;

for(i=0;i<k;i++)
{
	for(j=n-1;j>0;j--)
		{
		   if(arr[0][j-1]==1&&arr[1][j-1]==1)
		   arr[0][j]=arr[0][j]?0:1;
		}
		arr[0][0]=!arr[0][0];
	for(j=1;j<n;j++)
	{
		if(arr[0][j-1]==1&&arr[1][j-1]==1)
		{
		arr[1][j]=1;
		}
		else while(j<n)
		{
		arr[1][j]=0;
		j++;
		}
	}

}

for(i=0;i<n;i++)
{
if(arr[0][i]!=1||arr[1][i]!=1)
{
ou<<"OFF"<<'\n';
n=0;
}
}
if(n!=0)
ou<<"ON"<<'\n';;
}

in.close();
ou.close();
return 0;

}