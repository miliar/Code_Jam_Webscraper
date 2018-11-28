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


int do_switch(vector<string> & names, vector<string> queries, int index){
    int maxCount = 0;
    vector<int> which;
    if (index == queries.size())
        return 0;

    rep(i, names.size()){
        int c = 0;
        while(((index + c) < queries.size()) && names[i] != queries[index + c])c++;
        if (c > maxCount){
            which.clear();
            maxCount = c;
            which.push_back(i);
        } else if (c == maxCount){
            which.push_back(i);
        }
    }
    rep(i, which.size()){
        which[i] = do_switch(names, queries, index + maxCount);
    }
    return 1 + *max_element(which.begin(), which.end());
}

void solve()
{
    int N;
    cin >> N;
    for (int k = 0; k < N; ++ k){
        int S;
        int Q;
        vector<string> names;
        vector<string> queries;
        cin >> S;
        getchar();
        rep(i,S){
            string name;
            getline(cin, name);
            names.push_back(name);
        }
        cin >> Q;
        getchar();
        rep(i, Q){
            string query;
            getline(cin, query);
            queries.push_back(query);
        }
        
        if (Q == 0) {
            cout << "Case #" << (k+1) << ": " << 0<< '\n';
            continue;
        }

        int ret = do_switch(names, queries, 0);

        
        cout << "Case #" << (k+1) << ": " << (ret - 1)<< '\n';

    }

}

