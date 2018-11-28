#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <fstream>
#include <sstream>
#include <utility>

using namespace std;

int main(){
    int nc; cin >> nc;
    for (int Q = 1; Q <= nc; Q++){
        string s; cin >> s;
        string s2 = s;
        next_permutation(s2.begin(),s2.end());
        if (s2 > s){
           cout << "Case #" << Q << ": " << s2 << endl;
        }
        else {
             sort(s.begin(),s.end());
             string s3 = "";
             char dig;
             for (int i=0;i<s.size();i++){
                 if (s[i] == '0') s3 = s3 + '0';
                 else {
                      s3 = s3 + s.substr(i+1,s.size()-i-1);
                      dig = s[i];
                      break;
                 }
             }
             //cout << "s3 = " << s3 << endl;
             s3 = s3 + '0';
             sort(s3.begin(),s3.end());
             cout << "Case #" << Q << ": " << dig << s3 << endl;
        }
    }
    return 0;
}
