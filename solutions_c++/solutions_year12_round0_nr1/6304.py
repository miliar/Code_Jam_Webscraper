#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
    freopen("1.in","r",stdin);
    freopen("a.out","w",stdout);
    char s[300], str[200];
    memset(s,0,sizeof(s));
    s['e']='o';
    s['j']='u';
    s['p']='r';
    s[' ']=' ';
    s['m']='l';
    s['y']='a';
    s['s']='n';
    s['l']='g';
    s['j']='u';
    s['y']='a';
    s['l']='g';
    s['c']='e';
    s[' ']=' ';
    s['k']='i';
    s['d']='s';
    s[' ']=' ';
    s['k']='i';
    s['x']='m';
    s['v']='p';
    s['e']='o';
    s['d']='s';
    s['d']='s';
    s['k']='i';
    s['n']='b';
    s['m']='l';
    s['c']='e';
    s[' ']=' ';
    s['r']='t';
    s['e']='o';
    s[' ']=' ';
    s['j']='u';
    s['s']='n';
    s['i']='d';
    s['c']='e';
    s['p']='r';
    s['d']='s';
    s['r']='t';
    s['y']='a';
    s['s']='n';
    s['i']='d';
    s['r']='t';
    s['b']='h';
    s['c']='e';
    s['p']='r';
    s['c']='e';
    s[' ']=' ';
    s['y']='a';
    s['p']='r';
    s['c']='e';
    s[' ']=' ';
    s['r']='t';
    s['t']='w';
    s['c']='e';
    s['s']='n';
    s['r']='t';
    s['a']='y';
    s[' ']=' ';
    s['d']='s';
    s['k']='i';
    s['h']='x';
    s[' ']=' ';
    s['w']='f';
    s['y']='a';
    s['f']='c';
    s['r']='t';
    s['e']='o';
    s['p']='r';
    s['k']='i';
    s['y']='a';
    s['m']='l';
    s[' ']=' ';
    s['v']='p';
    s['e']='o';
    s['d']='s';
    s['d']='s';
    s['k']='i';
    s['n']='b';
    s['k']='i';
    s['m']='l';
    s['k']='i';
    s['r']='t';
    s['k']='i';
    s['c']='e';
    s['d']='s';
    s['d']='s';
    s['e']='o';
    s[' ']=' ';
    s['k']='i';
    s['r']='t';
    s[' ']=' ';
    s['k']='i';
    s['d']='s';
    s[' ']=' ';
    s['e']='o';
    s['o']='k';
    s['y']='a';
    s['a']='y';
    s[' ']=' ';
    s['k']='i';
    s['w']='f';
    s[' ']=' ';
    s['a']='y';
    s['e']='o';
    s['j']='u';
    s[' ']=' ';
    s['t']='w';
    s['y']='a';
    s['s']='n';
    s['r']='t';
    s[' ']=' ';
    s['r']='t';
    s['e']='o';
    s[' ']=' ';
    s['u']='j';
    s['j']='u';
    s['d']='s';
    s['r']='t';
    s[' ']=' ';
    s['l']='g';
    s['k']='i';
    s['g']='v';
    s['c']='e';
    s[' ']=' ';
    s['j']='u';
    s['v']='p';
    s['q']='z';
    s['z']='q';
    int T;
    cin>> T;
    getchar();
    for(int ca = 1;ca<=T;ca++){
        gets(str);
        printf("Case #%d: ",ca);
        for(int i =0; str[i];i++){
            cout<<s[str[i]];
        }
        cout<<endl;
    }
}
