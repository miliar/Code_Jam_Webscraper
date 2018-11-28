#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

using namespace std;

string bin(double, int);
long ssum(vector<long>);
long psum(vector<long>);

int main() {
    int cases; cin >> cases;
    long answers[cases];
    //cin.clear(); cin.sync();
    for (int t = 0; t < cases; t++) {
        int N; cin >> N;
        long candies[N];
        for (int i = 0; i < N; i++) {
            cin >> candies[i];
        }
        long seanVal = 0;
        for (double i = 1; i < pow(2.0, N)-1; i++) {
            vector<long> sean, patrick;
            string key = bin(i, N);
            for (int j = 0; j < N; j++) {
                key[j] == '1' ? sean.push_back(candies[j]) : patrick.push_back(candies[j]);
            }
            if (psum(sean) == psum(patrick)) {
                if (ssum(sean) >= ssum(patrick) && ssum(sean) > seanVal) seanVal = ssum(sean);
                else if (ssum(patrick) > ssum(sean) && ssum(patrick) > seanVal) seanVal = ssum(patrick);
            }
        }
        answers[t] = seanVal;
    }
    fstream fs ("output.txt", fstream::out);
    for (int t = 0; t < cases; t++) {
        fs << "Case #" << t+1 << ": ";
        if (answers[t] == 0) fs << "NO" << endl;
        else fs << answers[t] << endl;
    }
    return 0;
}

string bin(double n, int s) {
    vector<int> stack;
    while (n >= 1) {
        stack.push_back(int(fmod(n, 2)));
        n = floor(n / 2);
    }if (n > 0) stack.push_back(int(n));
    string result;
    while (stack.size() < s) stack.push_back(0);
    while (!stack.empty()) {
        result.push_back(stack.back() + 48);
        stack.pop_back();
    }
    return result;
}

long ssum(vector<long> pile) {
    long sum = 0;
    for (int i = 0; i < pile.size(); i++) sum += pile[i];
    return sum;
}

long psum(vector<long> pile) {
    long sum = 0;
    for (int i = 0; i < pile.size(); i++) sum ^= pile[i];
    return sum;
}
