#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int test;
    cin>>test;
    while(test--)
    {
    long long int a,b,i,pow=1,ans=0;
    cin>>a>>b;
    int digits=0,temp,check,cur;
    while(a)
    {
     digits++;
     a/=10;
     pow=pow*10;
    }
    check=b/(pow/10);
    for(i=a;i<=b;i++)
    {
     while(i)
     {
      
     }
    }
    }
    return 0;
}
