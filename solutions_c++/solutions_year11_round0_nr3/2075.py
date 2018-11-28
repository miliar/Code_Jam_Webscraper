// C. Candy Splitting.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int t, n;
vector<int> vec;

int main()
{
    //freopen("1.in", "r", stdin);
    //freopen("C-small-attempt0.in", "r", stdin);
    //freopen("C-small-attempt0.out", "w", stdout);
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    cin >> t;
    for (int cc = 1; cc <= t; cc++)
    {
        int temp;
        vec.clear();
        cin >> n;
        for (int i = 0; i < n; i++)
        {
            cin >> temp;
            vec.push_back(temp);
        }

        int res = 0;
        for (int i = 0; i < vec.size(); i++)
        {
            res ^= vec[i];
        }

        cout << "Case #" << cc << ": ";
        if (res != 0)
        {
            cout << "NO" << endl;
            continue;
        }

        sort(vec.begin(), vec.end());
        int sum = 0;
        for (int i = 1; i < vec.size(); i++)
        {
            sum += vec[i];
        }
        cout << sum << endl;
    }
	return 0;
}

