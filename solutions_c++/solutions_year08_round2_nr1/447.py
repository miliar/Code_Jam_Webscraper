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

int main()
{
    int cases;
    cin >> cases;
    int cnt = 1;
    int n;
    long long a, b, c, d, x, y, m;
    vector<long long> xx, yy;
    while(cases--)
    {
        xx.clear();
        yy.clear();          
        int ans = 0;
        cin >> n;
        cin >> a >> b >> c >> d >> x >> y >> m;
        xx.pb(x);
        yy.pb(y);
        for(int i = 0; i < n-1; i++)
        {
            x =  (a * x + b) % m ;          
            xx.pb(x);
            y = (c * y + d ) % m;
            yy.pb(y);
        }
        vector<bool> valid(n, true);
        //r(int i = 0; i < n;i++)
        //        cout<<endl<<xx[i]<<" "<<yy[i];
        for(int i =0; i < sz(xx)-2; i++)
        {
            for(int j = i+1; j < sz(xx)-1; j++)
            {
                for(int k = j+1; k < sz(xx); k++)
                {
                   if( ((xx[i] + xx[j] + xx[k]) % 3 == 0) && ((yy[i] + yy[j] + yy[k]) % 3 == 0))                
                   {
                       ans++;
                   }
                        
                      
                }
            }
        }
        cout<<"Case #"<<cnt<<": "<<ans<<endl;
        cnt++;
    }
    return 0;
}

