#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <deque>
#include <cmath>
#include <algorithm>
using namespace std;

long long res = 0;
char buf[100];
int len;

bool isUgly(long long t) {
    if( t == 0 || t%2 == 0 || t%3 == 0 || t%5 == 0 || t%7 == 0 ) return true;
    else return false;
}

void solve(long long n,int p,bool ex,long long pre) {
    if( p == len ) {
        if( isUgly(n+pre) ) res++;
    }
    else {
        if( ex ) solve(n,p+1,ex,pre*(long long)10+(buf[p]-'0'));
        else solve(n,p+1,ex,pre*10-(buf[p]-'0'));
        solve(n+pre,p+1,true,buf[p]-'0');
        solve(n+pre,p+1,false,(buf[p]-'0')*(-1));
    }
}



int main() {
    int N;
    cin >> N;
    int num = 0;
    while( num < N ) {
        res = 0;
        cin >> buf;
        len = strlen(buf);
        solve(0,1,true,buf[0]-'0');
        printf("Case #%d: ",num+1);
        cout << res << endl;
        num++;
    }
    system("pause");
    return 0;
}
