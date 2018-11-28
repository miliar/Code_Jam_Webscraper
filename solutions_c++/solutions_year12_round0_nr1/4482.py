#include<stdio.h>

char table[100]="yhesocvxduiglbkrztnwjpfmaq";

int main()
{
    int q=0,t;
    char s[1000];

    FILE *out,*in;

    in=fopen("input.txt","r");

    out=fopen("output.txt","w");

    fscanf(in,"%d",&t);
    fgets(s,1000,in);
    for(q=0;q<t;q++){

        fgets(s,1000,in);

        for(int i=0;s[i]!=0;i++){
            if(s[i]>='a' &&s[i]<='z') s[i]=table[s[i]-'a'];
        }
        fprintf(out,"Case #%d: %s",q+1,s);

    }

    return 0;
}
