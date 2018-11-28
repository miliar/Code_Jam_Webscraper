// gcj A1.cpp
#include<iostream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cctype>
#include<climits>
#include<cfloat>

using namespace std;

vector<string> deserialize(string s);
map< vector<string>, bool> mv;
int main()
{
    int T;
    scanf("%d", &T);
    for(int c = 1; c <= T; c++)
    {
        mv.clear();
        int a, b;
        scanf("%d%d", &a, &b);
        for(int i = 0; i < a; i++)
        {
            string tmp;
            cin >> tmp;
            mv[deserialize(tmp)] = 1;
        }
        int t = 0;
        for(int i = 0; i < b; i++)
        {
            string tmp;
            cin >> tmp;
            vector<string> vt = deserialize(tmp);
            vector<string> vt1;
            for(int j = 0; j < vt.size(); j++)
            {
                vt1.push_back(vt[j]);
                if(mv.find(vt1) == mv.end())
                {
                    mv[vt1] = 1;
                    t++;
                }
            }
        }
        printf("Case #%d: %d\n", c, t);
    }
    return 0;
}


vector<string> deserialize(string s)
{
    vector<string> t;
    string q;
    for(int i = 1; i < s.size(); i++)
    {
        if(s[i] == '/')
        {
            t.push_back(q);
            q = "";
        }
        else
            q += s[i];
    }
    t.push_back(q);
    return t;
}
