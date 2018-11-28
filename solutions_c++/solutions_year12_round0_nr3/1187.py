#include<iostream>
#include<fstream>
using namespace std;

int t,a,b,m,n,x,psifia,counter;
ofstream out("recycle.out"); 

int recycle(int z)
{
int kk=z%10;
int result;
result=kk*x+z/10;
return result;
}

int howmany(int z)
{
int i,result=0;
int start=z;
for(i=0;i<psifia;i++)
{z=recycle(z);
 if(z<=b&&z>start)
 result++;
 if(z==start)
 break;}
return result;
}

int main()
{
ifstream in("recycle.in");   
in >> t;
int i,j;

for(i=1;i<=t;i++)
{
in >> a >> b;
counter=0;
psifia=0;
x=1;
while(x<=a)
{x*=10; psifia++;}
x/=10;
for(j=a;j<b;j++)
{counter+=howmany(j);}
out << "Case #" << i << ": " << counter << endl;
}

in.close(); out.close();
return 0;
}
