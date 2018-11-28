#include <string.h>
#include <iostream>
#include <cstdio>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <cmath>
#include <string>
#include <map>
#include <cassert>
#include <queue>

using namespace std;

#define forn(i, n)  for (int i = 0; i < int(n); i++)

vector<int> a;
int n;

void read()
{
    a.clear();
    cin >> n;
    a.resize(n);
    forn(i, n)
        cin >> a[i];
}

void process()
{
    int sum = 0;
    forn(i, n)
        sum = (sum ^ a[i]);
    if (sum == 0)
    {
        sum = 0;
        sort(a.begin(), a.end());
        forn(i, n)
            if (i > 0)
                sum += a[i];
        cout << sum << endl;
        sum = 0;
        forn(i, n)
            if (i > 0)
                sum = sum ^ a[i];
        assert(sum == a[0]);
    }
    else
        cout << "NO" << endl;
}

int main(int argc, char* argv[])
{
    freopen("input.txt", "rt", stdin);
    
    int cases;
    scanf("%d", &cases);

    int from = (argc > 1 ? atoi(argv[1]) : 1);
    int to = (argc > 2 ? atoi(argv[2]) : cases);

    for (int i = 1; i <= cases; i++)
    {
        read();
        if (from <= i && i <= to)
        {
            printf("Case #%d: ", i);
            process();
        }
    }

    return 0;
}

