#include <cmath>
#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
    int j;
    scanf("%d",&j);
    for(int cn=1;cn<=j;cn++) {
        int a=1,b=1,t=0,ta=0,tb=0,n;
        scanf("%d",&n);
        while(n--) {
            char buf[3];
            int x;
            scanf("%s%d",buf,&x);
            if (buf[0]=='O') {
                int dt = 1 + max(0, abs(x-a)-(t-ta));
                t += dt;
                ta = t;
                a = x;
            } else {
                int dt = 1 + max(0, abs(x-b)-(t-tb));
                t += dt;
                tb = t;
                b = x;
            }
        }
        printf("Case #%d: %d\n",cn,t);
    }
    return 0;
}



