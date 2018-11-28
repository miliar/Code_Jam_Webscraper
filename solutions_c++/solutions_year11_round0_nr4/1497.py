
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <stack>
#include <cmath>
#include <iomanip>
#define LL long long
using namespace std;
/*
int main()
{int t,j,i,c,d,n;
freopen("D-small-attempt0.in","r",stdin);
freopen("out.txt","w",stdout);
cin>>t;
int mp1[200][200],mp2[200],arr[100],t2;

for(j=0;j<t;j++)
{char c1,c2,c3;
    cin>>c;
    memset(mp1,0,sizeof(mp1));memset(mp2,0,sizeof(mp2));memset(arr,0,sizeof(arr));
for(int m=0;m<c;m++)
{
cin>>c1>>c2>>c3;
mp1[(int)c1][(int)c2]=(int)c3;mp1[(int)c2][(int)c1]=(int)c3;
}
cin>>d;
for(int m=0;m<d;m++)
{
    cin>>c1>>c2;
mp2[(int)c1]=(int)c2;mp2[(int)c2]=(int)c1;
}
cin>>n;cin>>c1;//cout<<c1<<"pushed in"<<endl;
arr[0]=c1;int t1=n;
for(int m=1;m<t1;m++)
{
    cin>>c1;//taking one by one
  //  cout<<c1<<"received"<<endl;
 if(mp1[arr[m-1]][c1])
{arr[m-1]=mp1[arr[m-1]][c1];m--;t1--;continue;
}//in case of combination

else if(mp2[c1] )
{
    for(i=0;i<t1;i++)
    if(arr[i]==mp2[c1])
    {t2=arr[i];
     memset(arr,0,sizeof(arr));if(m==t1-1)break; else {cin>>c1;arr[++m]=c1;continue;}
    }
if(t2==mp2[c1] && m==t1-1)break;
}//in case of possible destructor




arr[m]=c1;
cout<<c1<<"pushed in"<<endl;
}//for m


cout<<"Case #"<<j+1<<": "<<"[";
int flag=0;
for(i=0;i<n;i++)
if(arr[i])
{
    if(flag==0)
{cout<<(char)arr[i];flag=1;}
else
cout<<", "<<(char)arr[i];
}//print
cout<<"]"<<endl;
}//for t

return 0;
}
*/
#include<iostream>
using namespace std;
typedef long long int64;

int main(){
freopen("D-large.in","r",stdin);
freopen("out.txt","w",stdout);
    int64 t,n,i,j,k,r;
    cin>>t;
    for(i=1;i<=t;i++){
        cin>>n; r=0;
        for(j=1;j<=n;j++){ cin>>k; if(k!=j) r++; }
        cout<<"Case #"<<i<<": "<<r<<".000000\n";
        }
    return 0;
}
