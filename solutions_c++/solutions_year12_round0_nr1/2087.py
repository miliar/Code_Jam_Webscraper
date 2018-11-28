#include <cstdio>
#include <cstring>
#include <map>

#define MAX 110

using namespace std;

char linha[MAX];
map<char,char> mapa;
int t;

int main(void){

    freopen("A.in","r",stdin);

    freopen("A.out","w",stdout);

    scanf("%d\n",&t);

    mapa['a']='y';
    mapa['b']='h';
    mapa['c']='e';
    mapa['d']='s';
    mapa['e']='o';
    mapa['f']='c';
    mapa['g']='v';
    mapa['h']='x';
    mapa['i']='d';
    mapa['j']='u';
    mapa['k']='i';
    mapa['l']='g';
    mapa['m']='l';
    mapa['n']='b';
    mapa['o']='k';
    mapa['p']='r';
    mapa['q']='z';
    mapa['r']='t';
    mapa['s']='n';
    mapa['t']='w';
    mapa['u']='j';
    mapa['w']='f';
    mapa['v']='p';
    mapa['x']='m';
    mapa['y']='a';
    mapa['z']='q';

    for(int caso=1;caso<=t;caso++){
        gets(linha);
        int tam=strlen(linha);
        printf("Case #%d: ",caso);

        for(int i=0;i<tam;i++){
            if(linha[i]==' ') printf(" ");
            else printf("%c",mapa[linha[i]]);
        }

        printf("\n");

    }

    return 0;

}
