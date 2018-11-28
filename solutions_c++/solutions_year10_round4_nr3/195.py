#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MAX = 150;

bool arr[MAX][MAX]={};

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t, n, x1, y1, x2, y2, cas = 0;
    scanf("%d", &t);
    while (t--){
        memset(arr, 0, sizeof(arr));
        scanf("%d", &n);
        int tot = 0;
        while (n--){
            scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
            if (x1 > x2) swap(x1,x2);
            if (y1 > y2) swap(y1,y2);
            for (int i = x1; i <= x2; ++i)
                for (int j = y1; j <= y2; ++j)
                    arr[i][j] = 1;
        }
        for (int i = 0; i < MAX; ++i)
            for (int j = 0; j < MAX; ++j)
                if (arr[i][j]) ++tot;
        int ans = 0;
        while (tot){
            bool a2[MAX][MAX]={};
            ++ans;
            for (int i = 0; i < MAX; ++i)
                for (int j = 0; j < MAX; ++j){
                    a2[i][j] = arr[i][j];
                    if (arr[i][j] && !arr[i-1][j] && !arr[i][j-1]) a2[i][j] = 0;
                    if (!arr[i][j] && arr[i-1][j] && arr[i][j-1]) a2[i][j] = 1;
                }
            tot = 0;
            for (int i = 0; i < MAX; ++i)
                for (int j = 0; j < MAX; ++j){
                    arr[i][j] = a2[i][j];
                    if (arr[i][j]) ++tot;
            }
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
