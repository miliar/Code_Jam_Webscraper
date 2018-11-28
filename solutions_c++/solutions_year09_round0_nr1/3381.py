#include <stdio.h>

int const MAXW= 5000;
int const MAXL= 15;
int const LENC= 256; // с запасом! 

int l, d, n;
bool mat[MAXL+1][LENC]; 
char mas[MAXW+1][MAXL+1]; 
char pat[MAXL*LENC]; 

int main() {
    int i, j, k;
    int res;
    bool o;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d %d %d", &l, &d, &n);
    for(i=1; i<=d; i++)
        scanf("%s", &mas[i]);
    
    for(k=1; k<=n; k++) {
        for(i=0; i<=MAXL; i++)
            for(j=0; j<LENC; j++)
                mat[i][j]= false; // нулим чтоб навреняка!
        i=0;
        j=0;
        res= 0;
        o= false;
        scanf("%s", &pat);
        while (pat[i]!='\0') {
            if ( pat[i]=='(' ){
                o= true;
            }
            else if ( pat[i]==')' ) {
                o= false;
                j++; /* инкуем в 2х случаях: 
                        - если закрыли скобку
                        - если o= false, т.е. мы не в скобках, а читаем подряд
                        */
            } 
            else {
                mat[j][pat[i]]= true;
                if (!o)
                    j++;
            }
            i++;
        }
        for(i=1; i<=d; i++) {
            o= true;
            for(j=0; j<l; j++)
                if ( mat[j][mas[i][j]]==false ) { //Тупо провреяем по патрице если ве поодши то инкуем
                    o= false;
                    break;
                }
            if (o)
                res++;
        }
        printf("Case #%d: %d\n", k, res);
    }
    return 0;
    //Сложность 5000*500*15 - пролезет!
}