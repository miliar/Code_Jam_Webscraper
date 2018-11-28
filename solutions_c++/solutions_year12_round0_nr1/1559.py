#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>

using namespace std;
char translate[27] = "yhesocvxduiglbkrztnwjpfmaq";

int main(int argc, char *argv[])
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t_size;
    scanf("%d\n", &t_size);

    char str[110];
    for(int i=0;i<t_size;i++)
    {
        gets(str);
        printf("Case #%d: ", i+1);
        unsigned len = strlen(str);
        for(int j=0;j<len;j++)
            if(str[j] == ' ')
                putchar(' ');
            else
                putchar(translate[str[j]-'a']);
        putchar('\n');
    }
	return 0;
}
