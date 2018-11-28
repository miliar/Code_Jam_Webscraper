#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

char str[30];

unsigned long long int n;

int i, tt, tam, C =1, T;

bool cmp (char a, char b) {
    return a > b;
}

int main() {


scanf("%d",&T);
while (T--) {

    memset(str,'0',sizeof(str));
    scanf("%s",str);
    int j = strlen(str)-1;
    for (int i=0;i<strlen(str)/2;i++) {
        char k = str[i];
        str[i] = str[j];
        str[j] = k;
        j--;
    }
    str[strlen(str)] = '0';
    tam = strlen(str)+1;
    str[tam-1] = '\0';

    //1. descobre ate onde
    int casas = 2;
    while (true) {
        char eu = str[casas-1];
        char menormaiorqeu = 0x3f;
        int indx = -1;
        for (int i=0;i<casas-1;i++)
            if (str[i] > eu and str[i] < menormaiorqeu) {
                menormaiorqeu = str[i];
                indx = i;
            }
        if (menormaiorqeu == 0x3f)
            { casas++; continue; }
        else {
            char aux = str[casas-1];
            str[casas-1] = str[indx];
            str[indx] = aux;
            sort(str,str+casas-1,cmp);
            break;
        }
    }


    printf("Case #%d: ",C++);
    int i;
    for (i=tam-4;i>=0;i--)
        if (str[i] != '0') { break; }
    for (;i>=0;i--)
        printf("%c",str[i]);
    printf("\n");
}
    return 0;
}
