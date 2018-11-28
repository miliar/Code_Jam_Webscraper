#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <fstream>
#include <map>

using namespace std;



bool search(vector<int> v){
    map<int, vector<int> > m;

    for(int i = 1; i <= (1 << v.size()); ++i){
        vector<int> vput;
        int sum = 0;
        for(int j = 0; j < v.size(); ++j)
            if(i & (1 << j)){
                vput.push_back(v[j]);
                sum += v[j];
            }
        if(m.find(sum) == m.end()){
            m[sum] = vput;
        }
        else{
            cout << endl;
            for(int j = 0; j < vput.size(); ++j)
                cout << vput[j] << " ";
            cout << endl;
            vector<int> h = m[sum];
            for(int j = 0; j < h.size(); ++j)
                cout << h[j] << " ";
            cout << endl;
            return true;
        }
    }
    return false;
}

int main(){
    int T;
    freopen("C-small-attempt0.in", "rt", stdin);
    freopen("C-small-attempt0.out", "wt", stdout);
    scanf("%d", &T);

    for(int i = 1; i <= T; ++i){
        cout << "Case #" << i << ": ";
        int N, x;
        scanf("%d", &N);
        vector<int> v;
        for(int j = 0; j < N; ++j){
            scanf("%d", &x);
            v.push_back(x);
        }
        sort(v.begin(), v.end());
        if(search(v) == false){
            cout << "Impossible" << endl;
        }
    }
}


