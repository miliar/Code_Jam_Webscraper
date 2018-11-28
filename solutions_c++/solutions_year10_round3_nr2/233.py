#include <iostream>
//#include <algorithm>
//#include <deque>
//#include <iomanip>
//#include <map>
//#include <queue>
//#include <set>
//#include <stack>
//#include <utility>
//#include <vector>

using namespace std;

bool solve(int cn){
    long long sol = 0;
    long long min, max, C;
    if(!(cin >> min >> max >> C)) return false;

    long long tmp = min;
    long long count = 0;
    while(tmp < max){
        tmp *= C;
        count++;
    }

    while(count > 1){
        if(count % 2) count = count / 2 + 1;
        else count = count / 2;
        sol++;
    }

    //cout << "Case #" << cn << ": " << (sol ? "yes" : "no") << endl;
    cout << "Case #" << cn << ": " << sol << endl;

    return true;
}

int main(){
    int cases = LONG_MAX;
    scanf("%d", &cases);
    for(int cn = 1; cn <= cases && solve(cn); cn++);
    return 0;
}
