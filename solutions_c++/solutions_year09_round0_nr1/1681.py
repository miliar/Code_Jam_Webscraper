#include <stdio.h>
#include <stdlib.h>

int L,D,N;

int is_matched(char* word, char* pattern) {
    int ind=0;
    for (int i=0;i<L;++i) {
        if (!pattern[ind]) return 0;
        if (pattern[ind] == word[i]) {
           ++ind;
           continue;
           }
        if (pattern[ind] != '(') 
           return 0;
        else {
           while (pattern[ind] != ')') {
                 if (pattern[ind] == word[i]) break;
                 ++ind;
                 }
           if (pattern[ind] == ')')
              return 0;
           while (pattern[ind++] != ')');             
        }
    }
    return 1;
}

int get_count(char** words, char* pattern) {
    int ret = 0;
    for (int i=0;i<D;++i) {
        ret += is_matched(words[i],pattern);
    }
    return ret;
}

int main() {
    freopen("file.in","r",stdin);
    freopen("file.out","w",stdout);
    scanf("%d %d %d\n",&L,&D,&N);
    char** words = (char**) malloc(D*sizeof(char*));
    for (int i=0;i<D;++i) {
        char* word = (char*) malloc(L+1);
        gets(word);
        words[i] = word;
        }
    for (int i=0;i<N;++i) {
        char pattern[500];
        gets(pattern);
        int cnt = get_count(words,pattern);
        printf("Case #%d: %d\n",i+1,cnt);
    }
    return 0;     
}
