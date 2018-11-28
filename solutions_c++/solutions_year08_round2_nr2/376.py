
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
using namespace std;
bool isp(int n)
{
     for(int i = 2; i <= sqrt(n); i++)
             if( n % i == 0) return false;
     return true;    
}
vector<int> g;
int getg(int n)
{
    return g[n] == n ? n : g[n] = getg(g[n]);    
}
int main()
{
    int cases;
    cin >> cases;
    int cnt = 1;
    while(cases--)
    {
        int a, b, p;
        cin >> a >> b >> p;
        
        g.clear();
        g.resize(b+1, -1);
        for(int i = a; i <=b ; i++)
                g[i] = i;
        //cout<<endl<<endl;
        //tr(g, itr) cout<<*itr<<" ";
        
        for(int i = p; i <= b; i++)
        {
            if(isp(i))
            {
                vector<int> t;
                for(int j = a; j <= b; j++)
                {
                    if(j % i == 0)
                        t.pb(j);
                }          
                if(sz(t) <= 1) continue;
                
                for(int k = 1; k < sz(t); k++)
                {
                    //vector<int> tt;
                    for(int x = a; x <= b; x++)
                        if(getg(x) == getg(t[k]))
                            g[x] = getg(t[0]);        
                }
                //cout<<endl<<endl;
                //tr(g, itr) cout<<*itr<<" ";
                
            }    
        } 
        set<int> ttt;
        for(int i = a; i <= b; i++)
                ttt.insert(g[i]);
        cout<<"Case #"<<cnt<<": "<<sz(ttt)<<endl;
        cnt++;
    }
    return 0;
}

