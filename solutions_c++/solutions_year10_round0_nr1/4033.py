#include<iostream>
using namespace std;

int main()
{
 int C;
 cin>>C;
 long long N,K;
 long long a,b;
 for(int X=1;X<=C;X++)
           {
           cin>>N>>K; 
           cout<<"Case #"<<X<<": ";
           a=K+1;
           b=(1<<N);
           if( (a%b)== 0 )  cout<<"ON"<<endl;
           else cout<<"OFF"<<endl;
           }   
    return 0;
}
