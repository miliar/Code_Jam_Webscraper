#include <iostream>

using namespace std;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int n;
    char c;
    char alpha[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    scanf("%i",&n);
    scanf("%c",&c);
    /*
    char *new_alpha=new char[26];
    char *falpha=new char[512];
    char *salpha=new char[512];
    for(char a='a';a<='z';a++)
        new_alpha[a-'a']=' ';
    int i=0,j=0;
    while(i<3){
        scanf("%c",&c);
        if(c=='\n')
            i++;
        else
            falpha[j++]=c;
    }
    j=0;
    while(i<6){
        scanf("%c",&c);
        if(c=='\n')
            i++;
        else
            salpha[j++]=c;
    }
    for(i=0;i<j;i++)
        new_alpha[falpha[i]-'a']=salpha[i];
        //printf("%c=>%c\n",falpha[i],salpha[i]);
    for(i=0;i<26;i++)
        printf("%c=>%c\n",i+'a',new_alpha[i]);
*/

    int i=1;
    printf("Case #%i: ",i);
    while(EOF!=scanf("%c",&c)){
        if(c=='\n'){
            if((i++)!=n)
                printf("\nCase #%i: ",i);
        }else
            printf("%c",(c==' ')?(c):(alpha[c-'a']) );
    }printf("\n");
    return 0;
}
