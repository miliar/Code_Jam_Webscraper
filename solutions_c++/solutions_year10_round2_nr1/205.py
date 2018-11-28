#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <set>
#include <iostream>
using namespace std;
const int maxn = 300;
string oldStr[maxn],newStr[maxn];

set <string> S;


void insert(string s)
{
    int l = s.length();
    string tmp = "/";
    for (int i = 1; i < l; ++i)
    {
        if (s[i] == '/')
        {
            S.insert(tmp);
    //        cout<<"insert"<<tmp<<endl;
        }
        tmp += s[i];
    }
    S.insert(tmp);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int Test = 1; Test <= T; ++Test)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        S.clear();
        for (int i = 1; i <= n; ++i)
        {
            cin>>oldStr[i];
            insert(oldStr[i]);
        }
        for (int i = 1; i <= m; ++i)
            cin>>newStr[i];
        sort(newStr+1,newStr+m+1);
        int ans = 0;
        for (int i = 1; i <= m; ++i)
        {
            string tmp = "/";
            int l = newStr[i].length();
            for (int j = 1; j < l; ++j)
            {
                if (newStr[i][j] == '/') 
                {
                    if (S.count(tmp)== 0)
                    {
                        ans ++;
                        S.insert(tmp);
                  //      cout<<"new"<<tmp<<endl;
                    }
                }
                tmp += newStr[i][j];
            }
            if (S.count(tmp) == 0)
            {
                ans ++;
                S.insert(tmp);
             //   cout<<"new"<<tmp<<endl;
            }
        }
        printf("Case #%d: %d\n",Test,ans);
    
    }
    return 0;
}
