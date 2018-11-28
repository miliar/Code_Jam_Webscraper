
#include <iostream>
#include <vector>
#include <list>

using namespace std;



void
do_test(int test_num, vector<int> &candies)
{
    int xs = 0;
    int sum = 0;
    int min = 1000001;
    for (int i = 0; i < candies.size(); i++) {
        xs ^= candies[i];
        sum += candies[i];
        if (candies[i] < min) {
            min = candies[i];
        }
    }

    cout << "Case #" << test_num << ": ";
    if (xs == 0) {
        cout << sum - min;
    } else {
        cout << "NO";
    }
    cout << endl;

}

int
main(int argc, char **argv)
{
    int num_tests = 0;

    cin >> num_tests;

    for (int i = 1; i <= num_tests; ++i) {
        int num_candies = 0;
        int val;
        vector<int> candies;
        
        cin >> num_candies;
        for (int j = 0; j < num_candies; j++) {
            cin >> val;
            candies.push_back(val);
        }

        do_test(i, candies);
    }
}
    
