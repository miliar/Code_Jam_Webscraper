#include <cstdlib>
#include <cstdio>
#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        int sekundy = 0, n;

        cin >> n;

        int bluePozycja = 1, orangePozycja = 1;
        int blueCzas = 0, orangeCzas = 0;

        for (int j = 0; j < n; ++j) {
            int nr;
            char robot;
            cin >> robot >> nr;

            if (robot == 'B') {
                int ile = abs(bluePozycja - nr);
                int ileRzeczywiscie = ile - blueCzas;

                if (ileRzeczywiscie < 0) {
                    ++sekundy;
                    ++orangeCzas;
                    blueCzas = 0;
                    bluePozycja = nr;
                } else if (ileRzeczywiscie == 0) {
                    bluePozycja = nr;
                    blueCzas = 0;
                    ++sekundy;
                    ++orangeCzas;
                } else {
                    sekundy += (ileRzeczywiscie + 1);
                    orangeCzas += (ileRzeczywiscie + 1);
                    blueCzas = 0;
                    bluePozycja = nr;
                }
            } else {
                int ile = abs(orangePozycja - nr);
                int ileRzeczywiscie = ile - orangeCzas;

                if (ileRzeczywiscie < 0) {
                    ++sekundy;
                    ++blueCzas;
                    orangeCzas = 0;
                    orangePozycja = nr;
                } else if (ileRzeczywiscie == 0) {
                    orangePozycja = nr;
                    orangeCzas = 0;
                    ++sekundy;
                    ++blueCzas;
                } else {
                    sekundy += (ileRzeczywiscie + 1);
                    blueCzas += (ileRzeczywiscie + 1);
                    orangeCzas = 0;
                    orangePozycja = nr;
                }
            }
        }

        printf("Case #%d: %d\n", i, sekundy);
    }
    return 0;
}
