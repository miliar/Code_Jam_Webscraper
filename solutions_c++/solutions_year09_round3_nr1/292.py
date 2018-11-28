#define maxn 100
#define ll long long
#include <iostream>
using namespace std;
char s[maxn];
ll ans;
int p[260];
int main(){
    int test;
    scanf("%d",&test); getchar();
    for (int c=1;c<=test;c++) {
        memset(p,0xff,sizeof p);
        gets(s);
        int cnt = 0;
        p[s[0]] = 1;
        int len = strlen(s);
        for (int i=1; i<len; i++){
            if (p[s[i]]!=-1) continue;
            p[s[i]] = ++cnt;
            if (cnt==1) p[s[i]] = 0;
        }
        cnt ++;
        ans = 0;
        ll tmp = 1;
        if (cnt==1) cnt++;
        for (int i=len-1; i>=0;i--){
            ans += tmp * p[s[i]];
            tmp *= cnt;
        }
        printf("Case #%d: %lld\n",c,ans);
    }
}

