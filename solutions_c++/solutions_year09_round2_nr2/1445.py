#include <cstdio>
#include <cstring>
#include <algorithm>
#include <functional>

using namespace std;

int main(int argc, char **argv) {
    int T, len, inx;
    char *itr = NULL;
    char buf[21], num[21];
    scanf("%d", &T);
    for(int i=0; i<T; ++i) {
        scanf("%s", buf);
        len = strlen(buf);
        inx = 20 - len;
        fill(num, num+inx, '0');
        copy(buf, buf+len+1, num+inx);
        next_permutation(num, num+20);
        itr = find_if(num, num+20, bind2nd(not_equal_to<int>(), '0'));
        inx = (itr == num+20) ? 0 : (itr-num);        
        printf("Case #%d: %s\n", i+1, num+inx);
    }
    return 0;
}
