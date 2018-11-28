#include<iostream>

using namespace std;

int power(int n)
{
int p=1;

for(int i=0;i<n;i++)
p=p*2;

return p;

}




int main()
{
int n,k,i,z=0;

cin>>i;

for(int j=0;j<i;j++)
{
cin>>n>>k;

z=power(n);

if(k%z==(z-1))
cout<<"Case #"<<j+1<<": ON\n";

else
cout<<"Case #"<<j+1<<": OFF\n";
}

}



