#include<cstdio>
#include<map>
#include<cstring>
using namespace std;
int main() {
    int casesQty;
    map<char, char> letterMap;
    char googlerese[106], english[106];
    char letter;
    strcpy(googlerese,"ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv");
    strcpy(english,"ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup");
    for(int i = 0; i < strlen(googlerese); i++)
        letterMap[googlerese[i]] = english[i];
    letterMap[' '] = ' ';
    letterMap['q'] = 'z';
    letterMap['z'] = 'q';
    scanf("%d ", &casesQty);
    for(int t = 0; t < casesQty; t++) {
        printf("Case #%d: ", t+1);
        do {
            scanf("%c", &letter);
            if(letter == '\n')
                break;
            printf("%c", letterMap[letter]);
        } while(letter != '\n');
        printf("\n");
    }
    return 0;
}
