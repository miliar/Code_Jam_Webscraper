#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <utility>
#include <functional>
#include <cctype>
#include <iomanip>
#include <cmath>
#include <sstream>
#include <map>

using namespace std;

int apply(int number, int base) {
    int ret=0;
    while(number) {
        ret+=(number%base)*(number%base);
        number/=base;
    }
    return ret;
}

map<int,int> got[11];

int happy(int number, int base) {
    if(number==1) return 1;
    if(got[base].count(number)) return got[base][number];
    got[base][number]=0;
    int next=apply(number, base);
    return got[base][number]=happy(next, base);
}

void solve(int cnum) {
    string s;
    getline(cin,s);
    vector<int> bases;
    stringstream ss;
    int temp;
    ss<<s;
    while(ss>>temp) {
        bases.push_back(temp);
    }
    int ret=-1;
    for(int i=2;;i++) {
        bool ok=1;
        for(int j=0;j<bases.size();j++) if(!happy(i, bases[j])) {
            ok=0;
            break;
        }
        if(ok) { ret=i; break; }
    }
    cout<<"Case #"<<cnum<<": "<<ret<<endl;
}

int main() {
    int cases;
    cin>>cases;
    string s;
    getline(cin,s);
    for(int cnum=1;cnum<=cases;cnum++) {
        solve(cnum);
    }
}

