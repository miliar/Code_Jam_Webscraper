#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

#define pb push_back
#define mp make_pair
#define pii pair <int, int>


using namespace std;

int getnum(vector<int> v)
{
    int ans = 0;
    for (int i = 0; i < v.size(); i++)
    {
        ans *= 10;
        ans += v[i];
    }
    return ans;
}

bool check(int a, int b)
{
    vector <int> v;
    while (a)
    {
        v.push_back(a%10);
        a /= 10;
    }
    reverse(v.begin(), v.end());

    for (int i = 0; i < v.size(); i++)
    {
        for (int j = 1; j < v.size(); j++)
        {
            swap(v[0], v[j]);
        }
        if (getnum(v) == b)
        {
            return 1;
        }
    }

    return 0;

}

int main()
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    int t;
    cin >> t;

    check(23, 32);

    for (int tc = 1; tc <= t; tc++)
    {
        cerr << tc << endl;
        int a, b;
        int ans = 0;
        cin >> a >> b;
        for (int i = a; i <= b; i++)
        {
            for (int j = i+ 1; j <= b; j++)
            {
                if (check(i, j)) ans++;
            }
        }

        cout << "Case #" << tc << ": " << ans << endl;
    }


    return 0;
}
