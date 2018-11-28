#include<iostream>
#include<string>
using namespace std;
main()
{	

int test,cas=1;
scanf("%d",&test);
while(test--)
{
string a;
cin>>a;
int fl=0;
for(int j=0;j<a.size()-1;j++)
{	
if(a[j+1]>a[j])
{	
fl=1;
break;
}
}
if(fl==0)
{
	a="0"+a;
}
next_permutation(a.begin(),a.end());
cout<<"Case #"<<cas<<": "<<a<<endl;
cas++;
}
}

