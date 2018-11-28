#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

    typedef set<pair<int, int> > spii;
    spii set1, set2;

int solve()
{
    spii& bacteria = set1;
    spii& next = set2;

    bacteria.clear();
    int R;
    cin >> R;
    for (int r = 0; r < R; r++) {
        int X1, X2, Y1, Y2;
        cin >> X1 >> Y1 >> X2 >> Y2;
        for (int x = X1; x <= X2; x++)
            for (int y = Y1; y <= Y2; y++)
                bacteria.insert(make_pair<int, int>(x, y));
    }
    int answer = 0;
    while (!bacteria.empty()) {
        // cerr << answer << " " << bacteria.size() << endl;
        answer++;
        next.clear();
        for (spii::iterator it = bacteria.begin(); it != bacteria.end(); it++) {
            int x = it->first;
            int y = it->second;
            // remains?
            if (bacteria.find(make_pair<int, int>(x - 1, y)) != bacteria.end() ||
                bacteria.find(make_pair<int, int>(x, y - 1)) != bacteria.end())
            {
                next.insert(make_pair<int, int>(x, y));
            }
            // produces?
            if (bacteria.find(make_pair<int, int>(x + 1, y - 1)) != bacteria.end())
                next.insert(make_pair<int, int>(x + 1, y));
            if (bacteria.find(make_pair<int, int>(x - 1, y + 1)) != bacteria.end())
                next.insert(make_pair<int, int>(x, y + 1));
        }
        swap(bacteria, next);
    }
    return answer;
}

int main()
{
    int C;
    cin >> C;
    for (int c = 1; c <= C; c++) {
        int answer = solve();
        cout << "Case #" << c << ": " << answer << endl;
        cerr << c << endl;
    }
    return 0;
}
