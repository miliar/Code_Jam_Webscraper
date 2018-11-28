#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <map>

using namespace std;
typedef long long LL;

bool solve(vector<pair<LL, LL> >& vines, LL distance){
    LL reachable = vines[0].first * 2;
    vector<LL> length(vines.size());
    length[0] = vines[0].first;
    for(size_t i = 1; i < vines.size(); i++){
        if(vines[i].first > reachable) break;
        for(size_t j = 0; j < i; j++){
            if(vines[j].first + length[j] >= vines[i].first){
                LL l = min(vines[i].second, vines[i].first - vines[j].first);
                length[i] = max(length[i], l);
                reachable = max(reachable, vines[i].first + length[i]);
            }
        }
    }
    return reachable >= distance;
}

int main(){
    size_t T = 0;
    cin >> T;
    for(size_t t = 1; t <= T; t++){
        int N;
        vector<pair<LL, LL> > vines;
        LL D;
        cin >> N;
        for(int n = 0; n < N; n++){
            LL d, i;
            cin >> d >> i;
            vines.push_back(pair<LL,LL>(d, i));
        }
        cin >> D;
        if(solve(vines, D)){
            cout << "Case #" << t << ": YES" << endl;
        }else{
            cout << "Case #" << t << ": NO" << endl;
        }
    }
    return 0;
}

