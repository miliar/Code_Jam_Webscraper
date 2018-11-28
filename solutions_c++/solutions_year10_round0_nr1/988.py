#include<string>
#include<vector>
#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream cin("f1.in");
    ofstream cout("f2.out");
    int i,n,j,t,k;
    cin>>t;
    int mark[31];
    mark[0]=0;
    for(i=0;i<=29;i++)
    {
       mark[i+1]=2*mark[i]+1;
    }            
    for(j=1;j<=t;j++)
    {
           cin>>n>>k;          
           cout<<"Case #"<<j<<":"<<" ";
           if((k+1)%(mark[n]+1)==0){cout<<"ON";}
           else{cout<<"OFF";}
           cout<<endl;
    }

}
