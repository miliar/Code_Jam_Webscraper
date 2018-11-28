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
long m[27] = {};
using namespace std;

int main () {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    string s = "ynficwlbkuomxsevzpdrjgthaq";
    long i,j;
    for (i = 0; i < s.size(); i ++) 
        m[s[i]-'a'] = i;
        
    long T;
    cin >> T;
    char st[111];
    fgets(st,111,stdin);
    
    for (i = 0; i < T; i ++) {
        fgets(st,111,stdin);
        for (j = 0; j < strlen(st);j ++)
            if ('a' <= st[j] && st[j] <= 'z') 
            st[j] = 'a'+m[st[j]-'a'];
        cout << "Case #" << i+1<< ": "<<st;
    }
}
