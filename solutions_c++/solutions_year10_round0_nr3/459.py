#include <iostream>
using namespace std;
long long int solveit() {
    long long int runs, seats, groups;
    long long int group[1001], money[1001], destination[1001], total = 0;
    cin >> runs >> seats >> groups;
    for (int x = 0; x < groups; x++) {
        cin >> group[x];
        total += group[x];
    }

    if (total <= seats)
        return total * runs;

    long long int currentcount = 0, posfill = 0, currentpos = 0;
    while (posfill < groups) {
        if (currentcount +group[currentpos] <= seats) {
            currentcount += group[currentpos++];
            currentpos %= groups;
        } else {
            money[posfill] = currentcount;
            destination[posfill] = currentpos;
            // cout << "DEBUG: " << posfill << " " << money[posfill] << " " << destination[posfill] << endl;
            currentcount -= group[posfill++];
        }
    }

    int queuestate = 0;
    long long int res = 0;
    while (runs--) {
        res += money[queuestate];
        queuestate = destination[queuestate];
    }
    return res;
}
int main() {
    int n;
    cin >> n;
    for (int c = 1; c <= n; c++) cout << "Case #" << c << ": " << solveit() << endl; 
    return 0;
}

