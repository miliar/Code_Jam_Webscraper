#include <algorithm>
#include <vector>
#include <sstream>
#include <set>
#include <iostream>
#include <map>
#include <iomanip>
#include <fstream>
#include <locale>
#include <cmath>
using namespace std;

int main() {
    ifstream cin("C-large.in");
    ofstream cout("out.txt");
    int T = 0;
    cin >> T;
    for (int t = 0; t < T; t++) {
        cout << "Case #" << t+1 << ": ";
        int A,B;
        cin >> A >> B;
        long long res = 0;
        set<int> tmp;
        for (int i = A; i < B; i++) {
            tmp.clear();
            ostringstream str;
            str << i;
            string s = str.str();
            //cout << "Current: " << i << endl;
            for (int j = 1; j < s.size(); j++) {
                //cout << "ind: " << j << endl;
                if (s[j] == '0')
                    continue;
                istringstream str2(s.substr(j) + s.substr(0, j));
                int temp;
                str2 >> temp;
                //cout << temp << endl;
                if (temp > i && temp <= B) {
                    //cout << temp << endl;
                    tmp.insert(temp);
                }
            }
            res += tmp.size();
        }
        cout << res;
        cout << endl;
    }
}
