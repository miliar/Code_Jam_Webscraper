#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <iterator>
#include <algorithm>
#include <functional>
#include <numeric>
#include <iomanip>

#include <cstdio>
#include <cstdlib>
#include <cstddef>
#include <cmath>
#include <cctype>
#include <ctime>

using namespace std;

typedef struct _dirrec
{
    string me;
    vector <struct _dirrec> child;
} dirrec;

int main(int argc, char *argv[])
{
    char bufline[10240];
    fgets(bufline, 10240, stdin);
    int ncase;
    sscanf(bufline, "%d", &ncase);
    for (int icase = 1; icase <= ncase; icase++)
    {
        fgets(bufline, 10240, stdin);
        int n,m;
        sscanf(bufline, "%d%d", &n, &m);
        dirrec root;
        root.me = "";
        for (int i = 0; i < n; i++)
        {
            fgets(bufline, 10240, stdin);
            dirrec *dp = &root;
            char *p = strtok(bufline, " \r\n\t/");
            while (p)
            {
                int j = 0;
                for (j = 0; j < dp->child.size(); j++)
                    if (dp->child[j].me == p)
                        break;
                dirrec t;
                t.me = p;
                if (j == dp->child.size())
                    dp->child.push_back(t);
                dp = &dp->child[j];
                p = strtok(NULL, " \r\n\t/");
            }
        }
        int ret = 0;
        for (int i = 0; i < m; i++)
        {
            fgets(bufline, 10240, stdin);
            dirrec *dp = &root;
            char *p = strtok(bufline, " \r\n\t/");
            while (p)
            {
                int j = 0;
                for (j = 0; j < dp->child.size(); j++)
                    if (dp->child[j].me == p)
                        break;
                dirrec t;
                t.me = p;
                if (j == dp->child.size())
                {
                    dp->child.push_back(t);
                    ret++;
                }
                dp = &dp->child[j];
                p = strtok(NULL, " \r\n\t/");
            }
        }
        printf("Case #%d: %d\n", icase, ret);
    }
    return 0;
}
