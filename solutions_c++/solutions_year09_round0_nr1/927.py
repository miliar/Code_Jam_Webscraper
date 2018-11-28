#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int max_size = 5000 + 10;
const int max_len = 15 + 1;

char dict[max_size][max_len];
char cur[max_size * 2];

int len, num, n;

int main(){
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    
    scanf("%d%d%d", &len, &num, &n);
    
    for (int i=0; i<num; i++) scanf("%s", dict[i]);

    for (int i=0; i<n; i++){
        scanf("%s", cur);
        int ans = 0;
        
        for (int j=0; j<num; j++){
            bool flag = true;
            int head = 0;
            
            for (int k=0; k<len; k++){
                flag = false;
                if (cur[head] == '('){
                    while (cur[head] != ')'){
                        if (cur[head] == dict[j][k]) flag = true;
                        head++;
                    }
                }
                else if (cur[head] == dict[j][k]) flag = true;
                head++;
                
                if (!flag) break;
            }
            if (flag) ans++;
        }
        
        printf("Case #%d: %d\n", i + 1, ans);
    }
    
    return 0;
}
