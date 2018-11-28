#include <iostream>
//#include <string>
//#include <sstream>
//#include <algorithm>
//#include <vector>
//#include <ctype.h>
//#include <assert.h>
//#include <math.h>
//#include <set>
//#include <map>

using namespace std;

typedef unsigned long long num;
typedef unsigned short arg;
typedef unsigned idx;


void solve(const num t)
{
    arg N;
    num K;
    const char *s;

    cin >> N >> K;
    s = ((K+1) % (1 << N) == 0)?"ON":"OFF";
    cout << "Case #" << t << ": " << s << endl;
}

int main(void)
{
    num T;

    cin >> T;
    for(num t=1; t<=T; ++t) solve(t);

    return 0;
}
