#include <cstdlib>
#include <vector>
#include <queue>
#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#include <map>
#include <cmath>
#include <cstdlib>
#include <list>
#include <set>

using namespace std;

int main(int argc, char** argv) {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);




    int T;
    cin >> T;
    int test = 0;
    while (test++ < T) {
        int R, K, N;
        cin >> R >> K >> N;
        vector < pair<int, long long > > L;
        int g;
        for (int i = 0; i < N; i++) {
            cin >> g;
            L.push_back(make_pair(i, g));

        }
        vector<pair<int, long long> > A;

        long long answer = 0;
        int cicle = -1;

        for (int i = 0; i < R; i++) {
            int cnt = L.size();
            long long mtv = 0;
            pair<int, long long> t = L[0];

            for (int j = 0; j < A.size(); j++) {
                if (A[j].first == t.first) {
                    cicle = j;
                    break;
                }
            }
            if (cicle != -1) {
                break;
            }

            while (cnt > 0 && mtv + L[0].second <= K && cnt > 0) {
                pair<int, long long> temp = L[0];
                mtv += temp.second;
                cnt--;
                L.erase(L.begin());
                L.push_back(temp);

            }
            A.push_back(make_pair(t.first, mtv));
        }
        if (cicle == -1) {
            cicle = 100000;
        }
        answer = 0;

        for (int i = 0; i < A.size() && i < cicle && R > 0; i++) {
            answer += A[i].second;
            R--;
        }
        long long length = A.size() - cicle;
        long long sum = 0;
        for (int i = cicle; i < A.size(); i++) sum += A[i].second;
        answer += (R / length) * sum;
        R %= length;
        while (R > 0) {
            answer += A[cicle++].second;
            R--;
        }

        cout << "Case #" << test << ": " << answer << endl;

    }


    return (EXIT_SUCCESS);
}

