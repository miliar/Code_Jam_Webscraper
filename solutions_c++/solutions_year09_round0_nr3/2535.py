#include<cstdio>
#include<algorithm>
using namespace std;

int x,wynik,len;
char wzor[19]={'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'},tekst[505];

void gcj(int ind,int wz){
     for(int i=ind;i<len;i++){
             if(tekst[i] == wzor[wz]){
                        if(wz == 18)
                              wynik++;
                        else
                            gcj(i+1,wz+1);
             }
     }
}

int main(){
    char c;
    scanf("%d\n",&x);
    for(int i=1;i<=x;i++){
            len=0;
            for(scanf("%c",&c);c!='\n';scanf("%c",&c))
              tekst[len++] = c;
            /*for(int j=0;j<len;j++)
                     printf("%c",tekst[j]);
            printf("-\n");*/
            wynik = 0;
            gcj(0,0);
            printf("Case #%d: %04d\n",i,wynik);
            /*for(int j=0;j<19;j++)
                     printf("%c",wzor[j]);
            printf("\n");*/
    }
    return 0;
}
