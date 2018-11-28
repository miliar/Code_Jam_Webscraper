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
    int T;
    cin >> T;

    for(int t = 0; t < T; t++)
    {
        int N;
        cin >> N;
        
        char ip[N + 1][N + 1];
        for(int i = 0; i < N; i++)
            cin >> ip[i];
            
        double wp[N], owp[N], oowp[N];
        
        for(int i = 0; i < N; i++)
        {
            int denom = 0, win = 0;
            for(int j = 0; j < N; j++)
            {
                if(ip[i][j] != '.')
                {
                    denom++;
                    if(ip[i][j] == '1')
                        win++;
                }
            }
            wp[i] = (double)win / denom;
          //  cout << wp[i] << endl;
        }
        
        for(int i = 0; i < N; i++)
        {
            vi opp;
            for(int j = 0; j < N; j++)
            {
                if(ip[i][j] != '.')
                    opp.PB(j);
            }
            
            vector <double> oppwp;
            for(int j = 0; j < SZ(opp); j++)
            {
                int denom = 0, win = 0;
                for(int k = 0; k < N; k++)
                {
                    if(k == i)
                        continue;
                    if(ip[opp[j]][k] != '.')
                    {
                        denom++;
                        if(ip[opp[j]][k] == '1')
                            win++;
                    }
                }
                oppwp.PB((double)win / denom);
                //cout << "a " << oppwp[j] << endl;
            }
            owp[i] = accumulate(ALL(oppwp), 0.0) / (double)SZ(opp);
            //cout << owp[i] << endl;
        }
        
         
        for(int i = 0; i < N; i++)
        {
            double tot = 0;
            int denom = 0;
            for(int j = 0; j < N; j++)
            {
                if(ip[i][j] != '.')
                {
                    tot += owp[j];
                    denom++;
                }
            }
            oowp[i] = tot / denom;
         }
         
         cout << "Case #" << t + 1 << ":" << endl;
         for(int i = 0; i < N; i++)
         {
             cout << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
         }
        
    }
    return 0;
}
