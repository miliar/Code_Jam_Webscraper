#include<iostream>
using namespace std;
unsigned long earning(unsigned long gr[],long K,int N);
void shifting(unsigned long gr[],int N);
int pos=0;
int main()
{
int T;
cin>>T;
unsigned long earnings[T];
for(int i=0;i<T;i++)
{
earnings[i]=0;
}
for(int i=0;i<T;i++)
{
long R,K;
int N;
cin>>R>>K>>N;
unsigned long g[N];
for(int j=0;j<N;j++)
include<iostream>
using namespace std;
unsigned long earning(unsigned long gr[],long K,int N);
void shifting(unsigned long gr[],int N);
int pos=0;
int main()
{
int T;
cin>>T;
unsigned long earnings[T];
for(int i=0;i<T;i++)
{
earnings[i]=0;
}
for(int i=0;i<T;i++)
{
long R,K;
int N;
cin>>R>>K>>N;
unsigned long g[N];
for(int j=0;j<N;j++)
{
cin>>g[j];
}
for(int j=0;j<R;j++)
{
earnings[i]=earnings[i]+earning(g,K,N);
shifting(g,N);
}
}
for(int i=0;i<T;i++)
{
cout<<"Case#"<<(i+1)<<": "<<earnings[i]<<endl;
}
return 0;
}
unsigned long earning(unsigned long gr[],long K,int N)
{
unsigned long sum=0;
int i=0;
while(sum<=K && i<N)
{
sum=sum+gr[i];
i++;
}
if(sum>K)
{
sum=sum-gr[i-1];
i--;
}
if(i>=N)
{
i--;
}
pos=i;
return sum;
}
void shifting(unsigned long gr[],int N)
{
int fill=pos;
unsigned long shift[N];
if(pos<N)
{
for(int i=0;i<(N-pos);i++)
{
shift[i]=gr[fill];
fill++;
}
int flag=0;
for(int i=(N-pos);i<N;i++)
{
shift[i]=gr[flag];
flag++;
}
for(int i=0;i<N;i++)
cout<<shift[i]<<" ";
cout<<endl;
for(int i=0;i<N;i++)
gr[i]=shift[i];
}
}