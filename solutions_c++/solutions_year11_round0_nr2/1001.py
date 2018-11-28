#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <utility>

using namespace std;

int main()
{
    int i;
    cin >> i;
    for (int n = 0; n < i; n++) {
         int ps;
         map< pair<char, char>, char> par;
         set< pair<char, char> > opps;
         cin >> ps;
         for (int j = 0; j < ps; j++) {
            string abc;
            cin >> abc;
            par[make_pair(abc[0], abc[1])] = abc[2];
            par[make_pair(abc[1], abc[0])] = abc[2];
         }
         cin >> ps;
         for (int j = 0; j < ps; j++) {
            string abc;
            cin >> abc;
            opps.insert(make_pair(abc[0], abc[1]));
            opps.insert(make_pair(abc[1], abc[0]));            
         }
         cin >> ps;
         vector<char> dam;
         for (int j = 0; j < ps; j++) {
            char zz;
            cin >> zz;
            if (dam.empty()) {
                dam.push_back(zz);
            } else {
                pair<char, char> tmp = make_pair(dam.back(), zz);
                if(par.find(tmp) != par.end()) {
                    dam.pop_back();
                    dam.push_back(par[tmp]);
                } else {
                    bool erased = false;
                    for (int a = dam.size() - 1; a >= 0; a --) {

                        if (opps.find(make_pair(dam[a], zz)) != opps.end()) {
                            dam.clear();
                            erased = true;
                        }
                    }
                    if (!erased) {
                        dam.push_back(zz);
                    }
                }
            }
         }
         cout << "Case #" << (n + 1) << ": [";
         if (!dam.empty()) {
            cout << dam[0];
         }
         for (int j = 1; j < dam.size(); j++) {
            cout << ", " << dam[j];
         }
         cout << "]" << endl;
    }
    return 0;
}
