#include <cstdio>

int n, lung, tst;
unsigned word[10000][22], testWord[22];

bool match(unsigned a[], unsigned b[]){
    for (int i=0; i<lung; i++)
        if ((a[i] & b[i]) == 0)
            return false;
    return true;
}

void solve(){
    char lin[1024];
    scanf("%s\n", lin);
    int poz = 0;
    for (int i=0; i<lung; i++, poz++)
        if (lin[poz] != '(')
            testWord[i] = 1u << (lin[poz] - 'a');
        else{
            poz++;
            testWord[i] = 0;
            while (lin[poz] != ')')
                testWord[i] |= 1u << (lin[poz++] - 'a');
        }
    int sol = 0;
    for (int i=0; i<n; i++)
        if (match(word[i], testWord))
            sol++;
    printf("%d\n", sol);
}

int main(){
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    scanf("%d %d %d\n", &lung, &n, &tst);
    for (int i=0; i<n; i++){
        char lin[1024];
        scanf("%s\n", lin);
        for (int j=0; j<lung; j++)
            word[i][j] = 1u << (lin[j] - 'a');
    }
    for (int i=1; i<=tst; i++){
        printf("Case #%d: ", i);
        solve();
    }
}
