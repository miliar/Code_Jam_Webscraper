#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>

#define SZ(a) (int)(a).size()
#define PB push_back
#define ALL(a) (a).begin(),(a).end()
#define INF (int)1e9
#define vi vector<int>
#define vs vector<string>

using namespace std;


int main()
{
    int test;
    cin >> test;

    for(int cas = 0; cas < test; cas++)
    {
       int L, N, C;
       long long t;
       cin >> L >> t >> N >> C;
       //if(cas + 1 > 23)
       // cout << L << " " << t << " " << N << " " << C << endl;
       
       int ai[1005], dist[1000005];
       
       for(int i = 0; i < C; i++)
       {
            cin >> ai[i];    
           // if(cas + 1 > 23)
                //cout << ai[i] << " ";
        }
        //cout << endl;
        
       long long total = 0;
       for(int i = 0; i < N; i++)
       {
           dist[i] = ai[i % C];
           total += dist[i];
           //cout << dist[i] << endl;
       }
            
        long long d1 = t / 2;
        long long d2 = 0;
        long long ans = 0;
        if(total <= d1)
        {
            ans = total * 2;
        }
        else
        {
            int star = 0;
            long long travel = 0;
            while(travel < d1)
            {
                travel += dist[star];
                star++;
            }
            
            vi newdist;
            if(travel > d1)
                newdist.PB(travel - d1);
            for(int i = star; i < N; i++)
                newdist.PB(dist[i]);
                
            sort(ALL(newdist));
            reverse(ALL(newdist));
            
            int idx = 0;
            while(idx < L && idx < SZ(newdist))
            {
                d2 += newdist[idx];
                idx++;
            }
            
            while(idx < SZ(newdist))
            {
                d1 += newdist[idx];
                idx++;
            }
            
            ans = (d1 * 2 + d2);
        }
        
        cout << "Case #" << cas + 1 << ": "<< ans << endl;
        
       
    }
    return 0;
}
