#include <stdio.h>
#include <map>
#include <string>
#include <vector>
using namespace std;
char s[111],st[111];
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int ca;
    scanf("%d", &ca);
    for(int v=1; v<=ca; v++) {
        int n,m;
        scanf("%d%d", &n, &m);
        int ret = 0;
        vector< map<string, int> > dir;
        int cnt = 1;
        dir.push_back(map<string, int>());
        for(int i=0; i<n; i++) {
            scanf("%s", s);
            vector<string> path;
            for(int j=1; s[j] != 0; ) {
                int k = j, w=0;
                while(s[k] != 0 && s[k] != '/') {
                    st[w++] = s[k];
                    k++;
                }
                st[w] = 0;
                path.push_back(st);

                if(s[k] == 0) break;
                else j = k+1;
            }
            int now = 0;
            for(int j=0; j<path.size(); j++) {
                if(dir[now].find(path[j]) != dir[now].end()) {
                    now = dir[now][path[j]];
                }
                else {
                    dir[now][path[j]] = cnt;
                    now = cnt;
                    dir.push_back(map<string, int>());
                    cnt++;
                }
            }
        }

        for(int i=0; i<m; i++) {
            scanf("%s", s);
            vector<string> path;
            for(int j=1; s[j] != 0; ) {
                int k = j, w=0;
                while(s[k] != 0 && s[k] != '/') {
                    st[w++] = s[k];
                    k++;
                }
                st[w] = 0;
                path.push_back(st);

                if(s[k] == 0) break;
                else j = k+1;
            }
            int now = 0;
            for(int j=0; j<path.size(); j++) {
                if(dir[now].find(path[j]) != dir[now].end()) {
                    now = dir[now][path[j]];
                }
                else {
                   // printf("add: %d %s\n", j, path[j].c_str());
                    dir[now][path[j]] = cnt;
                    now = cnt;
                    dir.push_back(map<string, int>());
                    cnt++;
                    ret++;
                }
            }
        }
        printf("Case #%d: %d\n", v, ret);
    }
    return 0;
}
