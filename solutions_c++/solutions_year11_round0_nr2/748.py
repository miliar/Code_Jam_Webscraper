#include <iostream>
#include <cstdio>
#include <map>
#include <set>
using namespace std;

int C, D, N;

map< pair<char, char>, char > combined;
set< pair<char, char> > opposed;

int last;
char coms[128], res[128];

void solve()
{     
    last = 0;
    for (int i = 0; i < N; i++)
    {
        if (last == 0)
        {            
            res[last] = coms[i];     
            last++;
            continue;
        }
        
        char prev = res[last - 1];
        char curr = coms[i];
        
        pair<char, char> charPair = make_pair(prev, curr);
        if (combined.count(charPair)) 
        {
           res[last - 1] = combined[charPair];
           continue;
        }
        
        bool cleared = false;
        for (int j = 0; j < last; j++)
        {
           charPair = make_pair(res[j], curr);
           if (opposed.count(charPair))
           {
               last = 0;
               cleared = true;
               break;
           }
        }
        
        if (cleared) continue;
        
        res[last] = coms[i];
        last++;
    }                       
}

int main()
{
    int T; cin >> T;
    for (int t = 1; t <= T; t++)
    {
        combined.clear();
        opposed.clear();
        
        cin >> C;
        for (int i = 0; i < C; i++)
        {
            char a1, a2, a3;        
            cin >> a1 >> a2 >> a3;
            combined[make_pair(a1, a2)] = a3;
            combined[make_pair(a2, a1)] = a3;
        }
        
        cin >> D;
        for (int i = 0; i < D; i++)
        {
            char a1, a2;
            cin >> a1 >> a2;
            opposed.insert(make_pair(a1, a2));
            opposed.insert(make_pair(a2, a1));
        }
        
        cin >> N;
        for (int i = 0; i < N; i++) cin >> coms[i];
        
        solve();
        
        cout << "Case #" << t << ": [";
        for (int i = 0; i < last; i++)
        {
            cout << res[i];
            if (i < last - 1) cout << ", ";
        }
        
        cout << "]" << endl;
    }
    
    return 0;
}
