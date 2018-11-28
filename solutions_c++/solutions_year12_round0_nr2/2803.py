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

using namespace std;

int main() {
    string line;
    getline(cin, line);
    const int T = atoi(line.c_str());
    for (int t=0; t<T; ++t) {
        getline(cin, line);
        istringstream iss(line);
        int N, S, p;
        iss >> N >> S >> p;
        int ok = p*3-2;
        int almost = p*3-4;
        int cnt = 0;
        for (int n=0; n<N; ++n) {
            int v;
            iss >> v;
            if (v>=ok) {
                cnt += 1;
            }
            else if (almost>0 && v>=almost) {
                if (S>0) {
                    cnt+=1;
                    S-=1;
                }
            }
        }
        cout << "Case #" << t+1 << ": " << cnt << endl;
    }
}

