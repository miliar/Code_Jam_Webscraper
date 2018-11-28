#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <sstream>
using namespace std;
const char* table = "QWERASDF";
map<string, string> strMap;
int fob[8][8] = {0};
int find(char ch)
{
    for(int i = 0;i < 8;i++) if(table[i] == ch) return i;
    return -1;
}
bool find_t(string &now)
{
    for(map<string,string>::iterator iter = strMap.begin();iter != strMap.end();iter++)
    {
        int index = now.find(iter->first);
        if(index != string::npos)
        {
            now.replace(index, iter->first.size(), iter->second);
            return true;
        }
    }
    return false;
}
void get(int cases, string str)
{
    string now = "";
    for(string::iterator ch = str.begin();ch != str.end();ch++)
    {
        now += *ch;
        while(find_t(now));
        int i = find(*now.rbegin());
        for(string::iterator j = now.begin();j != now.end() && i != -1;j++)
        {
            int k = find(*j);
            if(k != -1 && fob[k][i])
            {
                now = "";
                break;
            }
        }
    }
    printf("Case #%d: [", cases);
    for(string::iterator iter = now.begin();iter != now.end();iter++)
        if(iter == now.begin()) printf("%c", *iter);
        else printf(", %c", *iter);
    printf("]\n");
}
int main()
{
    int t;
    freopen("data.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    cin >> t;
    for(int j = 1;j <= t;j++)
    {
        int c, d, n;
        cin >> c;
        strMap.clear();
        memset(fob, 0, sizeof(fob));
        string str;
        for(int i = 0;i < c;i++)
        {
            cin >> str;
            string sub = str.substr(0, 2);
            strMap[sub] = str.substr(2, 1);
            reverse(sub.begin(), sub.end());
            strMap[sub] = str.substr(2, 1);
        }
        scanf("%d", &d);
        for(int i = 0;i < d;i++)
        {
            cin >> str;
            int a = find(str[0]), b = find(str[1]);
            fob[a][b] = fob[b][a] = 1;
        }
        scanf("%d", &n);
        cin >> str;
        get(j, str);

    }
    return 0;
}
