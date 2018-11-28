
#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;
typedef vector<int> VI;

const int JUDGES = 3;

int doit(VI &totals, int surprises, int min_best)
{
    int n = 0;
    
    int googlers = totals.size();

    sort(totals.begin(), totals.end());

    int used_surprises = 0;
    
    for (int i = 0; i < googlers; i++) {
        bool used_surprise = false;
        int &total = totals[i];
        int max_best = total / JUDGES;
        
        if (total % JUDGES > 0) {
            max_best++;
        }
        
        if (max_best > 0 && max_best < 10 && used_surprises < surprises && total % JUDGES != 1) {
            max_best++;
            used_surprise = true;
        }
        
        if (max_best >= min_best) {
            n++;
            used_surprises += used_surprise ? 1 : 0;
        }
    }
    
    return n;
}

int main(int argc, char **argv)
{
    int num_tests;
    
    cin >> num_tests;
    for (int i = 0; i < num_tests; i++) {
        
        int num_googlers;
        int num_surprises;
        int min_best_result;
        VI totals;

        cin >> num_googlers;
        cin >> num_surprises;
        cin >> min_best_result;

        totals.resize(num_googlers);
        
        for (int j = 0; j < num_googlers; j++) {
            int total;
            cin >> totals[j];
        }

        cout << "Case #" << i+1 << ": "
             << doit(totals, num_surprises, min_best_result) << endl;
    }
}
