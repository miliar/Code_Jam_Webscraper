#include <iostream>
#include <stdio.h>
#include <sstream>
#include <cmath>
using namespace std;

int main() {
int test;
freopen("C-large.in", "r", stdin);
freopen("o1.txt", "w", stdout);
cin>>test;
for(int i=1;i<=test;i++)
{
cout<<"Case #"<<i<<": ";
unsigned long int a,b;
int res=0;
cin>>a>>b;
for(int j=a;j<=b;j++)
{
int t=1;
int tmp=j;
while(tmp/10!=0){t++;tmp/=10;}
tmp=j;
do{
tmp=(tmp%10)*pow(10,t-1)+tmp/10;
if(tmp<=b && tmp>=a && tmp!=j) res++;}while(tmp!=j);
}
cout<<res/2<<endl;
}
	return 0;
}
