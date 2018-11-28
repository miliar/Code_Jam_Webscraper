#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

bool comp(pair<int, int> a, pair<int, int> b)
{
    return a.second > b.second;
}

FILE* out = fopen("output.txt", "w");

void go(int x)
{
    int ans=0;
    int n, s, p, m;
    vector< pair<int, int> > v;

    scanf("%d %d %d", &n, &s, &p);
    int visited[n];
    for(int i = 0; i < n; ++i)
        visited[i] = false;

    for(int i = 0; i < n; ++i)
    {
        scanf("%d", &m);
        int temp = m/3;

        if(m == 0 or m == 1)
            v.push_back(make_pair(m, m));
        else if(m == 2)
            v.push_back(make_pair(1, 2));
        else
        {
            if(m % 3 == 0)
            {
                v.push_back(make_pair(temp, temp+1));
            }
            else if(m % 3 == 1)
            {
                v.push_back(make_pair(temp+1, temp+1));
            }
            else if(m % 3 == 2)
            {
                v.push_back(make_pair(temp+1, temp+2));
            }
        }

    }

    sort(v.begin(), v.end(), comp);

    for(int i = 0; i < v.size(); ++i)
    {
        if(v[i].first >= p)
        {
            ++ans;
            visited[i] = true;
        }
    }

    for(int i = 0; i < v.size(); ++i)
    {
        if(s == 0)
            break;
        if(!visited[i])
        {
            --s;
            if(v[i].second >= p)
                ++ans;
        }
    }

    fprintf(out, "Case #%d: %d\n", x, ans);

}

int main()
{
    int t;
    cin >> t;

    for(int i = 1; i <= t; ++i)
        go(i);

    return 0;
}
