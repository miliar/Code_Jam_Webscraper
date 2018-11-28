#include <iostream> 
#include <vector>
#include <string>
#include <string.h>
#include <algorithm> 
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cfloat>
#include <bitset> 

using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
int mod=10000;
string quiero;
string cad;
int N,M;
int memo[20][503];

int funcion(int a,int b)
{

    if(a==M&&b==N)
    {
        return 1;
    }
    if(b==N)
    return 0;
    
    if(memo[a][b]!=-1)
    return memo[a][b];
    int res=0;
    
    if(quiero[a]==cad[b])
    {
        res+=(funcion(a+1,b+1)%mod);
        res%=mod;
    }
    res+=(funcion(a,b+1)%mod);
    res%=mod;
    memo[a][b]=res;
    return res;
}
int tonum(string cad)
{
    int res;
    stringstream is(cad);
    is>>res;
    return res;
}
int main()
{

    int n;
   quiero="welcome to code jam";
           
   getline(cin,cad);
   n=tonum(cad);
   M=quiero.size();
    for(int ii=0;ii<n;ii++)
    {
        getline(cin,cad);
        //cout<<cad<<endl;
        N=cad.size();
        memset(memo,-1,sizeof(memo));
        if(N<M)
        {
        cout<<"Case #"<<ii+1<<": 0000"<<endl;
        continue;
        }
     
        int res=funcion(0,0);
       // cout<<res<<endl;
        cout<<"Case #"<<ii+1<<": ";
        if(res==0)
        {
            cout<<"0000"<<endl;
        }
        else if(res<10)
        {
            cout<<"000"<<res<<endl;
        }
        else if(res<100)
        {
            cout<<"00"<<res<<endl;
        }
        else if(res<1000)
        {
            cout<<"0"<<res<<endl;
        }
        else cout<<res<<endl;
        
    }

return 0;
}
