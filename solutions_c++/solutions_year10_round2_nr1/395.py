#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>   
using namespace std;

int N, M;
set <string> exist, want;

int solve()
{
    int res = 0;
    
    set<string>::iterator p = want.begin();
    
    while (p != want.end())
    {
       string path = *p;   
          
       if (exist.count(path))
       {
       }
       else
       {
           res++;
           exist.insert(path);
       }                   
          
       p++;   
    }
    
    return res;
}

int main()
{
    int T;
    cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        cin >> N >> M;
        
        exist.clear();
        want.clear();
        
        for (int i = 0; i < N; i++)
        {
            string s;
            cin >> s;
            
            s += "/";
            
            for (int j = 1; j < s.size(); j++)
                if (s[j] == '/')
                   exist.insert(s.substr(0, j));
        }
            
        for (int i = 0; i < M; i++)
        {
            string s;
            cin >> s;
            
            s += "/";
            
            for (int j = 1; j < s.size(); j++)
                if (s[j] == '/')
                   want.insert(s.substr(0, j));
        }
        
        cout << "Case #" << t << ": " << solve() << endl;
    }
    
    return 0;
}
