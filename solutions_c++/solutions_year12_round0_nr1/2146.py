#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char s[200];

char aa[26];
char check[26];
int main(){
    FILE *f = fopen("tmp1.txt","r");
    for (int i = 0 ;i < 26 ; i++){
        fscanf(f,"%s",s);
        aa[s[0]-'a'] = i+'a';
    }
    fclose(f);
    f= fopen("in1.txt","r");
    FILE *fo = fopen("out1.txt","w");
    fgets(s,200,f);
    int T = atoi(s);
    for (int t = 1 ; t<= T ; t++){
        fprintf(fo,"Case #%d: ",t);
        fgets(s,200,f);
        int l = strlen(s) -1;
        for (int i = 0 ; i < l ; i++){
            if (s[i] != ' ') {
                s[i] = aa[s[i]-'a'];
            }
        }
        fprintf(fo,"%s",s);
    }
    fclose(fo);
   // system("pause");
}
