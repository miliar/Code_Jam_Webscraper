#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char change[26];

void prepare()
{
    char s1[] = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
    char s2[] = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
    
    for (int i = 0; i < 26; ++i)
        change[i] = 0;
    for (int i = 0; i < strlen(s1); ++i){
        if (s1[i]>='a' && s1[i]<='z') 
           change[(int)(s1[i] - 'a')] = s2[i];
    }
    change[25] = 'q';
    change[16] = 'z';
}
     
int main()
{
    int n;
    char c;
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    prepare();
    scanf("%d\n", &n);
    for (int i = 1; i <= n; ++i){
        printf("Case #%d: ", i);
        while (scanf("%c", &c), c!='\n')
              if (c<'a' || c >'z') printf(" "); else printf("%c", change[c-'a']);
        printf("\n");
    }              
                  
    return 0;
}
