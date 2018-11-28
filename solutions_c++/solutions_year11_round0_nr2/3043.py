#include <cstdio>
#include <string.h>
#include <string>
#include <iostream>
using namespace std;

#define TAM strlen(s)

int x[27][27],y[27];


main(){
    int t,c,n,d;
    char a,b,r;
    scanf("%d",&t);
    char s[200];
    for(int k=1;k<=t;k++){
        memset(x,-1,sizeof(x));
        memset(y,-1,sizeof(y));
        s[0]=0;
        scanf("%d",&c);
        while(c--){
            scanf(" %c%c%c",&a,&b,&r);
            a-='A';
            b-='A';
            r-='A';
            x[a][b]=r;
            x[b][a]=r;
        }
        scanf("%d",&d);
        c = d;
        while(c--){
            scanf(" %c%c",&a,&b);
            a-='A';
            b-='A';
            y[a]=b;
            y[b]=a;
        }
        scanf("%d",&n);
        while(n--){
            scanf(" %c",&a);

                if( TAM > 0 && (b = x[a-'A'][s[TAM-1]-'A'])!=-1 ){
                    s[TAM-1]= b+'A';
                }else if( TAM > 0 && (b = x[s[TAM-1]-'A'][a-'A'])!=-1 ){
                    s[TAM-1]= b+'A';
                }else if(y[a-'A']!=-1 && strchr(s, y[a-'A']+'A')!= NULL)
                    s[0]=0;
                else{
                    strncat(s,&a,1);
                }

            //printf("%s\n",s);
        }
    printf("Case #%d: [",k); //Case #1: [E, A]
    int ta = TAM;
    if(ta>0){
        for(int i=0;i<ta-1;i++){
            printf("%c, ",s[i]);
        }
        printf("%c",s[ta-1]);
    }
    printf("]\n");
    }

return 0;

}
