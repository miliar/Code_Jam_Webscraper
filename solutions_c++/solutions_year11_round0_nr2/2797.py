#include <iostream>
#include <cstdio>
#include <cstring>
#include <utility>
#include <vector>
using namespace std;
#define x first
#define y second
const int MAXN = 1000;
char StrEle[MAXN], ans[MAXN], st[10];
typedef pair<char, char> p;
typedef pair<p, char> pp;
pp combine[50];
p opposed[40];
int T, C, D, N;
int cnt;
int IsCom(char & c)
{
    p t;
    t.x = ans[cnt - 1];
    t.y = ans[cnt];
    for(int i = 0; i < C; i++){
        if((t.x == combine[i].x.x && t.y == combine[i].x.y) || (t.y == combine[i].x.x && t.x == combine[i].x.y)){
            c = combine[i].y;
            return 1;
        }
    }
    return 0;
}
int IsOpp()
{
    p t;
    t.y = ans[cnt];
    for(int j = 0; j < cnt; j++){
        t.x = ans[j];
        for(int i = 0; i < D; i++){
            if((t.x == opposed[i].x && t.y == opposed[i].y) || (t.y == opposed[i].x && t.x == opposed[i].y))
                return 1;
        }
    }
    return 0;
}
int main()
{
    char c;
    int con = 1;
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    while(T--){
        scanf("%d", &C);
        for(int i = 0; i < C; i++){
            scanf("%s", st);
            combine[i].x.x = st[0];
            combine[i].x.y = st[1];
            combine[i].y = st[2];
        }
        scanf("%d", &D);
        for(int i = 0; i < D; i++){
            scanf("%s", st);
            opposed[i].x = st[0];
            opposed[i].y = st[1];
        }
        scanf("%d %s", &N, StrEle);
        cnt = 0;
        for(int i = 0; i < N; i++){
            ans[cnt] = StrEle[i];
            if(cnt){
                if(IsCom(c)){
                    ans[cnt - 1] = c;
                }else if(IsOpp())
                    cnt = 0;
                else cnt++;
            }else cnt++;
        }
        ans[cnt] = '\0';
        printf("Case #%d: [", con++);
        for(int i = 0; i < cnt; i++){
            printf("%c", ans[i]);
            if(i != cnt - 1) printf(", ");
            else break;
        }
        printf("]\n");
    }
    return 0;
}
