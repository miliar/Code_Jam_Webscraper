#include<iostream>
#include<stdlib.h>
#include<math.h>
#include<cstdio>

using namespace std;

class Recycle{
public:
long A,B;
void input();
void output();
long digits(long);
};

void Recycle::input()
{
cin>>A;
cin>>B;
}

long Recycle::digits(long i)
{
long j=0,k=0;
while(i/((long)pow(10,j++))>0)
k++;
return k;
}

void Recycle::output()
{
long count=0;
for(long i=A;i<B;i++)
{
long m=0;
long n=digits(i);
for(long j=1;j<n;j++)
{
long q=i/((long)pow(10,j));
long r=i%((long)pow(10,j));
long x=(r*((long)pow(10,n-j)))+q;
if((x>i)&&(x<=B)&&(x!=m))
{
m=x;
count++;
}
}
}
cout<<count;
}

int main()
{
Recycle r[60];
int T;
cin>>T;
char ch=getchar();
if(ch=='\n')
{
for(int i=0;i<T;i++)
r[i].input();
for(int i=0;i<T;i++)
{
cout<<"Case #"<<(i+1)<<": ";
r[i].output();
cout<<"\n";
}
}
return 0;
}
