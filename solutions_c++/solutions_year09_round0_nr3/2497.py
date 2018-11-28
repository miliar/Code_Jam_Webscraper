#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *f = "welcome to code jam";
char input[503],tmp[503];
int total;

void find(int j,int k){
     if (j == strlen(f)){
        total++;
     }
     else {
          int i;
          for (i=k;i<strlen(input);i++){
              if (strlen(input) - i > 0 && input[i] == f[j]){//printf("%d %d\n",i,j);puts(f);getchar();
                 find(j+1,i);
              }
          }
     }
}

int main (){
    int n,i,j;
    fgets(input,503,stdin);
    input[strlen(input)-1] = '\0';
    sscanf(input,"%d",&n);
    for (i=0;i<n;i++){
        total=0;
        fgets(input,503,stdin);
        input[strlen(input)-1] = '\0';
        find(0,0);
        printf("Case #%d: ",i+1);
        sprintf(input,"%d",total);
        if (strlen(input) < 4){
           for (j=0;j<(4 - strlen(input));j++)printf("0");
           for (j=0;j<strlen(input);j++)printf("%c",input[j]);
        }
        else for (j=strlen(input)-4;j<strlen(input);j++){
             printf("%c",input[j]);
        }
        printf("\n");
    }
    
    while (getchar()!=EOF);
    return 0;
}
