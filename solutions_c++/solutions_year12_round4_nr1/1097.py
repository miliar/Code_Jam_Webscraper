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

    long long r;
    cin >> r;
    for(long long test = 1; test <= r; test++)
    {
        int n;
        cin >> n;
        vector<pair<int ,int> > V;
        vector<int> D(n + 1, -1);
        for(int i = 0; i < n; i++)
        {
            int d ,l;
            cin >> d >> l;
            V.pb(mp(d, l));
        }
        int G;
        cin >> G;
        V.pb(mp(G, 0));
        V[0].first = min(V[0].first, V[0].second);
        D[0] = V[0].first;
        for(int i = 0; i <= n; i++)
        {
            if(D[i] == -1)
            {
             //   cout << i << " " << " cont " << endl;
                continue;
            }
            int maxD = 0;
            for(int j = i + 1; j < V.size(); j++)
            {
           //     cout << i << " " << V[j].first - V[i].first << " " << D[i] << endl;
                if(V[j].first - V[i].first <= D[i])
                {
                    D[j] = max(D[j], min(V[j].first - V[i].first, V[j].second));
                }
            }
            //cout << i << " " << D[i] << endl;
        }
        cout << "Case #"<< test<<": ";
        if(D[n] == -1)
            cout << "NO" << endl;
        else
            cout << "YES" << endl;
    }

    return 0;
}
