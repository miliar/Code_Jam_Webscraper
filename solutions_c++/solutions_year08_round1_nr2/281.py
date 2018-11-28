#include <vector>
#include <iostream>
#include <map>
#include <functional>
#include <algorithm>
#include <list>
#include <string>
#include <sstream>
#include <bitset>
#include <cmath>
#include <iomanip>
#include <queue>
#include <set>
#include <stack>
#include <cassert>
using namespace std;

#define rep(i, size) \
    for (int i = 0; i < size; ++ i)

#define LL long long


void solve()
{
    int N;
    cin >> N;
    for (int k = 0; k < N; ++ k){
        int n;
        int m;
        cin >> n;
        cin >> m;
        vector<vector<int> > flavors;
        rep(i, m){
            int t;
            cin >> t;
            vector<int> cu;
            rep(j, t){
                int index;
                int malt;
                cin >> index;
                cin >> malt;
                cu.push_back(malt ? -index : index);
            }
            flavors.push_back(cu);
        }
        vector<int> ret(n, 0);
        bool impossible = false;
        
        while(true){
            bool found = false;
            rep(i, flavors.size()){
                if (flavors[i].size() == 1 && flavors[i][0] < 0){
                    ret[-flavors[i][0] - 1] = 1;
                    found = true;
                    int index = -flavors[i][0];
                    flavors.erase(flavors.begin() + i);
                    rep(ii, flavors.size()){
                        rep(j, flavors[ii].size()){
                            if (index == flavors[ii][j]){
                                flavors[ii].erase(flavors[ii].begin() + j);
                            }
                        }
                    }
                }
            }
            if (!found)
                break;
        }

        rep(i, flavors.size()){
            if (flavors[i].size() == 0)
                impossible = true;
        }


        if (impossible){
            cout << "Case #" << (k+1) << ": " << "IMPOSSIBLE" << '\n';
        } else {
            cout << "Case #" << (k+1) << ": ";
            rep(i, n){
                cout << ret[i] << ' ';
            }
            cout << '\n';
        }

    }

}