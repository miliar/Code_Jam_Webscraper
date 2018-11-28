#include <stdio.h>
#include <string.h>

char words[5010][20];
char pattern[20][256];
char token[5000];
int l,d,n;

int match(char *word) {
    for (int i=0; i<l; i++) {
        //printf("%c", word[i]);
        if (pattern[i][word[i]] == 0) return 0;
    }
    //printf("*");
    return 1;
}


int main() {
    scanf("%d%d%d\n", &l, &d, &n);

    for (int i=0; i<d; i++) {
        scanf("%s", words[i]);
    }

    for (int i=0; i<n; i++) {
        scanf("%s", token);
        memset(pattern, 0, sizeof(pattern));
        int p=0;
        int par=0;
        for (char* c=token; *c; c++) {
            if (*c=='(') {
                par=1;
            } else if (*c==')') {
                par=0;
            } else if (*c>='a' && *c<= 'z') {
                pattern[p][*c]=1;
            }
            if (par==0) {
                p++;
            }
        }
        /*for (int i=0; i<l;i++) {
            for (int j='a'; j<='z';j++) {
                if (pattern[i][j]) 
                printf("%c", j);
            }
            printf("\n");
        }*/

        int matches = 0;
        for (int j=0; j<d; j++) {
            if (match(words[j])) {
                matches++;
                //printf("%s\n", words[j]);
            }
            //printf("\n");
        }
        printf("Case #%d: %d\n", i+1, matches);
    }

}
