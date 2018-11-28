#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<iomanip>
#include<queue>

using namespace std;

int main(){
    ofstream fout ("out.out");
    ifstream fin ("in.in");
    int t;
    fin >> t;
    for (int caso = 1; caso <= t; caso++){
        long long L, t, N, C;
        fin >> L >> t >> N >> C;
        t/=2;
        vector<int> stars (C);
        for (int i = 0; i < C; i++){
            fin >> stars[i];
        }
        priority_queue<int> pq;
        long long res = stars[0]*2;
        long long ultRes = 0;
        long long dist = stars[0];
        if (dist >= t) pq.push(dist-t);
        for (int i = 1; i < N; i++){
            ultRes = dist;
            dist+=stars[i%C];
            res+=stars[i%C]*2;
            int h = max (ultRes, t);
            if (dist >= h) pq.push(dist-h);
        }
        for (int i = 0; i < L and !pq.empty(); i++){
            res-=pq.top();
            pq.pop();
        }
        fout << "Case #" << caso << ": " << res << endl;
    }
}
