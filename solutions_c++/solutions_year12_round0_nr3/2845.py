#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <functional>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <iterator>
#include <memory>
#include <utility>

#define DEBUG 0
using namespace std;

void fromInt(std::vector<char>& vec, int val) {
    if (val>0) {
        fromInt(vec, val/10);
        vec.push_back(val%10);
    }
}

bool operator<(vector<char>& lhs, vector<char>& rhs) {
    for (int i=0; i<lhs.size(); ++i) {
        if (lhs[i] < rhs[i]) return true;
        else if (lhs[i]>rhs[i]) return false;
    }
    return false;
}
ostream& operator<<(ostream&os, vector<char>& vec) {
    copy (vec.begin(), vec.end(), ostream_iterator<int>(os));
    return os;
}

void increment(vector<char> & vec) {
#if DEBUG
    cout <<"Increment " << vec;
#endif
    for (int i=vec.size()-1; i>=0; --i) {
        vec[i]+=1;
        if (vec[i]>9) {
            vec[i] -= 10;
        }
        else {
            break;
        }
    }
#if DEBUG
    cout << " Done " << vec << endl;
#endif
}

int main() {
    string line;
    getline(cin, line);
    const int T = atoi(line.c_str());
    for (int t=0; t<T; ++t) {
        getline(cin, line);
        istringstream iss(line);

        int A,B;
        iss >> A >> B;
        vector<char> vecA;
        vector<char> vecB;
        fromInt(vecB, B);
        int digits = vecB.size();
        fromInt(vecA, A);
        vector<char> orig = vecA;
        vector<char> rot;
        int cnt = 0;
        int first = 1;
        do {
            if (!first) increment(orig);
            first = 0;
#if DEBUG
            cout << "Orig: " << orig << endl;
#endif
            rot = orig;
            for (int r = 0; r<digits; ++r) {
                rotate(rot.begin(), rot.begin()+1, rot.end());
                if (rot>orig && rot <= vecB) {
                    cnt++;
#if DEBUG
                    cout << "Match: " << orig << "~" << rot << endl;
#endif
                }
#if DEBUG
                cout << "Rotated: " << rot << endl;
#endif
            }
        } while (orig<vecB);

        cout << "Case #" << t+1 << ": " << cnt << endl;
    }

}

