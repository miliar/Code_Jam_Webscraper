#include <iostream>

using namespace std;

int L,D,N;
char dict[5001][16];
bool Check(char a[16],int b[16][257]){
         for (int i = 0; i<L; i++)
         if (!b[i+1][a[i]]) return false;
         return true;
}
int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d%d%d\n",&L,&D,&N);
    for (int i = 1; i<=D; i++)
        gets(dict[i]);
    for (int i = 1; i<=N; i++){
        char s[5001];
        gets(s);
        int len = strlen(s);
        int Ans = 0;
        bool boo = false;
        int tmp[16][257] = {0};
        int t = 0;
        for (int j = 0; j<len; j++){
            if (s[j] == '(') boo = true,t++;
            if (s[j] == ')') boo = false;
            if (boo)tmp[t][s[j]] = 1;
            if (!boo) if (s[j]>='a'&&s[j]<='z') tmp[++t][s[j]] = 1;
        }
        for (int j = 1; j<=D; j++)
            if (Check(dict[j],tmp)) Ans++;
        printf("Case #%d: %d\n",i,Ans);
    }
    return 0;
}
