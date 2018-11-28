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

bool check(LL x, LL y, LL r, vector<pair<LL,LL> >& results, vector<pair<LL, size_t> >& arms){
    for(size_t i = 0; i < results.size(); i++){
        LL dx = results[i].first - x;
        LL dy = results[i].second - y;
        LL r2 = r + arms[i].first;
        if(dx*dx + dy*dy < r2*r2) return false;
    }
    return true;
}

vector<pair<LL,LL> > solve(LL width, LL length, vector<pair<LL, size_t> >& arms){
    sort(arms.begin(), arms.end(), greater<pair<LL, size_t> >());
    while(true){
        vector<pair<LL, LL> > result;
        for(size_t i = 0; i < arms.size(); i++){
            LL x = 0, y = 0;
            size_t c;
            const size_t challenge_max = 100;
            for(c = 0; c < challenge_max; c++){
                x = rand() % (width+1);
                y = rand() % (length+1);
                if(check(x, y, arms[i].first, result, arms)) break;
            }
            if(c >= challenge_max) break;
            result.push_back(pair<LL,LL>(x, y));
        }
        if(result.size() == arms.size()){
            vector<pair<LL, LL> > result2(result.size());
            for(size_t i = 0; i < arms.size(); i++){
                result2[arms[i].second] = result[i];
            }
            return result2;
        }
    }
}

int main(){
    size_t T = 0;
    cin >> T;
    for(size_t t = 1; t <= T; t++){
        int N, W, L;
        cin >> N >> W >> L;
        vector<pair<LL, size_t> > arms;
        for(int n = 0; n < N; n++){
            LL a;
            cin >> a;
            arms.push_back(pair<LL, size_t>(a, n));
        }
        vector<pair<LL,LL> > result = solve(W, L, arms);
        cout << "Case #" << t << ":";
        for(size_t i = 0; i < result.size(); i++){
            cout << " " << result[i].first << " " << result[i].second;
        }
        cout << endl;
    }
    return 0;
}

