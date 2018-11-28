#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>
#include<iostream>
#include<algorithm>

using namespace std;
char s[1010];
map<string,int> data;
int n,m,ans;

void solve(bool flag);

int main(){
    freopen("al.in","r",stdin);
    freopen("al.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int  t = 1; t <= T ; ++t){
       data.clear();
       ans = 0;
       
       scanf("%d%d", &n , &m);
       
       while (n--) solve(true);
       while (m--) solve(false);
       
       printf("Case #%d: ", t);
       printf("%d\n", ans);
    }
    return 0;
}

void solve(bool flag){
    scanf("%s", s);
    int len = strlen(s);
    if (len == 1) return;
    int pos = 1;
    while(pos < len){
        if (s[pos] == '/' || pos == len - 1){
            int p = pos;
            if (pos == len - 1) p++;
            if (flag) data[string(s,p)] = 1;
            else if (!data[string(s,p)]) {
                 ++ans;
                 data[string(s,p)] = 1;
              }
        }
        ++pos;
   }
}
