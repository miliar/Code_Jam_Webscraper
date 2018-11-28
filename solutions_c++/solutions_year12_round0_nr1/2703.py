#include <cstdio>
#include <cstring>

#define MAX 110

char G[MAX];
char S[MAX];

char antimap[26][2] = { {'a', 'y'},{'b', 'h'},{'c', 'e'}, {'d', 's'}, {'e', 'o'}
                        ,{'f', 'c'},{'g', 'v'}, {'h', 'x'}, {'i', 'd'}, {'j', 'u'}
                        ,{'k','i'},{'l','g'},{'m','l'},{'n','b'},{'o','k'}
                        ,{'p','r'},{'q','z'},{'r','t'},{'s','n'},{'t','w'}
                        ,{'u','j'},{'v','p'},{'w','f'},{'x','m'},{'y','a'},{'z','q'}
                };

int main()
{
    int T, i;
    FILE *fin = fopen("A-small.in", "r");
    FILE *fout = fopen("A-small.out", "w");
    fscanf(fin,"%d\n", &T);
    for(i=1;i<=T;++i){
        fgets(G, 105, fin);
        int len = strlen(G);
        int j;
        for(j=0;j<len;++j){
        if(G[j] == ' ')
            S[j] = ' ';
        else
            S[j] = antimap[G[j]-'a'][1];
        }
        S[len] = '\0';

        fprintf(fout, "Case #%d: %s\n", i, S);
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
