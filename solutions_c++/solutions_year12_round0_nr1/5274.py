#include <cstdio>
#include <cstring>
char f[]="ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
char g[]="ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
char a['z'], s[200], t[200];
bool u['z'];
int n;
int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A1.out", "w", stdout);
    for(int i=0; i<strlen(f); i++)
        a[f[i]] = g[i], u[f[i]] = 1;
    a['z'] = 'q', u['q'] = 1;
    for(int i='a'; i<='z'; i++)
        if(!u[i]) a[0] = i;
    for(int i='a'; i<='z'; i++)
        if(!a[i]) a[i] = a[0];
    for(int i='a'; i<='z'; i++)
        fprintf(stderr, "%c", i);
    fprintf(stderr, "\n");
    for(int i='a'; i<='z'; i++)
        fprintf(stderr, "%c", a[i]);
    fprintf(stderr, "\n");
    a[' '] = ' ';
    scanf("%d\n", &n);
    for(int i=1; i<=n; i++) {
        fgets(s, 200, stdin);
        for(int j=0; j<strlen(s); j++)
            t[j] = a[s[j]];
        printf("Case #%d: %s\n", i, t);
    }
    return 0;
}
