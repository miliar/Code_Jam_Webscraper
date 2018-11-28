#include <iostream>
#include <string>
using namespace std;

typedef unsigned long long ull;
int countdiffnumber(string str){
    int ret = 0;
    sort(str.begin(), str.end());
    for(int i = 0; i < str.size(); ++ i)
        if (i == 0 || str[i] != str[i - 1]) ++ ret;
    return ret;
}

int mymap[255];

ull calc(string& str){
    int base = countdiffnumber(str);
    if (base == 1) base = 2;
    memset(mymap, -1, sizeof(mymap));
    int nextnumber = 1;
    ull ret = 0;
    for(int i = 0; i < str.size(); ++ i) {
        if (mymap[str[i]] == -1) {
            mymap[str[i]] = nextnumber;
            if (nextnumber == 1)
                nextnumber = 0;
            else if (nextnumber == 0)
                nextnumber = 2;
            else ++ nextnumber;
        }
        ret = ret * base + mymap[str[i]];
    }
    return ret;
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w+", stdout);
    int T;
    cin >> T;
    string str;
    for (int i = 1; i <= T; ++ i){
        cin >> str;
        cout << "Case #" << i << ": " << calc(str) << endl;
    }
    return 0;
}
