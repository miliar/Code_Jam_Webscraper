#include <iostream>
#include <map>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>

using namespace std;

string doLine(const string &line, int n);
vector<string> &split(const string &s, char delim, vector<string> &elems);
vector<string> split(const string &s, char delim);

int main() {
    string first;
    getline(cin, first);
    int t = atoi(first.c_str());
    for (int i = 0; i < t; ++i) {
        string line;
        getline(cin, line);
        int n = atoi(line.c_str());
        getline(cin, line);
        string answer = doLine(line, n);
        cout << "Case #" << (i + 1) << ": " << answer << endl;
    }
    return 0;
}

string doLine(const string &line, int n) {
    vector<string> tokens;
    vector<int> values;
    split(line, ' ', tokens);

    unsigned int total = 0;
    int xors = 0;
    int smallest = atoi(tokens[0].c_str());

    for (int i = 0; i < n; ++i) {
        int value = atoi(tokens[i].c_str());
        values.push_back(value);
        total += value;
        xors ^= value;
        if (value < smallest) {
            smallest = value;
        }
    }

    if (xors != 0) {
        return "NO";
    }

    stringstream stream;
    stream << (total - smallest);

    return stream.str();
}

// http://stackoverflow.com/questions/236129/c-how-to-split-a-string
vector<string> &split(const string &s, char delim, vector<string> &elems) {
    stringstream ss(s);
    string item;
    while(getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}

vector<string> split(const string &s, char delim) {
    vector<string> elems;
    return split(s, delim, elems);
}
