#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <stack>

using namespace std;

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("in", "rt", stdin);
        freopen("out", "wt", stdout);
    #endif
    int testCount;
    cin >> testCount;
    for (int t = 1; t <= testCount; ++t)
    {
        vector< vector<char> > combineTable(256, vector<char>(256, 0));
        int c;
        cin >> c;
        while (c--)
        {
            string cs;
            cin >> cs;
            combineTable[cs[0]][cs[1]] = combineTable[cs[1]][cs[0]] = cs[2];
        }
        vector< vector<bool> > opposedTable(256, vector<bool>(256, false));
        int d;
        cin >> d;
        while (d--)
        {
            string os;
            cin >> os;
            opposedTable[os[0]][os[1]] = opposedTable[os[1]][os[0]] = true;
        }
        vector<char> st;
        int n;
        string elementList;
        cin >> n >> elementList;
        for (int i = 0; i < n; ++i)
        {
            char element = elementList[i];
            if (st.size() == 0)
            {
                st.push_back(element);
                continue;
            }
            char prevElement = st[st.size() - 1];
            char combinedElement = combineTable[prevElement][element];
            if (combinedElement != 0)
            {
                st.pop_back();
                st.push_back(combinedElement);
            } else
            {
                bool needClear = false;
                for (int j = 0; j < (int)st.size(); ++j)
                    if (opposedTable[st[j]][element])
                    {
                        needClear = true;
                        break;
                    }
                if (needClear)
                    st.clear();
                else
                    st.push_back(element);
            } 
        }
        printf("Case #%d: [", t);
        for (int i = 0; i < (int)st.size() - 1; ++i)
            printf("%c, ", st[i]);
        if ((int)st.size() > 0)
            printf("%c", st[(int)st.size() - 1]);
        printf("]\n");
    }
    return 0;
}
