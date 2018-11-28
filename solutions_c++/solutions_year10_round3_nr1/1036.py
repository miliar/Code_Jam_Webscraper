#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<numeric>
using namespace std;
class abc
{
  
   public:
   int func(vector <int> v1,vector <int> v2)
{

   int i,c=0,j,k;
 for(i=0;i<v1.size() && i<v2.size();i++)
{
for(k=i+1;k<v1.size() && k<v2.size();k++)
{
 if(v1[i]<v1[k] && v2[i]>v2[k])
  c++;
if(v1[i]>v1[k] && v2[i]<v2[k])
c++;
}

}

return c;
 



}

};

int main()
{

 abc  ob;
int T;

vector <int> v;
vector <int> v1;
vector <int> v2;
int a,b;

int i=1,r,j,n;
cin>>T;

while(i<=T)
{

cin>>n;
for(j=1;j<=n;j++)
{
cin>>a>>b;
 v1.push_back(a);
 v2.push_back(b);
}



r=ob.func(v1,v2);
v1.erase(v1.begin(),v1.end());
v2.erase(v2.begin(),v2.end());

v.push_back(r);

i++;
}

for(i=0;i<v.size();i++)
{
 cout<<"Case #"<<i+1<<": "<<v[i]<<endl;
}

return 0;
}
