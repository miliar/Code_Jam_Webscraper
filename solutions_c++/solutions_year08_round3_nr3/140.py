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
vector<long long int> values;
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
 
/*T dp_result(vector<int> values, int maxk)
{
   dp[0][1]=1;
   T ret=0;
   for(int i=1;i<values.size();i++) {
     dp[i][1]=1;
     for(int k=2;k<=maxk;k++) {
      for(int j=0;j<i;j++) {
         if(values[j]<values[i]) {
            dp[i][k]+=dp[j][k-1];
         }
      }
     }
     ret+=dp[i][maxk];
   }
   return ret;
}
*/
int main()
{
 
    int test,c=1;
cin>>test;
while(test--)
{
	
	memset(cumBIT,0,sizeof(cumBIT));
    long long int i,n,k,m,x,y,z,A[1001];
    cin>>n>>m>>x>>y>>z;
    values=vector<long long int>(n,0);
    for(i=0;i<m;i++)
    cin>>A[i];
     for(int i=0;i<n;i++) {
     values[i]=A[i%m];
     A[i%m]=(x*A[i%m] + y*(i+1))%z;
    }
    vector<long long int> temp=values;
 
    sort(values.begin(),values.end());
    mapIndex[values[0]]=1;
    for(i=1;i<n;i++) {
       if(values[i]!=values[i-1]) {
         mapIndex[values[i]]=i+1;
       }
    }
 
    values=temp;
    T ret = 0;
    for(i=0;i<n;i++) {
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
    cout<<"Case #"<<c<<": "<<ret<<endl;
    c++;
 //   cin>>ret; 
	values.clear();
}
}
