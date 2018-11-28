#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <string>
#include <vector>
#include <algorithm>

typedef long long i64;

using namespace std;

const string sample = "welcome to code jam";
string str;

i64 memo[500][20];
bool mark[500][20];

i64 DP(int stri, int sami) {
    if(sami == 19) return 1;
    if(stri >= str.size())
        return 0;
    if(mark[stri][sami]) return memo[stri][sami];
    mark[stri][sami] = true;
    i64 &count = memo[stri][sami];
    count = 0;
    count = DP(stri+1, sami);
    if(str[stri] == sample[sami])
        count += DP(stri+1, sami+1);
    return count;
}

int main() {
    
    #ifndef ONLINE_JUDGE
        freopen("C-small.in", "r", stdin);
        freopen("C-small.out", "w", stdout);
    #endif
    
    int N; scanf("%d\n", &N);
    char buff[501];
    for(int i=0; i<N; ++i) {
        fgets(buff, 501, stdin);
        memset(mark, 0, sizeof(mark));
        str = buff;
        //printf("%s\n", str.c_str());
        printf("Case #%d: %.4d\n", i+1, DP(0,0)%10000);
    }    
    return 0;
}
