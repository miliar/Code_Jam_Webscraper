#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int main()
{
    int cases;
    cin >> cases;

    for (int cs = 0; cs < cases; ++cs) {
        int K, n;
        vector<int> indices;
        cin >> K >> n;
        for (int i = 0; i < n; ++i) {
            int j;
            cin >> j;
            indices.push_back(j);
        }

        deque<int> q;
        for (int i = 0; i < K; ++i)
            q.push_back(i);

        vector<int> deck(K, -1);
        int done = 0;
        while (!q.empty()) {
            for (int i = 0; i < done; ++i) {
                int v = q.front();
                q.pop_front();
                q.push_back(v);
            }

            int v = q.front();
            q.pop_front();
            deck[v] = ++done;
        }

        cout << "Case #" << cs + 1 << ':';
        for (int i = 0; i < (int)indices.size(); ++i) {
            cout << ' ' << deck[indices[i] - 1];
        }
        cout << '\n';
    }

    return 0;
}
