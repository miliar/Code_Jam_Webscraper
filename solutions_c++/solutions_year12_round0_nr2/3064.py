#include <stdio.h>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <ctime>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

#define fi first
#define se second
#define pb(a) push_back(a)
#define mp(a, b) make_pair(a, b)

int D[1000];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    for(int test = 1; test <= n; test++)
    {
        int N, S , p;
        int good = 0;
        cin >> N >> S >> p;
        for(int i = 0; i < N; i++)
            cin >> D[i];
        for(int i = 0; i < N; i++)
        {
            int ans = (D[i] + 2)/ 3;
            if(ans >= p)
                good++;
            else if(ans < p && D[i]/3 == p-2 && D[i] % 3 == 2 &&  S > 0)
            {
                good++;
                S--;
            }
            else if(ans < p && D[i]/3 == p-1 && D[i]%3 == 0 && D[i]/3 > 0 && S > 0)
            {
                good++;
                S--;
            }
        }
        cout << "Case #"<< test<<": " << good << endl;
    }
    return 0;
}
