#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <list>
#include <cstdio>
#include <complex>
#include <stack>
#include <cctype>
#include <cstdlib>
#include <iostream>
#include <cstring>

#define X real()
#define Y imag()
#define PB push_back
#define MP make_pair
#define FR(i,n) for( long long i = 0; i < n; i ++ )
#define FOR(i,a,n) for(long long i = a; i < n; i ++)
#define FREACH(it,v) for( typeof(v.end()) it = v.begin(); it != v.end(); it ++ )
#define EPS 1e-9
using namespace std;

typedef long double ld;
typedef long long ll;

set<int> vis;

bool isHappy(int n,int base)
{
    vis.clear();
 //   cout << "next calc" << endl;
    while(n!=1)
    {
      //  cout << "n: " << n << endl;
        if(vis.find(n)!=vis.end()) return false;
        vis.insert(n);
        int cur=n;
        int sum=0;
        while(cur>0)
        {
            int rs=(cur%base);
            sum+=rs*rs;
            cur/=base;
        }
        n=sum;
    }
    return true;
}


//bool ok[bs][10000];

int main()
{
    int n;
    cin >> n;
    string s;
    getline(cin,s);
    
    
    FR(i,n)
    {
        getline(cin,s);
        stringstream ss(s);
        bool bses[11];
        memset(bses,false,sizeof(bses));
        int bs;
        while(ss>>bs)
        {
            //cout << "bs: " << bs << endl;
            bses[bs]=true;
            
        }
        int cc=2;
        int res;
        while(true)
        {
         //   cout << cc << endl;
            bool okk=true;
            FR(i,11) if(bses[i]&&!isHappy(cc,i)){
                okk=false;
                break;
            }
            if(okk)
            {
                res=cc;
                break;
            }
            cc++;
        }
        
        
        printf("Case #%d: ",i+1);
        cout << res << endl;
        
    }
}