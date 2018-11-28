#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

int it, n, k1, k2, ind1[1000], ind2[1000], t1[1000], t2[1000], p1, p2, l1, l2;

void read ()
{
    cin >> n;
    k1 = k2 = 0;
    for (int i = 0; i < n; ++i)
    {
        char c;
        cin >> c;
        if (c == 'O')
        {
            t1[k1] = i;
            cin >> ind1[k1++];
        }
        else
        {
            t2[k2] = i;
            cin >> ind2[k2++];
        }
    }
    p1 = p2 = 1;
    l1 = l2 = 0;
}

int mv ()
{
    int dis = min( abs( p1 - ind1[l1] ), abs( p2 - ind2[l2] ) );
    if (dis == 0) return 0;
    p1 += ((ind1[l1] - p1) / abs(ind1[l1] - p1)) * dis;
    p2 += ((ind2[l2] - p2) / abs(ind2[l2] - p2)) * dis;
    return dis;
}

void solve ()
{
    /*for (int i = 0; i < k1; ++i)
        cout << ind1[i] << " ";
    cout << endl;
    for (int i = 0; i < k2; ++i)
        cout << ind2[i] << " ";
    cout << endl;*/
    int cnt = 0;
    while (l1 < k1 && l2 < k2)
    {
        int cp = ( (t1[l1] < t2[l2])?(1):(2) );
        cnt += mv();

        if (cp == 1 && p1 == ind1[l1])
        {
            //cout << "O eat " << ind1[l1] << " at time " << cnt << endl;
            cnt++;
            l1++;
            if (p2 < ind2[l2])
                p2++;
            else if (p2 > ind2[l2])
                p2--;
            continue;
        }

        if (cp == 2 && l1 < k1 && p2 == ind2[l2])
        {
            //cout << "B eat " << ind2[l2] << " at time " << cnt << endl;
            cnt++;
            l2++;
            if (p1 < ind1[l1])
                p1++;
            else if (p1 > ind1[l1])
                p1--;
            continue;
        }

        cnt += max( abs( p1 - ind1[l1] ), abs( p2 - ind2[l2] ) );
        p1 = ind1[l1];
        p2 = ind2[l2];
    }

    for (; l1 < k1; ++l1)
    {
        cnt += abs(ind1[l1] - p1) + 1;
        p1 = ind1[l1];
    }
    for (; l2 < k2; ++l2)
    {
        cnt += abs(ind2[l2] - p2) + 1;
        p2 = ind2[l2];
    }

    cout << cnt << endl;
}

int main ()
{
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );

    cin >> it;
    for (int i = 0; i < it; ++i)
    {
        read();
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
