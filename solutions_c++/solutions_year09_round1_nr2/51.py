#include<iostream>
#include<queue>
#include<vector>
#include<tuple>
#include<utility>
#include<functional>

using namespace std;

typedef tuple<long long,long long,long long,long long> state;

int main() {
    long long T;
    cin >> T;
    for(long long t=1; t<=T; t++) {
        long long n, m;
        long long si[20][20], wi[20][20], ti[20][20];
        cin >> n >> m;
        for(long long i=0; i<n; i++) {
            for(long long j=0; j<m; j++) {
                cin >> si[i][j] >> wi[i][j] >> ti[i][j];
                long long interval = si[i][j] + wi[i][j];
                ti[i][j] -= interval * 100000000;
                ti[i][j] ++;
            }
        }

        long long dp[20][20][4] = {{{}}};

        priority_queue<state, vector<state>, greater<state>> q;
        q.push(make_tuple<long long,long long,long long,long long>(1, n-1, 0, 2));

        while(dp[0][m-1][1] == 0) {
            state s = q.top();
            q.pop();

            long long t = get<0>(s), i = get<1>(s), j = get<2>(s), k = get<3>(s);
            if(i < 0 or i >= n or j < 0 or j >= m) continue;

            long long& ref = dp[i][j][k];

            if(ref != 0) continue;
            ref = get<0>(s);


            long long nh = t, nv = t;
            long long interval = si[i][j] + wi[i][j];
            long long t0 = ti[i][j] + (t - ti[i][j])/interval * interval;
            if(t - t0 < si[i][j]) nh = t0 + si[i][j];
            else nv = t0 + interval;

            if(k == 0) {
                q.push(make_tuple<long long,long long,long long,long long>(t+2, i, j-1, 1));
                q.push(make_tuple<long long,long long,long long,long long>(t+2, i-1, j, 2));
                q.push(make_tuple<long long,long long,long long,long long>(nh+1, i, j, 1));
                q.push(make_tuple<long long,long long,long long,long long>(nv+1, i, j, 2));
            }
            else if(k == 1) {
                q.push(make_tuple<long long,long long,long long,long long>(t+2, i, j+1, 0));
                q.push(make_tuple<long long,long long,long long,long long>(t+2, i-1, j, 3));
                q.push(make_tuple<long long,long long,long long,long long>(nh+1, i, j, 0));
                q.push(make_tuple<long long,long long,long long,long long>(nv+1, i, j, 3));
            }
            else if(k == 2) {
                q.push(make_tuple<long long,long long,long long,long long>(t+2, i+1, j, 0));
                q.push(make_tuple<long long,long long,long long,long long>(t+2, i, j-1, 3));
                q.push(make_tuple<long long,long long,long long,long long>(nv+1, i, j, 0));
                q.push(make_tuple<long long,long long,long long,long long>(nh+1, i, j, 3));
            }
            else {
                q.push(make_tuple<long long,long long,long long,long long>(t+2, i+1, j, 1));
                q.push(make_tuple<long long,long long,long long,long long>(t+2, i, j+1, 2));
                q.push(make_tuple<long long,long long,long long,long long>(nv+1, i, j, 1));
                q.push(make_tuple<long long,long long,long long,long long>(nh+1, i, j, 2));
            }
        }

        cout << "Case #" << t << ": " << dp[0][m-1][1] - 1<< endl;
    }
}

