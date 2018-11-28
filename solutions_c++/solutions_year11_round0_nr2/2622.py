#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

string st;
char g[255][255],a[1000];
bool op[255][255];

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    cin >> T;
    for (int casenum=1; casenum<=T; ++casenum){
        int t1,t2,n;
        cin >> t1;
        memset(g,0,sizeof(g));
        memset(op,0,sizeof(op));
        for (int i=1; i<=t1; ++i){
            cin >> st;
            g[st[0]][st[1]] = st[2];
            g[st[1]][st[0]] = st[2];
        }
        cin >> t2;
        for (int i=1; i<=t2; ++i){
            cin >> st;
            op[st[0]][st[1]] = 1; op[st[1]][st[0]] = 1;
        }
        cin >> n;
        cin >> st;
        int len = 0;
        for (string::size_type i=0; i<st.size(); ++i){
            a[len++] = st[i];
            if (len > 1 && g[a[len-1]][a[len-2]]){
                a[len-2] = g[a[len-1]][a[len-2]];
                len--;
                continue;
            }
            for (int i=0; i<len-1; i++)
                if (op[a[i]][a[len-1]]){
                    len = 0; break;
                }
        }
        printf("Case #%d: [",casenum);
        for (int i=0; i<len; ++i){
            printf("%c",a[i]);
            if (i != len-1) printf(", ");
        }
        printf("]\n");
    }
    return 0;
}
