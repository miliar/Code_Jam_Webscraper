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
    ifstream cin("B-large.in");
    ofstream cout("out.txt");
    int T = 0;
    cin >> T;
    for (int t = 0; t < T; t++) {
        cout << "Case #" << t+1 << ": ";
        int N;
        cin >> N;
        int S;
        cin >> S;
        int p;
        cin >> p;
        vector<int> t(N);
        for (int i = 0; i < N; i++)
            cin >> t[i];
        sort(t.begin(), t.end());
        int res = 0;
        for (int i = 0; i < N; i++) {
            if ((t[i]+2)/3 >= p)
                res++;
            else if (t[i] > 0 && t[i]%3 == 0 && t[i]/3 + (S > 0) >= p) {
                res++;S--;
            }
            else if (t[i]%3 == 2 && t[i]/3 + 2*(S > 0) >= p){
                res++; S--;
            }
        }
        cout << res;
        cout << endl;
    }
}
