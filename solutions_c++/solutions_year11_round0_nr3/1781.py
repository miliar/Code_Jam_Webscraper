#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

string RunTestCase(const vector<int>& candy_weights) {
    int test = 0, total_sum = 0;
    for (size_t i = 0; i < candy_weights.size(); ++i) {
        test ^= candy_weights[i];
        total_sum += candy_weights[i];
    }
    
    if (test != 0)
        return "NO";
    
    stringstream converter;
    converter << (total_sum - *min_element(candy_weights.begin(), candy_weights.end()));
    return converter.str();
}

int main(int argc, char** argv) {
    int num_test_cases;
    cin >> num_test_cases;
    
    for (int i = 0; i < num_test_cases; ++i) {
        int num_candies;
        cin >> num_candies;
        
        vector<int> candy_weights(num_candies);
        for (int j = 0; j < num_candies; ++j)
            cin >> candy_weights[j];
        
        cout << "Case #" << (i + 1) << ": " << RunTestCase(candy_weights) << endl;
    }
    
    return 0;
}
