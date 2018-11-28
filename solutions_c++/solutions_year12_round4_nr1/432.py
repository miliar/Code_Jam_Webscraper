/* 
 * File:   main.cpp
 * Author: Ants
 *
 * Created on May 26, 2012, 4:51 PM
 */

#include <cstdlib>
#include <cstring>
#include <deque>
#include <queue>
#include <iostream>

using namespace std;

/*
 * 
 */

int bh[10010];
int d[10010];
int l[10010];

int main(int argc, char** argv) {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N;
        cin >> N;
        for (int n = 0; n < N; n++) {
            cin >> d[n] >> l[n];
        }
        int D;
        cin >> D;
        
        memset(bh, 0, N*sizeof(int));
        
        bh[0] = d[0];
        deque<pair<int, int> > queue; //vine index, height
        queue.push_back(make_pair(0, d[0]));
        
        
        bool answer = false;
        
        while (!queue.empty()) {
            int i = queue.front().first;
            int h = queue.front().second;
            queue.pop_front();
            
            if (h < bh[i]) continue;
            
            if (D-d[i] <= h) {
                answer = true;
                break;
            }
            
            for (int j = i+1; j < N; j++) {
                if (d[j]-d[i] > h) break;
                int h2 = min(l[j], d[j]-d[i]);
                if (h2 > bh[j]) {
                    bh[j] = h2;
                    queue.push_back(make_pair(j, h2));
                }
            }
        }
        
        cout << "Case #" << t << ": " << (answer ? "YES" : "NO") << endl;
    }
    
    
    return 0;
}

