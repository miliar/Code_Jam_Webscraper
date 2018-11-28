#include <algorithm>
#include <iostream>
#include <iterator>
#include <fstream>
#include <numeric>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::string;
using std::vector;

typedef vector<int> Candies;

int XOR(const int& a, const int& b) {
    return a^b;
}

int IncorrectAddition(const vector<int>& values) {
    return std::accumulate(values.begin(),values.end(),0,XOR);
}

vector<Candies> ParseInput(const string& filename) {

    vector<Candies> res;
    std::ifstream fin;
    fin.open(filename.c_str(), std::ifstream::in);
    if (fin.fail()) {
        cout << "Failed to open " << filename << endl;
        return res;
    }

    int num_sequences;
    fin >> num_sequences;
    for (int i = 0; i < num_sequences; ++i) {
        int num_candies;
        fin >> num_candies;
        Candies sequence(num_candies, 0);
        for (int j = 0; j < num_candies; ++j)
            fin >> sequence[j];
        res.push_back(sequence);
    }

    return res;
}

int main(int argc, char** argv) {

    vector<Candies> all_candy_sequences = ParseInput(string(argv[1]));
    //std::copy(all_candy_sequences[0].begin(),all_candy_sequences[0].end(),std::ostream_iterator<int>(cout, " "));

    std::ofstream fout;
    fout.open("output.txt", std::ofstream::out);
    if (fout.fail()) {
        cout << "Failed to open output.txt for writing." << endl;
        return 1;
    }

    int num_sequences = all_candy_sequences.size();
    for (int i = 0; i < num_sequences; ++i) {
        Candies sequence = all_candy_sequences[i];
        fout << "Case #" << i+1 << ": ";
        int incorrect_sum = IncorrectAddition(sequence);
        if (incorrect_sum != 0) {
            fout << "NO" << endl;
            continue;
        }
        // key observation, if a sequence is splittable (its XOR == 0), then whichever way it is splitted, both subsets will yield the same XOR!
        // Hence, to maximize Sean's profit, just leave the candy with the least value to Patrick
        int min_val = *(std::min_element(sequence.begin(), sequence.end()));
        int all_candies = std::accumulate(sequence.begin(),sequence.end(),0);
        fout << all_candies - min_val << endl;
    }
    fout.close();
    return 0;
}
