#include <iostream>
#include <algorithm>
//#include <deque>
//#include <iomanip>
//#include <map>
//#include <queue>
//#include <set>
//#include <stack>
#include <utility>
//#include <vector>

using namespace std;

bool solve(int cn){
    int sol = 0;
    int n = 0;
    cin >> n;

    int a1[n];
    int a2[n];

    for(int i=0; i<n; i++){
        cin >> a1[i] >> a2[i];
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(i == j) continue;
            if(a1[i] < a1[j] && a2[i] > a2[j]) sol++;
            if(a1[i] > a1[j] && a2[i] < a2[j]) sol++;
        }
    }

    sol = sol / 2;

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
