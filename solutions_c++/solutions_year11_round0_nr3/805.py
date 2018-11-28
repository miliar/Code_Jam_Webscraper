#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

void Solve(int testid, const vector<int>& candy) {
    fout << "Case #" << testid + 1 << ": ";
    int patric_sum = 0;
    for (int i = 0; i < candy.size(); ++i)
        patric_sum ^= candy[i];
    if (patric_sum) {
        fout << "NO\n";
        return;
    }
    int minidx = 0;
    int sum = candy[0];
    for (int i = 1; i < candy.size(); ++i) {
        sum += candy[i];
        if (candy[i] < candy[minidx])
            minidx = i;
    }
    patric_sum = 0;
    for (int i = 0; i < candy.size(); ++i)
        if (i != minidx)
        patric_sum ^= candy[i];
    fout << /*patric_sum << " " << candy[minidx] << " " << */sum - candy[minidx] << endl;
}

int main() {
    int T; fin >> T;
    for (int i = 0; i < T; ++i) {
        int N; fin >> N;
        vector<int> candy(N);
        for (int j = 0; j < N; ++j)
            fin >> candy[j];
        Solve(i, candy);
    }
    return 0;
}