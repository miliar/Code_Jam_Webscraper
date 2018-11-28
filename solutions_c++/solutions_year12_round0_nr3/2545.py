#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <set>

using namespace std;

unsigned long int toInt(string s){
    return atoi(s.c_str());
}

string toString(unsigned long int a){
    stringstream ss;
    ss << a;
    return ss.str();
}

string recycle(string s){
    unsigned long int len = s.length();
    return s.at(len-1) + s.substr(0, len -1);
}

int main(int argc, char const* argv[])
{
    unsigned long int T, ans, iA, iB;
    string A, B;
    cin >> T;
    for(int i=0; i<T; i++){
        ans = 0;
        cin >> A >> B;
        iA = toInt(A);
        iB = toInt(B);
        set<string> ansset;
        for(unsigned long int j = iA; j < iB; j++){
            ansset.clear();
            string jstr = toString(j);
            int len = jstr.length();
            string tmp = jstr;
            for(int k = 0; k < len-1; k++){
                tmp = recycle(tmp);
                if(toInt(tmp) > j && toInt(tmp) <= iB){
                        //cout << "j:" << j << ", tmp:" << tmp << endl;
                        ansset.insert(tmp);
                }
            }
            ans += ansset.size();
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    return 0;
}
