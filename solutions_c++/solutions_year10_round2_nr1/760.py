#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

int T;
int N, M, n;
int ans;

class node
{
    public:
        int floor;
        int fa;
        char name[101];
}v[10001];

int main()
{
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    scanf("%d", &T);
    for(int i = 1; i <= T; i++)
    {
        scanf("%d%d", &N, &M);
        n = 0;
        ans = 0;
        memset(v, 0, sizeof(v));
        for(int j = 1; j <= N; j++)
        {
            int k = 1;
            int pos;
            int last = 0;
            int fl = 0;;
            char temp[101];
            char getname[101];
            memset(temp, 0, sizeof(temp));
            scanf("%s", temp);
            while(1)
            {
                memset(getname, 0, sizeof(getname));
                pos = 0;
                for(; temp[k]!= '/' && temp[k] != '\0'; k++)
                {
                    getname[pos] = temp[k];
                    pos++;
                }
                bool flag = 1;
                for(int l = 1; l <= n; l++)
                {
                    if(!strcmp(getname, v[l].name) && v[l].floor == fl && v[l].fa == last)
                    {
                        last = l;
                        flag = 0;
                        break;
                    }
                }
                if(flag)
                {
                    n++;
                    strcpy(v[n].name, getname); 
                    v[n].floor = fl;
                    v[n].fa = last;
                    last = n;
                }
                if(temp[k] == '\0') break;
                k++;
                fl++;
            }
        }
        for(int j = 1; j <= M; j++)
        {
            int k = 1;
            int pos;
            int last = 0;
            int fl = 0;;
            char temp[101];
            char getname[101];
            memset(temp, 0, sizeof(temp));
            scanf("%s", temp);
            while(1)
            {
                memset(getname, 0, sizeof(getname));
                pos = 0;
                for(; temp[k]!= '/' && temp[k] != '\0'; k++)
                {
                    getname[pos] = temp[k];
                    pos++;
                }
                bool flag = 1;
                for(int l = 1; l <= n; l++)
                {
                    if(!strcmp(getname, v[l].name) && v[l].floor == fl && v[l].fa == last)
                    {
                        last = l;
                        flag = 0;
                        break;
                    }
                }
                if(flag)
                {
                    n++;
                    strcpy(v[n].name, getname); 
                    v[n].floor = fl;
                    v[n].fa = last;
                    last = n;
                    ans++;
                }
                if(temp[k] == '\0') break;
                k++;
                fl++;
            }
        }
        printf("Case #%d: %d\n", i, ans);
    }
    return 0;
}
