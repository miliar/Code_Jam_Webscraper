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
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>

using namespace std;

bool func(int i, int j) { return (i > j); }

int main() {
        int N, P, K, L, num;
        vector <int> arr;
        vector<int>::iterator it;
        char temp;
        int ret;
        int tt;

        cin >> N;
        scanf("%c", &temp);
        for(int i=0 ; i < N ; i++) {
                cin >> P >> K >> L;
                scanf("%c", &temp);
                ret = 0;
                arr.clear();
                for(int j=0 ; j < L ; j++) {
                        cin >> num;
                        arr.push_back(num);
                }
                sort(arr.begin(), arr.end(), func);

                for(int j=0 ; j < arr.size() ; j++) {
                        ret += (arr[j] * (j/K+1));
                }
                cout << "Case #" << i+1 << ": " << ret << endl;
                ret = 0;
        }
}
