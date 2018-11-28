#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(){
    int n;
    int size;
    char* string=(char*)malloc(sizeof(char)*200);
    char* alphabet = "yhesocvxduiglbkrztnwjpfmaq";
    scanf("%d",&n);
    char* s;
    gets(s);
    for(int i=0;i<n;i++){
        gets(string);
        size=strlen(string);
        printf("Case #%d: ",i+1);
        for(int j=0;j<size;j++){
            if(string[j]==' ')printf(" ");
            else{
                int a=string[j]-97;
                printf("%c",alphabet[a]);
            }
        }
        printf("\n");
    }
    return 0;
}
