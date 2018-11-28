#include <cstdio>
#include <cstring>
using namespace std;

char dict[30];

int main()
{
    FILE *fin = fopen("A-small-attempt1.in","r");
    FILE *fout = fopen("A-small-attempt1.out","w");

    char gg[] = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
    char ss[] = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
    for(int i = 0; i < strlen(gg); i++)
    {
        dict[gg[i]-'a'] = ss[i];
    }
    dict['z'-'a'] = 'q';
    dict['q'-'a'] = 'z';

    for(int i = 0; i< 30; i++)
    {
        printf("%c %c\n", 'a'+i,dict[i]);
    }

    int T;
    char g[200];

    fscanf(fin, " %d ", &T);
    for(int t = 1; t <= T; t++)
    {
        fscanf(fin, " %[^\n]s ", g);
        for(int i = 0; i < strlen(g); i++)
        {
	if(g[i] != ' ')
	{
	    g[i] = dict[g[i]-'a'];
	}
        }
        fprintf(fout, "Case #%d: %s\n", t, g);
    }
    return 0;
}
