#include<iostream>
#include<vector>
#include<utility>
//#include<functional>

using namespace std;

struct less_mag {
    bool operator () ( const pair<int,int>& a, const pair<int,int>& b ) {
        return a.first < b.first;
    }
};


int main() {
    int T; cin >> T;
    for (int c=1; c<=T; c++) {
        int N; cin >> N;
        vector< pair<int,int> > v;
        for (int i=0; i<N; i++) {
            int a,b; cin >> a >> b;
            pair<int,int> line = make_pair(a,b);
            v.push_back(line);
        }
        sort(v.begin(), v.end(), less_mag());
        
        int count = 0;
        for (int i=0; i<v.size()-1; i++) {
            for (int j=i+1; j<v.size(); j++) {
                if (v[j].second > v[i].second) ++count;
            }
        }
        cout << "Case #" <<c << ": " << (N*(N-1)/2 - count) << endl;
    }
    return 0;
}
