#include <cstdio>
//char p[26]="                q        z";
  char p[27]="yhesocvxduiglbkrztnwjpfmaq";
char s[1000];
int  tc;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    gets(s);
    sscanf(s, "%i", &tc);
    for(int tt=1; tt<=tc; ++tt)
    {
        gets(s);
        for(int i=0; s[i]; ++i) if (s[i] >= 'a' && s[i] <= 'z') s[i] = p[s[i]-'a'];
        printf("Case #%i: %s\n", tt, s);
    }
}