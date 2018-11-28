#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<functional>
#include<algorithm>
#include<limits>
#include<utility>
#define PB push_back
#define MP make_pair
#define _F first
#define _S second
#define PP system("PAUSE");

using namespace std;

char conv[1000];
char line[5][100], line1[5][100];
char text[1000];

int main(void){
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small-attempt2.out", "w", stdout);
    for(int i = 'a'; i <= 'z'; i++) conv[i] = i;
    strcpy(line[0], "ejp mysljylc kd kxveddknmc re jsicpdrysi");
    strcpy(line[1], "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    strcpy(line[2], "de kr kd eoya kw aej tysr re ujdr lkgc jv");
    strcpy(line1[0], "our language is impossible to understand");
    strcpy(line1[1], "there are twenty six factorial possibilities");
    strcpy(line1[2], "so it is okay if you want to just give up");
    conv['z'] = 'q';
    conv['q'] = 'z';
    conv['a'] = 'y';
    conv['y'] = 'a';
    conv['o'] = 'e';
    conv['e'] = 'o';
    int len;
    len = strlen(line[0]);
    for(int i = 0; i < len; i++) if(line[0][i] != ' ') conv[line[0][i]] = line1[0][i];
    len = strlen(line[1]);
    for(int i = 0; i < len; i++) if(line[1][i] != ' ')  conv[line[1][i]] = line1[1][i];
    len = strlen(line[2]);
    for(int i = 0; i < len; i++) if(line[2][i] != ' ')  conv[line[2][i]] = line1[2][i];

    int T;
    scanf("%d", &T); getchar();
    for(int i = 1; i <= T; i++){
        gets(text);
        printf("Case #%d: ", i);
        len = strlen(text);
        for(int j = 0; j < len; j++){
            if(text[j] == ' ') printf(" ");
            else printf("%c", conv[text[j]]);
            }
        if(i != T) puts("");
        memset(text, 0, sizeof(text));
        }

    return 0;
    }
