#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
using namespace std;

const int N = 50;

int n;
string s[N];
int lng[N];
set<vector<int> > have;

bool check(vector<int> v)
{
    for(int i = 0; i < n; i++)
    {
        if(lng[v[i]] > i) return 0;
    }
    return 1;
}

bool Have(vector<int> v)
{
    return have.count(v);
}

int bfs()
{
    have.clear();
    queue<pair<vector<int>, int> > que;
    vector<int> v;
    for(int i = 0; i < n; i++) v.push_back(i);

    que.push(make_pair(v, 0));
    have.insert(v);

    while(!que.empty())
    {
        v = que.front().first;
        int x = que.front().second;
        que.pop();
        if(check(v))
        {
            return x;
        }
        for(int i = 1; i < n; i++)
        {
            swap(v[i], v[i-1]);
            if(!Have(v))
            {
                que.push(make_pair(v, x+1));
                have.insert(v);
            }
            swap(v[i], v[i-1]);
        }
    }
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin>>T;

    for(int i = 1; i <= T; i++)
    {
        cin>>n;
        for(int j = 0; j < n; j++)
        {
            cin>>s[j];
            int k;
            for(k = n-1; k >= 0; k--)
            {
                if(s[j][k] == '1') break;
            }
            lng[j] = k;
        }

        printf("Case #%d: %d\n", i, bfs());
    }
}
