#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    int no_cases;
    cin >> no_cases;
    for (int c = 1; c <= no_cases; ++c) {
        int no_chickens = 0;
        int want_get = 0;
        int barn = 0;
        int time = 0;
        cin >> no_chickens >> want_get >> barn >> time;
        vector<int> locations(no_chickens);
        vector<int> speeds(no_chickens);
        for (int i = 0; i < no_chickens; ++i)
            cin >> locations[i];
        for (int i = 0; i < no_chickens; ++i)
            cin >> speeds[i];

        int slow_ahead = 0;
        int got = 0;
        int lifts = 0;
        for (int i = no_chickens - 1; i >= 0; --i) {
            if (got >= want_get)
                break;
            if (speeds[i] * time >= barn - locations[i]) {
                lifts += slow_ahead;
                ++ got;
            }
            else {
                ++ slow_ahead;
            }
        }
        if (got >= want_get)
            cout << "Case #" << c << ": " << lifts << endl;
        else
            cout << "Case #" << c << ": IMPOSSIBLE" << endl;

    }
}
