/* VERY VERY GOOD CODE*/

//Preserve for any BIT problems. First AC on SPOJ under BIT problems. Thanks to nomind and nokia on TC.

#include <iostream>
#include <map>
#include <vector>
using namespace std;
 
const int MAXN = 1001;
const int MAXK = 1001;
const long int BIG=1000000007;
typedef long long T;
 
T cumBIT[MAXK][MAXN+10];
T howMany[MAXK][MAXN+10];
vector<int> values;
map<int,int> mapIndex;
//T dp[MAXN][MAXK];
void update(int idx, int k, int n, T val)
{
    while(idx<n) {
        cumBIT[k][idx]+=val;
        cumBIT[k][idx]=cumBIT[k][idx]%BIG;
        idx+=(idx&-idx);
    }
}
 
T getValue(int idx, int k)
{
   T ret = 0;
   while(idx>0) {
 
      ret+=cumBIT[k][idx];
      ret=ret%BIG;
      idx-=(idx& (-idx));
   }
   return ret%BIG;
}
 
int main()
{
 long long int i,j,nn,mm,x,y,z,k,test,tt,a[200],n;
cin>>test;
for(tt=1;tt<=test;tt++)
{cin>>nn>>mm>>x>>y>>z;
 for(i=0;i<mm;i++)
{cin>>a[i];
}
values=vector<int>(nn,0);
for(i=0;i<nn;i++)
{values[i]=a[i%mm];
a[i%mm]=(x*a[i%mm] + y*(i+1))%z;
}
    memset(cumBIT,0,sizeof(cumBIT));
    int n;n=nn;
    /*for(int i=0;i<n;i++) {
        cin>>values[i];
    }*/
    vector<int> temp=values;
 
    sort(values.begin(),values.end());
    mapIndex[values[0]]=1;
    for(int i=1;i<n;i++) {
       if(values[i]!=values[i-1]) {
         mapIndex[values[i]]=i+1;
       }
    }
 
    values=temp;
    T ret = 0;
    for(int i=0;i<n;i++) {
      int index = mapIndex[values[i]];
      howMany[1][i]=1;
      update(index,1,n,howMany[1][i]);
      for(int j=2;j<=n;j++) {
         howMany[j][i]=getValue(index-1,j-1);
         update(index,j,n,howMany[j][i]);
      }
     for(k=1;k<=n;k++) 
     ret+=howMany[k][i]%BIG;
      ret=ret%BIG;
    }
 
    ret=ret%BIG;
    cout<<"Case #"<<tt<<": "<<ret<<endl;;
}
 //   cin>>ret; 
}
