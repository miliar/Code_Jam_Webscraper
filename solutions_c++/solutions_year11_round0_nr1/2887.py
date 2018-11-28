#include <iostream>
#include <cstdio>
using namespace std;

int solve(){
    int n;
    scanf("%d", &n);
    int p[2], t[2];
    p[0]=p[1]=1;
    t[0]=t[1]=0;
    int time=0;
    int b;
    char r;
    for (int i=0; i<n; ++i){
        scanf(" %c %d", &r, &b);
        if (r=='O') r=0;
        else r=1;
        time=max(time, t[r]+abs(p[r]-b))+1;
        t[r]=time;
        p[r]=b;
    }
    return time;
}

int main(){
    int t;
    char fin[100], fout[100];
    printf("Input file: ");
    gets(fin);
    printf("Output file: ");
    gets(fout);
    freopen(fin, "r", stdin);
    freopen(fout, "w", stdout);
    scanf("%d", &t);
    for (int i=0; i<t; ++i)
        printf("Case #%d: %d\n", i+1, solve());
}
