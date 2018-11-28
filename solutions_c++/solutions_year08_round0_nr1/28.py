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
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

using namespace std;

int memo[150][1050];

int n, m;
vector <int> V;

int calc(int k, int a)
{
    if(a==V.size()) return 0;
    
    if(memo[k][a]!=-1) return memo[k][a];
    
    int minN = 1<<30;
    if(V[a]!=k) minN = calc(k, a+1);
    for(int i=0; i<n; i++)
    {
        if(i!=k)
        {
            minN = min(minN, 1 + calc(i, a+1));
        }
    }
    
    memo[k][a] = minN;
    return minN;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int N;
    cin>>N;
    
    for(int caso=0; caso<N; caso++)
    {
        memset(memo, -1, sizeof(memo));
        
        cin>>n;
        
        string s;
        getline(cin, s);
        
        map <string, int> M;
        
        for(int i=0; i<n; i++)
        {
            getline(cin, s);
            M[s] = i;
        }
        
        V.clear();
        
        cin>>m;
        
        getline(cin, s);
        
        for(int i=0; i<m; i++)
        {
            getline(cin, s);
            V.push_back(M[s]);
        }
        
        int minN = 1<<30;
        for(int i=0; i<n; i++)
            minN = min(minN, calc(i, 0));
        cout<<"Case #"<<caso+1<<": "<<minN<<endl;
    }
    
    return 0;
}

