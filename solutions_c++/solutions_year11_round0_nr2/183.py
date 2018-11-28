#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <algorithm>
#include <string>
#include <cmath>

#define D(x) x

using namespace std;

template<typename T>
ostream& operator <<(ostream& os, vector<T> v) {
    os << "[";
    for (int i = 0; i < v.size(); i++) {
        if (i > 0) os << ", ";
        os << v[i];
    }
    os << "]";
    return os;
}

int main() {
    int T;

    cin >> T;
    for (int testCase = 1; testCase <= T; testCase++) {
        int C;
        cin >> C;

        vector<string> combinations;
        string tmp;
        for (int i = 0; i < C; i++) {
            cin >> tmp;
            combinations.push_back(tmp);
            swap(tmp[0], tmp[1]);
            combinations.push_back(tmp);
        }
        C = combinations.size();

        int D;
        cin >> D;
        vector<string> opposed;
        for (int i = 0; i < D; i++) {
            cin >> tmp;
            opposed.push_back(tmp);
            swap(tmp[0], tmp[1]);
            opposed.push_back(tmp);
        }
        D = opposed.size();

        int N;
        cin >> N;
        string seq;
        cin >> seq;

        vector<char> elements;
        for (int i = 0; i < N; i++) {
            elements.push_back(seq[i]);
            int l = elements.size();

            bool replaced=false;
            for (int j = 0; j < C; j++) {
                if (elements[l-1] == combinations[j][0] 
                        && elements[l-2] == combinations[j][1]) {
                    elements.pop_back();
                    elements[l-2] = combinations[j][2];
                    replaced=true;
                    break;
                }
            }
            if (replaced) continue;

            for (int j = 0; j < D; j++) {
                if (elements[l-1] == opposed[j][0]
                        && find(elements.begin(), elements.end(), 
                            opposed[j][1]) != elements.end())
                    elements.clear();
            }
        }
        cout << "Case #" << testCase << ": " << elements << endl;
    }
}

