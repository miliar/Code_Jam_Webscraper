#include <iostream>
#include <cstdio>
#include <functional>
#include <algorithm>
#define MAX 810

using namespace std;
int main()
{
    int T,t,n,i;
    int res[31] = { 1, 5, 27, 143, 751, 935, 607, 903,\
		991, 335, 47, 943, 471, 55, 447, 463, 991, 95,607,\
		263, 151, 855, 527, 743, 351, 135, 407, 903, 791, 135, 647};
    scanf("%d",&T);
    for (t = 1;t <= T;t++){
        scanf("%d",&n);
        printf("Case #%d: %03d\n",t,res[n]);
    }
}
