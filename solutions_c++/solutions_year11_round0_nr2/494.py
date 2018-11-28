#include <cstdio>

int main() {
    int t, T;
    scanf("%d", &T);
    
    for (t = 1; t <= T; t++) {
        int c, d, n;
        int combine[26][26];
        int oppose[26][26];
        int curr[100];
        int currn = 0;
        
        char temp[200];
        int i, j;
        
        for (i = 0; i < 26; i++) {
            for (j = 0; j < 26; j++) {
                combine[i][j] = 26;
                oppose[i][j] = 0;
            }
        }
        
        scanf("%d", &c);
        for (i = 0; i < c; i++) {
            scanf("%s", temp);
            combine[temp[0]-'A'][temp[1]-'A'] = temp[2]-'A';
            combine[temp[1]-'A'][temp[0]-'A'] = temp[2]-'A';
        }
        scanf("%d", &d);
        for (i = 0; i < d; i++) {
            scanf("%s", temp);
            oppose[temp[0]-'A'][temp[1]-'A'] = 1;
            oppose[temp[1]-'A'][temp[0]-'A'] = 1;
        }
        scanf("%d", &n);
        scanf("%s", temp);
        
        for (i = 0; i < n; i++) {
            if (currn > 0 && combine[temp[i]-'A'][curr[currn-1]] != 26) {
                curr[currn-1] = combine[temp[i]-'A'][curr[currn-1]];
                continue;
            }
            
            for (j = 0; j < currn; j++) {
                if (oppose[temp[i]-'A'][curr[j]]) {
                    j = currn;
                    currn = 0;
                }
            }
            if (j != currn)
                continue;
            
            curr[currn] = temp[i]-'A';
            currn++;
        }
        
        printf("Case #%d: [", t);
        for (i = 0; i < currn-1; i++)
            printf("%c, ", curr[i]+'A');
        if (currn > 0)
            printf("%c", curr[i]+'A');
        printf("]\n");
    }
}
        
            
        
            
