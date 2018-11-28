#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

class w
{
public:
    char ori[12];
    char mark[12];
    char contain[30];
    int point;
    int x;
    bool operator < (const w &r) const
    {
        return strcmp(mark, r.mark) < 0;
    }
    void reset()
    {
        int len = strlen(ori);
        memset(mark, '_', len);
        mark[len] = '\0';
        memset(contain, 0, 30);
        for (int i = 0; i < len; i++)
            contain[ori[i]-'a'] = 1;
        point = 0;
    }
    void markwith(char a)
    {
        int len = strlen(ori);
        for (int i = 0; i < len; i++)
        {
            if (ori[i] == a)mark[i] = a;
        }
    }
};

vector<w> dict;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int ti = 1; ti <= tc; ti++)
    {
        printf("Case #%d: ", ti);
        int n, m;
        scanf("%d%d", &n, &m);
        w w1;
        dict.clear();
        for (int i = 0; i < n; i++)
        {
            scanf("%s", w1.ori);
            w1.x = i;
            dict.push_back(w1);
        }
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
                dict[j].reset();
            char g[30];
            scanf("%s", g);
            int l = strlen(g);
            for (int j = 0; j < l; j++)
            {
                //printf("j %d\n",j);
                sort(dict.begin(), dict.end());
                int s = 0, t = 0;
                while (s < n)
                {
                    while (t < n && !strcmp(dict[s].mark, dict[t].mark))t++;
                    int k;
                    for (k = s; k < t && !dict[k].contain[g[j]-'a']; k++);
                    if (k < t)
                    {
                        //printf("%d %c %s\n", t-s, g[j], dict[s].mark);
                        for (int kk = s; kk < t; kk++)
                        {
                            if (!dict[kk].contain[g[j]-'a'])
                                dict[kk].point++;
                            dict[kk].markwith(g[j]);
                        }
                    }
                    s = t;
                }
            }
            int d = 0;
            for (int j = 0; j < dict.size(); j++)
            {
                if (dict[j].point > dict[d].point || (dict[j].point == dict[d].point && dict[j].x < dict[d].x))d = j;
                //printf("%s %s %d\n", dict[j].ori, dict[j].mark, dict[j].point);
            }
            printf("%s ", dict[d].ori);
            //printf("ans %s\n", dict[d].ori);
        }
        printf("\n");
    }
    return 0;

}
