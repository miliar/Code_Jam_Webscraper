#include <iostream>
#include <vector>

using namespace std;

void readInstance(vector<int>* input) {
    int n;
    cin >> n;

    for(int i = 0; i < n; ++i) {
        int c;
        cin >> c;
        input->push_back(c);
    }
}



int solve(const vector<int>& permutation) {
    int fixed_points = 0;
    for(int i = 0; i < permutation.size(); ++i) {
        if(permutation[i] == i + 1) {
            ++fixed_points;
        }
    }
    return permutation.size() - fixed_points;
}

void output(int caseNo, int answer) {
    cout << "Case #" << caseNo << ": " << answer << endl;
}

int main() {
    int n;
    cin >> n;
    for(int i = 0; i < n; ++i) {
        vector<int> input;
        readInstance(&input);
        output(i + 1, solve(input));
    }
    return 0;
}
