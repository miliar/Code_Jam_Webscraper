#include<stdio.h>
#include<string.h>
int mapping[1000];
int main (){
    char s1[100],s2[100];
    int len,i;
    while(gets(s1)){
        gets(s2);
        len = strlen(s1);
        for(i=0;i<len;i++){
            if(s1[i] != ' '){
                mapping[s1[i]] = s2[i];
            }
        }

    }
    for(i=97;i<97+26;i++){
        printf("else if(in[i] == '%c')in[i] = '%c';\n",i,mapping[i]);
    }
    return 0;
}
