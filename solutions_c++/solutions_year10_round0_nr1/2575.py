#include<vector>
#include<iostream>
#include<iomanip>
#include<set>
#include<string>
#include<map>
#include<algorithm>
#include<cassert>
#include<cstdio>
#include<cstdlib>
#include<cmath>

using namespace std;
#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back
#define mp make_pair
long long unsigned powe(int a,int b){
     long long unsigned ret=1;
     for(long long  unsigned i=0;i<b;i++)
     ret*=a;
     return ret;
}     
int main()
{  freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
   int t;
   int  n;
   long long unsigned m;
   cin>>t;
  
   
    
    for(int i=1;i<=t;i++)
    {       bool boo=false;
            cin>>n>>m;
            if((m+1)%powe(2,n))
            boo=false;
            else
            boo=true;
           
                         
            if(boo)        
            cout<<"Case #"<<i<<": ON"<<endl;
            else
            cout<<"Case #"<<i<<": OFF"<<endl;
    }
                                   
    
    
    return 0;
}                    
                    
                    
