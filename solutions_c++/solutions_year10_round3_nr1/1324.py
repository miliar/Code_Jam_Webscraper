using namespace std;

#include<iostream>

int main()
{
    
int T=0;
cin>> T;
int r=1;
while(T--)
{
        
          int N;
          cin>>N;
          
          long A[N],B[N];
          for(int i=0;i<N;i++)
          cin>>A[i]>>B[i];
          int count=0;
          
for(int i=0;i<N;i++)
{
for(int j=0;j<N;j++)
{
if(i==j) continue;
if(A[i]>A[j] && B[i]<B[j]) count++;
else if(A[i]<A[j] && B[i]>B[j]) count++;
}
}

count=count/2;

cout<<"Case #"<<r++<<": "<<count<<endl;
}


}




