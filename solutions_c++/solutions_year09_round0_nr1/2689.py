#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

int l,d,n,wynik,len;
char tekst[425],slownik[5005][16];
bool dane[28][16];

bool spr(int a){
     for(int i=0;i<l;i++){
             if(dane[slownik[a][i]-97][i] == 0)
                                          return false;
     }
     return true;
}

int main(){
    scanf("%d%d%d",&l,&d,&n);
    for(int i=0;i<d;i++){
            scanf("%s",slownik[i]);
    }
    for(int i=1;i<=n;i++){
            scanf("%s",tekst);
            len=strlen(tekst);
            int z = 0;
            bool otwarty;
            for(int j=0;j<len;j++){
                    if(tekst[j] == '('){
                                otwarty = true;
                                continue;
                    }
                    if(tekst[j] == ')'){
                                otwarty = false;
                                z++;
                                continue;
                    }
                    dane[tekst[j]-97][z] = 1;
                    if(!otwarty)
                                z++;
            }
            /*for(int j=0;j<27;j++){
                    for(int k=0;k<17;k++)
                            printf("%d ",dane[j][k]);
                    printf("\n");
            }*/
            wynik = 0;
            for(int j=0;j<d;j++){
                    if(spr(j))
                           wynik++;
            }
            printf("Case #%d: %d\n",i,wynik);
            for(int j=0;j<27;j++)
                    for(int k=0;k<17;k++)
                            dane[j][k] = false;
    }
    return 0;
}
