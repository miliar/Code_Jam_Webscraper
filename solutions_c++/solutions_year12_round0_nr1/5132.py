#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int map[100];
char chch[200];
int main()
{
    freopen("A-small-attempt1.in","r",stdin );
    //freopen("in.in","r",stdin );
    freopen("out.out","w",stdout );

    char ch[200] = "yeqejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv\0";
    char ch2[200] = "aozourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup\0";

    int len = strlen(ch);
    for(int i = 0;i < len;i++)
    {
        int a = ch[i]-'a';
        int b = ch2[i]-'a';
        map[a] = b;
    }

    map['z'-'a'] = 'q'-'a';

    int t;
    cin >> t;
    getchar();
    for(int i = 0;i < t;i++)
    {

        gets(chch);
        printf("Case #%d: ",i+1);
        for(int j = 0;j < strlen(chch);j++)
        {
            if(chch[j] >= 'a' && chch[j] <= 'z')
                printf("%c",map[chch[j] - 'a']+'a');
            else printf("%c",chch[j]);
        }
        printf("\n");
    }
    return 0;
}
