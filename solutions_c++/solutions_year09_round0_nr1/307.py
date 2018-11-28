#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char aux[3000];
int l, d, n;
int v[5002][30];
bool dapra[5002];

void parenteses(char *s, int n, int posicaonodicionario, int posicaonos, int *fechaparenteses) {
    int parenteses = 0;
    int bitmask = 0;
    while (true) {
        if (s[posicaonos] == '(') { parenteses++; posicaonos++; continue; }
        if (s[posicaonos] == ')' and parenteses == 0) {*fechaparenteses = posicaonos; break; }
        if (s[posicaonos] == ')') { parenteses--; }
        bitmask |= 1 << (s[posicaonos]-'a');
        posicaonos++;
    }
    for (int i=0;i<d;i++)
        if (!((v[i][posicaonodicionario] & bitmask) != 0 and dapra[i]))
            dapra[i] = false;
}

bool resp(char *s, int tams, int posnodicionario, int posicaoems) {
    if (posicaoems == tams and posnodicionario < l) return false;
    if (posicaoems == tams) return true;
    if (posnodicionario == l) return false;
    if (s[posicaoems] != '(' and s[posicaoems] != ')') {
        for (int i=0;i<d;i++)
            if (!(v[i][posnodicionario] == 1 << (s[posicaoems]-'a') and dapra[i]))
                dapra[i] = false;
        return resp(s,tams,posnodicionario+1,posicaoems+1);
    }
    if (s[posicaoems] == '(') {
        int fechaparenteses;
        parenteses(s,tams,posnodicionario,posicaoems+1,&fechaparenteses);
        return resp(s,tams,posnodicionario+1,fechaparenteses+1);
    }
}

int main () {

    int C = 1;

    scanf("%d %d %d\n",&l, &d, &n);
    for (int i=0;i<d;i++) {
        scanf("%s\n",aux);
        for (int j=0;j<l;j++)
            v[i][j] = (1<<(aux[j]-'a'));
    }

    for (int i=0;i<n;i++) {
        scanf("%s\n",aux);
        fill(dapra,dapra+d,true);
        if (resp(aux,strlen(aux),0,0)) {
            int tot = 0;
            for (int i=0;i<d;i++)
                if (dapra[i]) tot++;
            printf("Case #%d: %d\n",C++,tot);
        } else
            printf("Case #%d: 0\n",C++);
    }
    return 0;
}
