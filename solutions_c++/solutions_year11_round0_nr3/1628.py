#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
#include <stack>
#include <deque>
#include <map>
#include <numeric>
#include <iterator>

#define FOR(i,s,n) for((i)=(s);(i)<(int)(n);(i)++)
#define FORD(i,s,n) for((i)=(s);(i)>=(int)(n);(i)--)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define INF (1<<29)

#define isnbit(d, n) ((d>>n)&1)

using namespace std;




int run(int ncase){
    int i, j, k;
    int N;
    vector<int> list, list2;
    string ans;
    int sum = 0;
    int sum2 = 0;

    cin >> N;
    list.resize(N);
    list2.reserve(N);
    FOR(i, 0, N){
        cin >> list[i];
        sum ^= list[i];
        sum2 += list[i];
    }

    if(sum != 0)
        sum2 = -1;
    else{
        sort(list.begin(), list.end());
        sum2 -= list[0];
    }



    cout << "Case #" << ncase << ": ";
    if(sum2 >= 0)
        cout << sum2 << endl;
    else
        cout << "NO" << endl;
    return 0;
}

int main() {
    int i, test_set;
    cin >> test_set;
    //cin.ignore();
    FOR(i, 0, test_set) run(i+1);
    return 0;
}
