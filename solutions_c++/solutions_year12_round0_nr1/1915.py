#include <iostream>

//abcdefghijklmnopqrstuvwxyz
char map[] = "yhesocvxduiglbkrztnwjpfmaq";
char s[1000];

int main(void){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    
    int test;
    scanf("%i\n",&test);
    for (int i=0;i<test;i++){
        gets(s);
        int j =0;
        while (s[j]){
            if (s[j]>='a' && s[j]<='z'){
                s[j]=map[s[j]-'a']; 
                //printf("%c",s[j]);
                //flush();   
            }
            j++;  
        }  
        printf("Case #%i: ",i+1);
        printf("%s\n",s);
    }
    
    return 0;    
}
