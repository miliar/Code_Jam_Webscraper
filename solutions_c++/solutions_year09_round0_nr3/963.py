#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const char base[] = "welcome to code jam";
const int max_size = 500 + 50;
const int max_len = 30 + 5;

int opt[max_size][max_len];

int main(){
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    
    int nCase;
    
    scanf("%d", &nCase);
    getchar();
    
    for (int t=1; t<=nCase; t++){
        printf("Case #%d:", t);
        int l2 = strlen(base);
        
        char tmp[max_size];
        gets(tmp);
        
        memset(opt, 0, sizeof(opt));
        
        int len = strlen(tmp);
        
        if (tmp[0] == base[0]) opt[0][0] = 1;
        
        for (int i=1; i<len; i++)
            if (tmp[i] == base[0]) opt[i][0] = opt[i - 1][0] + 1;
            else opt[i][0] = opt[i - 1][0];
        
        
        for (int i=1; i<len; i++)
            for (int j=1; j<l2; j++){
                if (tmp[i] == base[j]) opt[i][j] = opt[i - 1][j] + opt[i - 1][j - 1];
                else opt[i][j] = opt[i - 1][j];
                opt[i][j] %= 10000;
            }
        
        printf(" %04d\n", opt[len - 1][l2 - 1]);
    }
    
    return 0;
}
