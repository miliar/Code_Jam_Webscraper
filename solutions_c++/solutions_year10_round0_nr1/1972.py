#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
class snapper
{
 
  public:


 int snap(int n,int k)
{ int i,st,fl=1,p;
vector <int> v;

int *a=new int[n];

k = k%(long long int)(pow(2, n));
 


while(k)
{
 p=k%2;
v.push_back(p);
k/=2;
}

for(i=0;i<v.size();i++)
{
 if(!v[i])
 {fl=0;
 break;
 }
}


if(fl && v.size()==n)
return 1;

else
 return 0;

}




};

int main()
{

 snapper ob;
int t,n,k,i=1;
int s;
char *a;
a=new char[3];
a[0]=NULL;
vector <int> state;
cin>>t;
while(i<=t)
{
cin>>n;
cin>>k;
s=ob.snap(n,k);
state.push_back(s);
i++;
}

for(i=0;i<state.size();i++)
{
 if(state[i]==1)
 strcpy(a,"ON");
 else 
  strcpy(a,"OFF"); 
 
cout<<"Case #"<<i+1<<": "<<a<<"\n";
}
return 0;
}



