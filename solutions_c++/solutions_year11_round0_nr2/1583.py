#include <iostream>
#include <cstdio>

using namespace std;

int k;
int l[200];
char res[30][30];
bool bad[30][30];

inline void get(char& ch){
    scanf("%c", &ch);
    while((ch < 'A') || (ch > 'Z')){
        scanf("%c", &ch);
    }
}

inline int f(char ch){
    return (ch - 'A');
}

inline char g(int a){
    return ('A' + a);
}

inline bool good(char ch){
    return ((ch >= 'A') && (ch <= 'Z'));
}

void add(int a){
    char ch = res[l[k - 1]][a];
    if(good(ch)){
        l[k - 1] = f(ch);
        while(k > 1){
            ch = res[l[k - 2]][l[k - 1]];
            if(good(ch)){
                l[k - 2] = f(ch);
                k--;
            }
            else{
                break;
            }
        }
    }
    else{
        for(int i = 0; i < k; i++){
            if(bad[l[i]][a]){
                k = 0;
                return;
            }
        }
        l[k++] = a;
    }
}

int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int tt = 0; tt < t; tt++){
        for(int i = 0; i < 26; i++){
            for(int j = 0; j < 26; j++){
                res[i][j] = '!';
                bad[i][j] = false;
            }
        }
        int n;
        scanf("%d", &n);
        for(int i = 0; i < n; i++){
            char a, b, c;
            get(a);
            get(b);
            get(c);
            int aa = f(a);
            int bb = f(b);
            res[aa][bb] = res[bb][aa] = c;
        }
        scanf("%d", &n);
        for(int i = 0; i < n; i++){
            char a, b;
            get(a);
            get(b);
            int aa = f(a);
            int bb = f(b);
            bad[aa][bb] = bad[bb][aa] = true;
        }
        k = 0;
        scanf("%d", &n);
        for(int i = 0; i < n; i++){
            char ch;
            get(ch);
            int cur = f(ch);
            add(cur);
        }
        printf("Case #%d: [", tt + 1);
        if(k > 0){
            printf("%c", g(l[0]));
            for(int i = 1; i < k; i++){
                printf(", %c", g(l[i]));
            }
        }
        printf("]\n");
    }
    return 0;
}
