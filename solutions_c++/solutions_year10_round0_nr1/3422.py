#include<iostream>
using namespace std;
int main()
{
int l;
cin>>l;
for(int i=1;i<=l;i++)
{
long long int n,k,tmp;
cin>>n>>k;
int lop;
tmp=k;
int fl=1;
while(n!=0)
{
lop=tmp%2;
tmp/=2;

fl=fl&&lop;
//cout<<fl<<"  "<<lop<<endl;
n--;

}
cout<<"Case #"<<i<<": ";
if(fl==0)
cout<<"OFF\n";
else
cout<<"ON\n";

}
return 0;
}
