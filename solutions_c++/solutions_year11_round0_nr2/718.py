#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>

using namespace std;

const int maxn = 110;
const int maxm = 310;


char mat[maxm][maxm];
int det[maxm][maxm];
int n, m;
char ch[maxm];
char stk[maxm];
int len;
int cnt;

void Init(){
    for(int i = 0; i < maxm; i ++){
        for(int j = 0; j < maxm; j ++){
            mat[i][j] = '$';
            det[i][j] = 0;
        }
    }
}

void Solve(int t){
    cnt = 0;
    for(int i = 0; i < len; i ++){
//        for(int i = 0; i < cnt;i ++)
//            cout << stk[i] << " ";
//        cout << endl;
        if(cnt > 0 && mat[stk[cnt - 1]][ch[i]] != '$'){
            stk[cnt - 1] = mat[stk[cnt - 1]][ch[i]];
        }
        else
            stk[cnt ++] = ch[i];
        if(cnt > 0){
            for(int j = 0; j < cnt - 1; j ++){
                if(det[stk[cnt - 1]][stk[j]]){
                    cnt = 0;
                    break;
                }
            }
        }
    }

    cout << "Case #" << t << ": ";
    cout << "[";
    bool flag = false;

    for(int i = 0; i < cnt; i ++){
        if(!flag)
            flag = true;
        else
            printf(", ");
        printf("%c", stk[i]);
    }

    cout << "]" << endl;
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;
    cin >> T;

    for(int t = 1; t <= T; t ++){
        Init();
        cin >> n;
        for(int i = 0; i < n; i ++){
            scanf("%s", ch);
            mat[ch[0]][ch[1]] = ch[2];
            mat[ch[1]][ch[0]] = ch[2];
        }

        cin >> m;
        for(int i = 0; i < m; i ++){
            scanf("%s", ch);
            det[ch[0]][ch[1]] = 1;
            det[ch[1]][ch[0]] = 1;
        }

        cin >> len;
        scanf("%s", ch);

        Solve(t);
    }

    return 0;
}
