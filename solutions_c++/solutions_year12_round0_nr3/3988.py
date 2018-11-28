#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;

int shifter(int n, int j)
{
int mod,nod;
int i;
int nodigits=log10(n)+1;
int array[nodigits];
for(i=0;i<nodigits;i++)
{
array[i]=n%10;
n=n/10;
//cout<<i<<"th digit"<<array[i]<<endl;
}

int k;
for(k=0;k<j;k++)
{
int temp=array[0];
for(i=0;i<nodigits-1;i++)
array[i]=array[i+1];
array[nodigits-1]=temp;

}
int ans=0;
for(i=nodigits-1;i>-1;i--)
ans=ans*10+array[i];
return ans;
}

int main()
{
int nooftest;
ofstream f;f.open("output.txt");
cin>>nooftest;
int testcase;
for(testcase=0;testcase<nooftest;testcase++)
{
int a,b;
cin>>a>>b;
int i;
int count;

count=0;
//cout<<a<<" "<<b<<" "<<log10(a)<<endl;;
int last=-1;
int array[7];
int first=-1;
for(i=a;i<=b;i++)
{
int j;
int t1;
for(t1=0;t1<7;t1++)
array[t1]=-1;
for(j=0;j<(int)(log10(i));j++)
{
array[j]=shifter(i,j+1);

int flag=0;
for(t1=0;t1<j;t1++)
if(array[t1]==array[j])
flag=1;
if(flag==1)
break;
//cout<<i<<" sdf "<<j<<" "<<shifter(i,j+1)<<endl;
if(shifter(i,j+1)>i && shifter(i,j+1)<=b)
{count++;
if(i!=first)
//cout<<")"<<endl<<i<<":( ";cout<<shifter(i,j+1)<<" ";
if(first==i && last==shifter(i,j+1))
cout<<"codered"<<array[j]<<" "<<j<<" "<<array[j-2]<<endl;
first=i;
last=shifter(i,j+1);

}
}
}
cout<<"Case #"<<testcase+1<<": "<<count<<"\n";

f<<"Case #"<<testcase+1<<": "<<count<<"\n";

}
f<<flush;
f.close();
return 0;
}
