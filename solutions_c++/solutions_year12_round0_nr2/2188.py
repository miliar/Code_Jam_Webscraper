#include <iostream>

using namespace std;

int main ()
{
    cout.sync_with_stdio(false);
    long cases;
    cin >> cases;
    for (long i = 1; i <= cases; ++i) {
        long n_googlers, n_surprising, p, points, total = 0;
        cin >> n_googlers >> n_surprising >> p;
        
        while (n_googlers --> 0) {
            cin >> points;

            // nice cases
            if (points % 3 == 0 && points / 3 >= p && points / 3 >= 0) {
                total++;
            } else if ((points + 2) % 3 == 0 && (points + 2) / 3 >= p && (points + 2) / 3 - 1 >= 0) {
                total++;
            } else if ((points + 1) % 3 == 0 && (points + 1) / 3 >= p && (points + 1) / 3 - 1 >= 0) {
                total++;
            }
            else if (n_surprising > 0) { //suprising cases
                if ((points + 3) % 3 == 0 && (points + 3) / 3 >= p && (points + 3) / 3 - 2 >= 0) {
                    n_surprising--;
                    total++;
                }
                else if ((points + 4) % 3 == 0 && (points + 4) / 3 >= p && (points + 4) / 3 - 2 >= 0) {
                    n_surprising--;
                    total++;
                }
            }
        }
        cout << "Case #" << i << ": " << total << "\n";
    }
    return 0;
}