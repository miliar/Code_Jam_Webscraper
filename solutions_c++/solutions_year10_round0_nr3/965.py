#include <iostream>
#include <queue>

using namespace std;

int main() {
    int TESTCASE;
    int R, k, N;
    cin >> TESTCASE;
    for (int CASE = 1 ; CASE <= TESTCASE ; CASE++) {
        long long euro = 0;
        queue<int> q;
        cin >> R >> k >> N;
        for(int i = 0 ; i < N ; i++) {
            int g;
            cin >> g;
            q.push(g);
        }
        for(int i = 0 ; i < R ; i++) {
            //cout << "ride " << i << " times" << endl;
            int currN = 0;
            int p = 0;

            while (++currN <= N and p + q.front() <= k) {
                //cout << "in > " << q.front() << endl;
                q.push(q.front());
                p += q.front();
                q.pop();
            }

            euro += p;
        }

        cout << "Case #" << CASE << ": " << euro << endl;
    }
}
