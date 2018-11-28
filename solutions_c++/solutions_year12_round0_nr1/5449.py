#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
using namespace std;
int Case = 1, t;
string inv = "yhesocvxduiglbkrztnwjpfmaq";
string a, b;
int main(){
    freopen("a.out", "w", stdout);
    cin >> t;
    getline(cin, a);
    while(t--){
        getline(cin, a);
        printf("Case #%d: ", Case++);
        for(int i = 0; i < a.size(); i++){
            if(isalpha(a[i]))cout << inv[a[i] - 'a'];
            else cout << a[i];
        }
        cout << endl;
    }
    return 0;
}