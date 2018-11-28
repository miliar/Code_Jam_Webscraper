#include <iostream>
#include <queue>
#include <set>
#include <string>
#include <sstream>
#include <map>
#define FOR(i,n) for(int i=0;i<n;i++)
#define debln(a) cout << #a << ":" << a <<endl;
using namespace std;

typedef pair<long,long> P;
typedef long long lld;

lld t,r,n,k;
queue<P> q;
lld v[1024];
map<string,lld> used;

string toS(lld x)
{
    ostringstream out;
    out<<x;
    return out.str();
}

int main()
{
    scanf("%d",&t);
    FOR(i,t)
    {
        lld euro=0;
        
        while(!q.empty()) q.pop();
        used.clear();
        
        cin >> r>>k>>n;
        FOR(ff,n) { lld o; cin>>o; q.push(make_pair(o,ff)); }
        vector<lld> iter;
        lld citer = 0;
        FOR(j,r)
        {
            lld ck = k;
            citer=0;
            vector<P> toPush;
            while(ck>0)
            {
                if(q.empty()) break;
                P f = q.front();
                if(ck>=f.first)
                {
                    ck-=f.first;
                    euro+=f.first;
                    citer+=f.first;
                    q.pop();
                    toPush.push_back(f);
                }
                else
                {
                    break;
                }
            }
            
            if(toPush.size()==0) break; // we can't fit this...
            
            string cs = toS(toPush[0].second)+"-"+toS(toPush[toPush.size()-1].second);
            if(used.find(cs) == used.end())
            {
                FOR(t, toPush.size()) q.push(toPush[t]);
                iter.push_back(citer);
                used[cs] = iter.size() - 1;
            }
            else
            {
                lld cycleStart = used[cs];
                lld cycleLength = iter.size() - cycleStart;  
                lld iterCost=0;
                
                for(int ff=cycleStart;ff<iter.size();ff++) iterCost+=iter[ff];
                lld add = (r-cycleStart)/cycleLength;
                euro = add * iterCost;
                
                FOR(ff, cycleStart) euro += iter[ff];
                
                lld nr = r-cycleStart;
                if(nr % cycleLength != 0)
                {
                    lld mod = nr % cycleLength;
                    lld ff = cycleStart;
                    while(mod>0)
                    {
                        euro+=iter[ff];
                        ff++;
                        mod--;
                    }
                }
                
                break;
            }
        }
        cout << "Case #" << i+1 <<": " << euro << endl;
    }
    return 0;
}
