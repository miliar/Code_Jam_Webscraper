#include<cstdio>
#include<cstring>
int tc;
char s[500];
int hash[50];

int main(){
 scanf("%d\n",&tc);
 for (int ti = 1; ti <= tc; ti++){
    gets(s);    
    memset(hash,0,sizeof(hash));
    for (int i = 0; s[i]; i++){
        hash[s[i]-'0']++;    
    }
    bool dec = true;
    for (int i = 1; s[i]; i++){
        if (s[i] > s[i-1]) dec = false;
    }
    printf("Case #%d: ",ti);
    if (dec){
       for (int i = 1; i <= 9; i++){
           if (hash[i] > 0) {printf("%d",i); hash[i]--; break; }    
       }
       printf("0");
       for (int i = 0; i <= 9; i++){
           for (int j = 1; j <= hash[i]; j++) printf("%d",i);    
       }
       printf("\n");
    } else{
       int pos = 0;
       for (int i = 0; s[i+1]; i++){
           if (s[i] < s[i+1]) { pos = i;}
       }
       int posi = -1;

       for (int i = pos+1; s[i]; i++){
           if (s[i] > s[pos]) {
              if ((posi == -1) || (s[i] < s[posi])) posi = i;
           }
       }

       for (int i = 0; i < pos; i++){ printf("%c",s[i]);}
       printf("%c",s[posi]);
       memset(hash,0,sizeof(hash));
       for (int i = pos; s[i]; i++){
           if (i == posi) continue;
           hash[s[i]-'0']++;
       }
       for (int i = 0; i <= 9; i++){
           for (int j = 1; j <= hash[i]; j++) printf("%d",i);    
       }
       printf("\n");
       
    }
 }
}
