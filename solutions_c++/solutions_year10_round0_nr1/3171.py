#include<iostream>
#include<string>
using namespace std;
int main()
{
  int n1;
  cin>>n1;
  int n,k;
  for(int i=1;i<=n1;i++)
 {
   cin>>n>>k;
   string str;
   str=(k+1)%(1<<n)?"OFF":"ON";
   cout<<"Case #"<<i<<": "<<str<<endl;
 }
 return 1;
}
