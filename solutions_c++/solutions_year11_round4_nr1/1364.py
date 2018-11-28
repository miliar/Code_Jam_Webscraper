#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
#include <iomanip>
#include <cstdio>

using namespace std;

struct W {
    int beg, end, speed;
    bool operator < (const W& w) const {
        return beg < w.beg;
    }
};

void solution(int C, double s) {
    printf("Case #%d: %.9lf\n",C,s);
}

bool cmp(const W& w1, const W& w2) {
    return w1.speed < w2.speed;
}

double calc(double len, int speed) {
    return len/speed;
}

double time(int X, int S, int R, double t, vector<W> V) {
    sort(V.begin(),V.end());
    int prev = 0;
    int sz = V.size();
    for(int i = 0; i < sz; ++i) {
        if(V[i].beg == prev) {
            prev = V[i].end;
            continue;   
        }
        V.push_back((W){prev,V[i].beg,0});
        prev = V[i].end;
    }
    if(prev < X) V.push_back((W){prev,X,0});

    sort(V.begin(),V.end(),cmp);

    double tid = 0;
    int i = 0;
    while(t > 0 && i < (int)V.size()) {
        int len = V[i].end - V[i].beg;
        double maxspeed = (R+V[i].speed);
        if(len < t*maxspeed) {
            tid += calc(len,maxspeed);
            t -= double(len)/maxspeed;
        } else {
            tid += t;
            tid += calc(len-t*maxspeed,V[i].speed + S);
            t = 0;
        }
        ++i; 
    }
    for(int j = i; j < (int)V.size(); ++j) {
        tid += calc(V[j].end-V[j].beg,V[j].speed + S);
    }

    return tid;
}

int main() {
    int T;
    cin>>T;
    for(int C = 1; C <= T; ++C) {
        int X, S, R, t, N;
        cin>>X>>S>>R>>t>>N;
        vector<W> V(N);
        for(int i = 0; i < N; ++i) {
            cin>>V[i].beg>>V[i].end>>V[i].speed;
        }
        cin>>setprecision(9)>>fixed;
        solution(C,time(X,S,R,t,V));
    }
    return 0;
}
