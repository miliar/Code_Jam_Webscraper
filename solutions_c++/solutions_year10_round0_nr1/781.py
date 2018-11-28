#include <cstdio>
using namespace std;

int main() {
    int j;
    scanf("%d",&j);
    for(int c=1;c<=j;c++) {
        int n,k;
        scanf("%d%d",&n,&k);
        bool result = (k%(1<<n))==((1<<n)-1);
        printf("Case #%d: %s\n",c,result?"ON":"OFF");
    }
    return 0;
}


