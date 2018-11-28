#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

queue<pair<int,int> > r1;
queue<pair<int,int> > r2;

void solve(int k)
{
    int n; cin >> n;
    for(int i=0;i<n;i++)
    {
        int tmp; string s;
        cin >> s >> tmp;
        if(s[0] == 'O')
            r1.push(make_pair(i,tmp));
        else
            r2.push(make_pair(i,tmp));
    }

    int cur1, cur2;
    cur1 = cur2 = 1;
    int count = 0;

    while(!r1.empty() || !r2.empty())
    {
        if(r2.empty())
        {
            int res = cur1 - r1.front().second;
            if(res == 0)
                r1.pop();
            else if(res < 0)
                cur1++;
            else
                cur1--;
        }
        else if(r1.empty())
        {
            int res = cur2 - r2.front().second;
            if(res == 0)
                r2.pop();
            else if(res < 0)
                cur2++;
            else
                cur2--;
        }
        else
        {
            int f1 = r1.front().second;
            int f2 = r2.front().second;

            if(r1.front().first < r2.front().first)
            {
                int res = cur1 - f1;
                if(res == 0)
                {
                    r1.pop();
                }
                else if(res < 0)
                    cur1++;
                else
                    cur1--;

                res = cur2 - f2;
                if(res < 0)
                    cur2++;
                else if(res > 0)
                    cur2--;
            }
            else
            {
                int res = cur2 - f2;
                if(res == 0)
                {
                    r2.pop();
                }
                else if(res < 0)
                    cur2++;
                else
                    cur2--;

                res = cur1 - f1;
                if(res < 0)
                    cur1++;
                else if(res > 0)
                    cur1--;
            }
        }
        count++;
    }

    printf("Case #%d: %d\n", k, count);
}

int main()
{
    int n; cin >> n;
    for(int i=0;i<n;i++)
    {
        solve(i+1);
    }
    return 0;
}
