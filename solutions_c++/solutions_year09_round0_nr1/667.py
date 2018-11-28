#include<iostream>
#include<string>
#include<vector>
using namespace std;

int stat[20][30];
vector<string> dict;
int L, D, N;

int main() {
    FILE* fin = freopen("input.in", "r", stdin);
    scanf("%d %d %d", &L, &D, &N);
    char cc[20];
    for (int i=0;i<D;++i) {
        scanf("%s", cc);
        dict.push_back(string(cc));
    }

    for (int i=0;i<N;++i) {
        memset(stat, 0, sizeof(stat));
        for (int j=0;j<L;++j) {
            char ch;

            for (;;) {
                scanf("%c", &ch);
                if ((ch == '(') || (ch == ')')) break;
                if (('a'<=ch) && (ch<='z')) break;
            }
            if (ch != '(') 
                stat[j][ch-'a'] = 1;
            else {
                for (;;) {
                    scanf("%c", &ch);
                    if (ch == ')') break;
                    stat[j][ch-'a'] = 1;
                }
            }
        }

        int tot = 0;
        for (int j=0;j<D;++j) {
            bool flag = true;
            for (int k=0;k<L;++k)
                if (stat[k][dict[j][k]-'a'] ==0) {
                    flag = false;
                    break;
                }
            if (flag) tot++;
        }

        printf("Case #%d: %d\n", i+1, tot);
    }
    return 0;
}
