#include <cstdio>
#include <algorithm>
#include <list>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
#include <cctype>

using namespace std;

char Tab[50];

int main() {
    int lw;
    scanf("%d",&lw);

    for (int L=1;L<=lw;L++) {
        scanf("%s",Tab);
        int n = strlen(Tab);
        bool res = next_permutation(Tab,Tab+n);
        printf("Case #%d: ",L);
        if (res) {
            printf("%s\n",Tab);
        } else {
            Tab[n++] = '0';
            Tab[n] = '\0';
            sort(Tab,Tab+n);
            for (int i=0;i<n;i++)
                if (Tab[i]>'0') {
                    swap(Tab[0], Tab[i]);
                    break;
                }
            printf("%s\n",Tab);
        }
    }
    
    return 0;
}
