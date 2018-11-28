#include <stdio.h>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <ctime>
#include <vector>
#include <utility>
#include <algorithm>
#include <set>
using namespace std;

#define fi first
#define se second
#define pb(a) push_back(a)
#define mp(a, b) make_pair(a, b)

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int r;
    cin >> r;
    for(int test = 1; test <= r; test++)
    {
        int good = 0;
        int n ,m;
        cin >> n >> m;
        for(int i = n; i <= m; i++)
        {
            set<int> Set;
            //cout << "i = " << i << endl;
            int maxdeg = 10;
            while(maxdeg <= i){
                maxdeg *= 10;
            }
            int deg = 10;
            while(deg < maxdeg)
            {
                int f = i % deg;
                int s = i / deg;
                int num = f * maxdeg/deg + s;
               // cout << num << endl;
                if(num > i && num >= n && num <= m && Set.find(num) == Set.end())
                {
                    Set.insert(num);
                    good++;
                }
                deg *= 10;
            }
        }
        cout << "Case #"<< test<<": " << good << endl;
    }

    return 0;
}
