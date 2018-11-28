#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;

int T;
int tam1, tam2;
int PD[550][550];

int resp(const char *s1, const char *s2, int pos1, int pos2) {
    if (s2[pos2] == '\0' and pos1 <= tam1) return 1;
    if (s1[pos1] == '\0') return 0;
    if (PD[pos1][pos2] != ~0) return PD[pos1][pos2];
    int tot = 0;
    if (s1[pos1] == s2[pos2])
        tot = resp(s1,s2,pos1+1,pos2+1)%10000;
    return PD[pos1][pos2] = (tot + resp(s1,s2,pos1+1,pos2))%10000;
}

int main() {

    scanf("%d\n",&T);
    int C = 1;
    while (T--) {
        string S;
        getline(cin,S);
        tam1 = S.length();
        tam2 = 19;
        for (int i=0;i<tam1+5;i++)
            memset(PD[i],~0,(tam2+5)*sizeof(int));
        printf("Case #%d: %.4d\n",C++,resp(S.data(),"welcome to code jam",0,0)%10000);
    }

    return 0;
}
