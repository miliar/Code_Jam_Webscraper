#include <iostream>
#include <algorithm>
#include <cmath>
#define mp make_pair
#define x first
#define y second
using namespace std;

void solve_case(int case_id)
{
    int i, mom = 0, N, pos;
    char wh;
    pair<int, int> red = mp(0, 1), blue = mp(0, 1); // vreme, poziciq
    cin >> N;
    for(i = 0; i < N; ++i)
    {
        cin >> wh >> pos;
        if(wh == 'B')
        {
            int t1 = blue.x + abs(pos - blue.y);
            if(t1 > mom) mom = t1;
            blue = mp(mom + 1, pos);
        }
        else
        {
            int t1 = red.x + abs(pos - red.y);
            if(t1 > mom) mom = t1;
            red = mp(mom + 1, pos);
        }
        ++mom;
    }
    cout << "Case #" << case_id <<": " << mom << '\n';
}

int main()
{
    int i, t;
    cin >> t;
    for(i = 1; i <= t; ++i) solve_case(i);
    return 0;
}
