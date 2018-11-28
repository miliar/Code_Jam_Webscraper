#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<map>

using namespace std;

map<string, int> mix;
int cou;
int dp[20000];
int n;
int presize[20000];
int pre[20000][20];

void calc(int pos) {
    int i,j;
    vector<int> sizes;
    for (i=0; i<presize[pos]; i++) {
        calc(pre[pos][i]);
        sizes.push_back(dp[pre[pos][i]]);
    }
    sort(sizes.begin(), sizes.end());
    dp[pos] = 1 + presize[pos];
    for (i=0; i<presize[pos]; i++) {
        if (dp[pos] < presize[pos] - i - 1 + sizes[i])
            dp[pos] = presize[pos] - i - 1 + sizes[i];
        //printf("pos %d %d %d\n", pos, pre[pos][i], dp[pos]);
    }    
}

int main(){
    int teste;
    int c;
    int i, j;
    char leitor[1000];
    scanf("%d", &c);
    for (teste=0;teste<c;teste++) {
        scanf("%d", &n);
        cou = 0;
        mix.clear();
        for (i=0; i<n; i++){
            scanf("%s", leitor);
            string aux = string(leitor);
            int val;
            if (mix.count(aux) == 0){
                val = cou;
                mix[aux] = cou;
                cou++;
            }
            else {
                val = mix[aux];
            }
            int m;
            scanf("%d", &m);
            presize[val] = 0;
            for (j=0; j<m; j++) {
                scanf("%s", leitor);
                if (leitor[0] >= 'a' && leitor[0] <= 'z') continue;
                string aux2 = string(leitor);
                int val2;
                if (mix.count(aux2) == 0){
                    val2 = cou;
                    mix[aux2] = cou;
                    cou++;
                }
                else {
                    val2 = mix[aux2];
                }
                pre[val][presize[val]++] = val2;
            }
        }
        calc(0);
        /*for (i=0; i<cou; i++) {
            printf("%d %d\n", i, dp[i]);
        }*/
        printf("Case #%d: %d\n", teste+1, dp[0]);
    }
    return 0;
}
