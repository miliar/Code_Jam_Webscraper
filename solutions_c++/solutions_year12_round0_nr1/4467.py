#include<stdio.h>
#include<string.h>
#include<conio.h>

int main(){

    char s[1000],out[1000];
    char ch[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w',
    'j','p','f','m','a','q'};
    int i,n;

    scanf("%d",&n);
    gets(s);
    for(i=0;i<n;i++){
        gets(s);
        int j=0,k=0;
        while(s[j]!='\0'){
            if(s[j]==' ')out[k]=' ';
            else out[k]=ch[(int)s[j]-97];
            k++;j++;
        }
        out[k]='\0';
        printf("Case #%d: %s\n",i+1,out);
    }

}
