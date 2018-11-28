#include <cstdio>
#include <string>
#include <set>

using namespace std;

const int MAX = 110;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("output.out","w",stdout);
    int n, m, t, cas = 0;
    char str[MAX];
    scanf("%d", &t);
    while (t--){
        scanf("%d %d", &n, &m);
        set<string> dic;
        while (n--){
            char tmp[MAX]={};
            scanf("%s", str);
            for (int i = 0; str[i]; ++i){
                tmp[i] = str[i];
                if (str[i+1] == '/' || str[i+1] == 0) dic.insert(tmp);
            }
        }
        int ans = 0;
        while (m--){
            char tmp[MAX]={};
            scanf("%s", str);
            for (int i = 0; str[i]; ++i){
                tmp[i] = str[i];
                if (str[i+1] == '/' || str[i+1] == 0){
                    if (dic.count(tmp) == 0) ++ans, dic.insert(tmp);
                }
            }
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
