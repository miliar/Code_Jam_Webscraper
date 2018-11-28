#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <list>
#include <stack>
#include <queue>
#include <vector>
#include <cctype>
#include <cmath>

using namespace std;

char *ptr = " welcome to code jam";
const int MOD = 10000;

int main() {
    int lw;
    scanf("%d",&lw);
    for (int L=1;L<=lw;L++) {
        char c = getchar();
        while ( !(c>='a' && c<='z') )
            c=getchar();

        int ile[20];
        int nile[20];
        for (int i=0;i<20;i++) 
            ile[i] = 0;
    
        ile[0] = 1;
        int m = strlen(ptr);

        while (c!='\n') {
            for (int i=1;i<m;i++) {
                for (int j=0;j<20;j++)
                    nile[j] = ile[j];
                if (ptr[i] == c) {
                    nile[i] = (nile[i] + ile[i-1])%MOD;
                }
                for (int j=0;j<20;j++)
                    ile[j] = nile[j];
            }
            c = getchar();
        }
        printf("Case #%d: %04d\n",L,ile[m-1]);
    }
    return 0;
}
