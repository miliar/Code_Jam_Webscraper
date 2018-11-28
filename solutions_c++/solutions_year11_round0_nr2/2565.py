#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <stdlib.h>
using namespace std;

map<string, string> combine;
map<string, int> opp;
char dest[105];

string ret;

int main()
{


    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, C, D, N;
    char str[4];
    char base[3];
    char target[2];

    base[2] = '\0';
    target[1] = '\0';
    scanf("%d", &T);

    int cnt = 0;

    while(T--)
    {
        cnt ++;
        combine.clear();
        scanf("%d", &C);
        for(int i = 0; i < C; ++ i)
        {
            scanf("%s", str);
            base[0] = str[0]; base[1] = str[1];
            target[0] = str[2];
            combine.insert(make_pair(base, target));
            base[0] = str[1]; base[1] = str[0];
            combine.insert(make_pair(base, target));
        }

        scanf("%d",&D);
        opp.clear();
        for(int i = 0; i < D; ++ i)
        {
            scanf("%s", str);
            opp[str]++;
            char tmp = str[0];
            str[0] = str[1];
            str[1] = tmp;
            opp[str]++;
        }

        scanf("%d", &N);
        scanf("%s", dest);

        ret = "";
        char tmp[3];
        tmp[2] = '\0';
        ret += dest[0];
        for(int i = 1; i < N; ++ i)
        {
            int end = ret.size() - 1;
            tmp[0] = ret[end];
            tmp[1] = dest[i];
            if(combine[tmp] != "")
            {
                ret[end] = combine[tmp][0];

            }
            else
            {
                bool flag = false;
                for(int j = 0; j < ret.size(); ++ j)
                {
                    tmp[0] = ret[j];
                    tmp[1] = dest[i];
                    if(opp[tmp])
                    {
                        ret.clear();
                        flag = true;
                        break;
                    }
                }

                if(!flag)
                {
                    ret.push_back(dest[i]);
                }
            }
        }

        if(ret.size() == 0)
        {
              printf("Case #%d: []\n", cnt);
              continue;
        }

        printf("Case #%d: [", cnt);

        for(int i = 0; i < ret.size()-1; ++ i)
        {
            printf("%c, ", ret[i]);
        }
        printf("%c]\n", ret[ret.size() -1]);
    }

    return 0;
}
