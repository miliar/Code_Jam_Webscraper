#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    char in[] = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvqz";
    char out[]= "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupzq";

    char mapping[26] = {0};

    for(int i = 0; in[i]; i++)
    {
        if(mapping[in[i]-'a'] == 0)
        {
            mapping[in[i]-'a'] = out[i];
        }
    }

    int n;
    char str[200];
    scanf("%d\n", &n);

    for(int i = 0; i < n; i++)
    {
        printf("Case #%d: ", i+1);
        gets(str);

        for(int j = 0; str[j]; j++)
        {
            if(str[j] == ' '){putchar(' ');}
            else{putchar(mapping[str[j]-'a']);}
        }
        putchar('\n');
    }
}