#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

char f[111][3];
char o[111][2];
int solve( int x ) {
    int c,d,n;
    int i,j,k,l;
    string str,list = "";
    string null = "";
    cin >> c;
    for (i = 1; i <= c; i++) {
        cin >> str;
        f[i][0] = str[0]; f[i][1] = str[1]; f[i][2] = str[2];
        f[c+i][0] = f[i][1];
        f[c+i][1] = f[i][0];
        f[c+i][2] = f[i][2];
    }    

    cin >> d; 
    for (i = 1; i <= d; i++) {
        cin >> str;
        o[i][0] = str[0];
        o[i][1] = str[1];        
        o[d+i][0] = o[i][1];
        o[d+i][1] = o[i][0];
    }
    cin >> n >> str;
    
    for (i = 0; i < n; i++) {
        list = list + str[i];
        l = list.length();
        for (j = 1; j <= 2*c; j++) 
             if ((list[l-1] == f[j][0]) && (list[l-2] == f[j][1])) {
                list[l-2] = f[j][2];
                list.erase(l-1);
                continue;
            }
        for (j = 1; j <= 2*d; j++) 
            for (k = 0; k < l-1; k++)
            if ((list[l-1] == o[j][0]) && (list[k] == o[j][1])) {
                list.erase(0,l+1);
            }
    }    
    cout<<"Case #"<<x<<": [";
    if (list.length() == 0) { cout<<"]\n"; return 0 ;}
    for (i = 0; i < list.length()-1; i++) cout<<list[i]<<", ";
    cout<<list[list.length()-1]<<"]\n";
}

int main() {
   freopen("B-large.in", "rt", stdin);
   freopen("b.out", "wt", stdout);
    int t,i,j;
    cin>>t;
    for (i = 1; i <= t; i++) {
        solve(i);
    }
};
