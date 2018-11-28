#include <iostream>
#include <map>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>

using namespace std;

typedef map<char, map<char, char> > comboMap;
typedef map<char, vector<char> > oppMap;

string doLine(const string &line);
int reduce100(int num);
vector<string> &split(const string &s, char delim, vector<string> &elems);
vector<string> split(const string &s, char delim);

int main(int argc, char** argv) {
    string first;
    getline(cin, first);
    int n = atoi(first.c_str());
    for (int i = 0; i < n; ++i) {
        string line;
        getline(cin, line);
        string answer = doLine(line);
        cout << "Case #" << (i + 1) << ": " << answer << endl;
    }
    return 0;
}

string doLine(const string &line) {
    vector<string> tokens;
    split(line, ' ', tokens);

    int n = atoi(tokens[0].c_str());
    int pd = atoi(tokens[1].c_str());
    int pg = atoi(tokens[2].c_str());

    int minGameD = reduce100(pd);
    // int minGameG = reduce100(pg);

    if (minGameD > n) {
        return "Broken";
    }
    if (pg == 100 && pd != 100) {
        return "Broken";
    }
    if (pg == 0 && pd != 0) {
        return "Broken";
    }

    return "Possible";
}

int reduce100(int num) {
    int ans = 100;
    if (num % 4 == 0) {
        ans /= 4;
    }
    else if (num % 2 == 0) {
        ans /= 2;
    }
    if (num % 25 == 0) {
        ans /= 25;
    }
    else if (num % 5 == 0) {
        ans /= 5;
    }
    return ans;
}

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
