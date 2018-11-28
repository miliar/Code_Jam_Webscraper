#include <iostream>
#include <vector>
#include <string>
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

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define eps 1e-8
#define pi acos(-1)

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
        
    int nCasos;
    cin>>nCasos;
    
    for(int caso=1; caso<=nCasos; caso++)
    {
        int N;
        cin>>N;
        
        vector <int> v(N);
        
        for(int i=0; i<N; i++)
        {
            string s;
            cin>>s;
            for(int j=0; j<N; j++)
                if(s[j]=='1') v[i] = j;
        }
        
        int x = 0;
        vector <int> ok(N, 1);
        
        for(int k=0; k<N; k++)
        {
            int cnt = 0;
            for(int i=0; i<N; i++)
            {
                if(ok[i]) cnt++;
                
                if(v[i] <= k && ok[i])
                {
                    x += cnt - 1;
                    ok[i] = 0;
                    break;
                }
            }
        }
        cout<<"Case #"<<caso<<": "<<x<<endl;
    }

    return 0;
}
