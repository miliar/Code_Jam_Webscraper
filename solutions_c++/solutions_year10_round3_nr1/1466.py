#include<iostream>

using namespace std;

void main()
{
int T, point,A[1024],B[1024],N;

freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);


cin>>T;

for(int i=0;i<T;i++)
{
cin>>N;
point =0;
for(int j=0;j<N;j++)
cin>>A[j]>>B[j];

for(j=0;j<N-1;j++)
{
if(A[0]<A[j+1] && B[0]>B[j+1])
point++;
if(A[0]>A[j+1] && B[0]<B[j+1])
point++;
}

cout<<"Case #"<<i+1<<": "<<point<<endl;

}
}