/* 
 * File:   main.cpp
 * Author: Ants
 *
 * Created on May 26, 2012, 4:51 PM
 */

#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int abs(int x) {
    return (x < 0) ? (-x) : x;
}
/*
 * 
 */
int main(int argc, char** argv) {
    srand(time(0));
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, W, L;
        cin >> N >> W >> L;
        
        bool flip = L > W;
        if (flip) {
            int temp = W;
            W = L;
            L = temp;
        }
        
        vector<pair<int, int> > people(N); //radius, index
        vector<int> X(N);
        vector<int> Y(N);
        for (int n = 0; n < N; n++) {
            int r;
            cin >> r;
            people[n].first = r;
            people[n].second = n;
        }
        sort(people.rbegin(), people.rend());
        
        
        bool right = true;
        X[people[0].second] = 0;
        Y[people[0].second] = 0;
        for (int i = 1; i < N; i++) {
            int r = people[i].first;
            int nx = X[people[i-1].second];
            nx += (right ? 1 : -1)*(r+people[i-1].first);
            if (nx > W || nx < 0) {
                right = !right;
                nx = (right ? 0 : W);
            }
            int ny = 0;
            for (int j = 0; j < i; j++) {
                int x2 = X[people[j].second];
                int y2 = Y[people[j].second];
                int r2 = people[j].first;
                if (abs(nx - x2) < r+r2 && ny < y2+r+r2) {
                    ny = y2+r+r2;
                }
            }
            if (ny > L) {
                right = !right;
                ny = L;
                nx = (right ? 0 : W);
                for (int j = 0; j < i; j++) {
                    int x2 = X[people[j].second];
                    int y2 = Y[people[j].second];
                    int r2 = people[j].first;
                    if (abs(ny-y2) < r+r2 && abs(nx-x2) < r+r2) {
                        nx = x2 + (right ? 1 : -1)*(r+r2);
                    }
                }
                int ny = 0;
                for (int j = 0; j < i; j++) {
                    int x2 = X[people[j].second];
                    int y2 = Y[people[j].second];
                    int r2 = people[j].first;
                    if (abs(nx - x2) < r + r2 && ny < y2 + r + r2) {
                        ny = y2 + r + r2;
                    }
                }

            }
            X[people[i].second] = nx;
            Y[people[i].second] = ny;
        }
        
        cout << "Case #" << t << ": ";
        for (int i = 0; i < N; i++) {
            if (!flip) {
                cout << X[i] << " " << Y[i] << " ";
            } else {
                cout << Y[i] << " " << X[i] << " ";
            }
        }
        cout << endl;
        
    }
    
    return 0;
}
