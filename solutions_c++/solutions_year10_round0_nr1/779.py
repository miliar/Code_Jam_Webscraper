#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <cassert>
using namespace std;
void problem(int id)
{
    int n, k;
    assert(2 == scanf("%d%d", &n, &k));
    printf("Case #%d: ", id + 1);
    printf("%s\n", k & 1 && k + 1 >= 2 * n ? "ON" : "OFF");
}
int main(int argc, char **argv)
{
    int n;
    assert(1 == scanf("%d", &n));
    int id = 0;
    while (n--) {
        problem(id++);
    }
    return 0;
}
