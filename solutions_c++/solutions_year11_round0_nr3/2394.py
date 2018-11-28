#include <cstdlib>
#include <iostream>

using namespace std;

int c[1001];


int main(int argc, char *argv[])
{
    int t;
    int total,xtotal;
    int n,min;
    char rb;
    scanf("%d", &t);
    for (int i=1; i<=t; i++){
        scanf("%d",&n);
        total = 0;
        xtotal = 0;
        min = 1000000;
        for(int j=0; j<n ; j++){
            scanf("%d", &c[j]);
            if (c[j]<min) min = c[j];
            total = total + c[j];
            xtotal = xtotal ^ c[j];
        }
        printf("Case #%d: ",i);
        if (xtotal == 0) printf("%d\n",total-min);
        else printf("NO\n");
    }
 //   system("PAUSE");
    return EXIT_SUCCESS;
}
