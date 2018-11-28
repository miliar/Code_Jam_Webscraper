#include <cstdio>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

string intToString(int n){
    string ret = "";
    while(n){
        ret = (char)('0' + (n % 10)) + ret;
        n /= 10;
    }
    return ret;
}

int stringToInt(string s){
    int ret = 0;
    for(int i = 0; i < (int)s.length(); ++i){
        ret = ret * 10 + (int)(s[i] - '0');
    }
    return ret;
}

string makeMovedString(string s, int change){
    string ret;
    ret += s.substr(s.size() - change, change);
    ret += s.substr(0, s.size() - change);
    return ret;
}

int main(void)
{
    int T;
    cin >> T;

    for(int t = 0; t < T; ++t){
        int A, B;
        cin >> A >> B;

        long long ret = 0;
        for(int n = A; n < B; ++n){
            if (n < 10){
                continue;
            }
            string nStr = intToString(n);

            map<int, int> found;
            for(int change = 1; change <= (int)nStr.length()-1; ++change){
                string mStr = makeMovedString(nStr, change);
                if (mStr[0] == '0'){
                    continue;
                }
                
                int m = stringToInt(mStr);
                if (found.find(m) == found.end()){
                    if (n < m && m <= B){
                        ++ret;
                        found[m] = 1;
                    }
                }
            }
        }

        cout << "Case #" << (t+1) << ": " << ret << endl;
    }

    return 0;
}
