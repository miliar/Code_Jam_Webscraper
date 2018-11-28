#include <iostream>
#include <vector>
#include <stdio.h>
#include <cstring>
#include <string>
#include <cmath>
using namespace std;

#define PI acos(-1.0)
#define read(x) scanf("%d",&x)
#define write(x) printf("%d",x)
#define writeln(x) printf("%d",x)
int tc,i;
long long u,k,n;
int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    read(tc);
    for (int i=1;i<=tc;++i)
    {

        read(n);
        read(k);
        u=1;
        for (int j=1;j<=n;++j) u*=2;
        printf("%s%d%s","Case #",i,": ");
        if (k%u!=u-1)
            puts("OFF");
        else
            puts("ON");
    }
	return 0;
}
