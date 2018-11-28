#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

void solve(int k)
{
    vector<string> tri;
    vector<string> clear;
    int n; cin >> n;

    for(int i=0;i<n;i++)
    {
        string s; cin >> s;
        tri.push_back(s);
    }

    cin >> n;
    for(int i=0;i<n;i++)
    {
        string s; cin >> s;
        clear.push_back(s);
    }

    string seq;
    cin >> n >> seq;

    vector<char> list;
    for(int i=0;i<n;i++)
    {
        list.push_back(seq[i]);
        if(list.size() > 1)
        {
            char c1 = list[list.size()-1];
            char c2 = list[list.size()-2];

            bool wastri = false;
            for(int j=0;j<tri.size();j++)
            {
                if((c1 == tri[j][0] && c2 == tri[j][1]) || (c1 == tri[j][1] && c2 == tri[j][0]))
                {
                    list.pop_back();
                    list.pop_back();
                    list.push_back(tri[j][2]);
                    wastri = true;
                    break;
                }
            }

            if(!wastri)
            {
                for(int x=0;x<list.size()-1;x++)
                {
                    c2 = list[x];
                    for(int j=0;j<clear.size();j++)
                    {
                        if((c1 == clear[j][0] && c2 == clear[j][1]) || (c1 == clear[j][1] && c2 == clear[j][0]))
                        {
                            list.clear();
                            break;
                        }
                    }
                    if(list.size() == 0)
                        break;
                }
            }
        }

    }

    printf("Case #%d: [", k);
    for(int i=0;i+1 < list.size(); i++)
        printf("%c, ", list[i]);
    if(list.size() > 0)
        printf("%c]\n", list[list.size()-1]);
    else
        printf("]\n");
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

