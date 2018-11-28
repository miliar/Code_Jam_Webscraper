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
    int n;
    assert(1 == scanf("%d", &n));
    vector < pair < int, int > > vec;
    for (int i = 0; i < int (n); ++i) {
        int a, b;
        assert(2 == scanf("%d%d", &a, &b));
        vec.push_back(make_pair(a, b));
    }
    int tot = 0;
    for (int i = 0; i < int (n); ++i)
        for (int j = 0; j < int (i); ++j)
            tot +=
             (vec[i].first < vec[j].first) != (vec[i].second < vec[j].second);
    printf("Case #%d: %d\n", id + 1, tot);
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
