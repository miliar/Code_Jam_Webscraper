#include <cstdio>
#include <cctype>
char map[] = "yhesocvxduiglbkrztnwjpfmaq";
char *buf;
int main()
{
    int n;
    size_t m=101;
    buf = new char[102];
    scanf("%d\n",&n);
    for (int i=1; i<=n; i++)
    {
        getline(&buf, &m, stdin);
        for (int j=0; j<m; j++)
            if (islower(buf[j]))
                buf[j] = map[buf[j]-'a'];
            else if (isupper(buf[j]))
                buf[j] = 'A' + map[buf[j]-'A'];
        
        printf("Case #%d: %s",i, buf);
    }
}
