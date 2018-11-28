#include <stdio.h>

FILE *out;

char letras[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char c;

int main(){
    out = fopen("texto.txt","w");
    int t;
    scanf("%d ",&t);
    for(int i=1;i<=t;i++){
        fprintf(out,"Case #%d: ",i);
        scanf("%c",&c);
        while(c!='\n'&&c!='\0'&&c!=0){
            if(c==' ')
                fprintf(out," ");
            else fprintf(out,"%c",letras[c-'a']);
            scanf("%c",&c);
        }
        fprintf(out,"\n");
    }
    return 0;
}
