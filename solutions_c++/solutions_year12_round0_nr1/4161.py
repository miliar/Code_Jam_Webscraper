#include <string>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;
typedef long long ll;
// Utilities
#define S(N) scanf("%d", &N)
#define SS(N) scanf("%s", N)
#define FOR(A,B,C) for(int A=B;A<C;++A)
#define RFOR(A,B,C) for(int A=B;A>=C;--A)
#define MEM(A,B) memset(A,B,sizeof(A))
#define MAX(A,B) ((A > B) ? A : B)
#define MIN(A,B) ((A < B) ? A : B)
// Debugging
bool DBG;
#define debug(args...) dbg(),args
struct dbg { template<typename T> dbg& operator , (const T& v) { if(DBG)
cerr << v << " "; return *this; } ~dbg() { if (DBG) cerr << endl; } };

#define MOD 100000007
#define LIM 1000000000

char trans[26];

void learn() {
    char inp[4][101] = {
        "y qee",
        "ejp mysljylc kd kxveddknmc re jsicpdrysi",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv" };
    char res[4][101] = {
        "a zoo",
        "our language is impossible to understand",
        "there are twenty six factorial possibilities",
        "so it is okay if you want to just give up" };
    int i, check = 0;
    FOR(k, 0, 4) {
        int i = -1;
        while(inp[k][++i]) {
            if (inp[k][i] == ' ')
                continue;
            trans[inp[k][i] - 'a'] = res[k][i] - 'a';
            check |= 1<<(res[k][i]-'a');
        }
    }
    int missing = 0, left = 0;
    FOR(i, 0, 26)
        if(trans[i]==0)
            missing = i;
    FOR(i, 0, 26)
        if((check & (1<<i)) == 0)
            left = i;
    trans[missing] = left;
}

int main (int argc, char *argv[]) {
    DBG = (argc > 1 && *argv[1] != '0'); // Set debug on if required
    learn();
    int t;
    scanf("%d\n", &t);
    FOR(k, 0, t) {
        int n; char str[101];
        scanf(" %[^\n]s", str);
        int i=-1;
        while(str[++i]) {
            if(str[i]==' ') continue;
            str[i] = trans[str[i]-'a']+'a';
        }

        printf("Case #%d: %s\n", k+1, str);
    }
    return 0;
}
