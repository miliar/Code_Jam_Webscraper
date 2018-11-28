#include <iostream>
#include <map>
#include <vector>
#include <string>

using namespace std;
/*
  #include <string>
    istream& std::getline( istream& is, string& s, char delimiter = '\n' );
*/
string thecode = "welcome to code jam";
vector<int> countp;
vector<int> counti;

int main () {
    int T;
    int count = 1;
    string s;
    cin >> T;
    getline(cin, s);
    while (T--) {
        getline(cin, s);
        countp = vector<int>(thecode.size(), 0);
        counti = vector<int>(thecode.size(), 0);
        for(int i = 0; i < s.size(); i++) {
            counti = countp;
            for (int j = 0; j < thecode.size(); j++) {
                if (s[i] == thecode[j]) {
                    if (j != 0) {
                        countp[j] = (counti[j-1] + counti[j])%10000;
                    } else
                        countp[j]++;
                }
            }
//            for(int i = 0; i < countp.size(); i++)
//                cout << " " << countp[i];
//        cout << endl;
        }
        int sol = countp[countp.size()-1];
        int m,c,d,u;
        m = ((sol-sol%1000)/1000)%10;
        c = ((sol-sol%100)/100)%10;
        d = ((sol-sol%10)/10)%10;
        u = ((sol)%10);
        cout << "Case #" << count++ << ": "<< m<<c<<d<<u<< endl;
    }
    return 0;
}



