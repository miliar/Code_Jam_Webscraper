#include <cstdio>
#include <cstdlib>
#include <cstring>

int main(){
    char dic[100];
    int i,j,k,t;
    char in[300];
    char out[300];
    char aux;
    
    strcpy(in,"ejp mysljylc kd kxveddknmc re jsicpdrysi");
    strcpy(out,"our language is impossible to understand");
    for( i =0; i < strlen(in);i++){
        if(in[i] != ' '){
            dic[in[i]-'a'] = out[i];
        }
    }
    strcpy(in,"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    strcpy(out,"there are twenty six factorial possibilities");
    for( i =0; i < strlen(in);i++){
        if(in[i] != ' '){
            dic[in[i]-'a'] = out[i];
        }
    }
    strcpy(in,"de kr kd eoya kw aej tysr re ujdr lkgc jv");
    strcpy(out,"so it is okay if you want to just give up");
    for( i =0; i < strlen(in);i++){
        if(in[i] != ' '){
            dic[in[i]-'a'] = out[i];
        }
    }
    dic['z'-'a'] = 'q';
    dic['q'-'a'] = 'z';
  //  for( i = 0; i <= 'z'-'a'; i++){
  //      printf("%c -> %c\n", i+'a', dic[i]);
 //   }
    scanf("%d", &t);
    scanf("%c", &aux);
    while( aux != '\n' ) {
        scanf("%c", aux);
    }
    for( i =1; i <= t; i++){
        printf("Case #%d: ", i);
        while(1){
            if(scanf("%c", &aux) == 0 ) break;
            if( aux == ' ' || aux == '\n'){
                printf("%c", aux);
                if( aux == '\n' ) break;
            } else {
                printf("%c", dic[aux-'a']);
            }
        }
    }
}
