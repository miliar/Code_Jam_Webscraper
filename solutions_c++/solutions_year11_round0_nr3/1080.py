#include <iostream>
#include <vector>

using namespace std;


int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        int N;
        cin >> N;
        vector<int> v;
        v.resize(N);
        for(int i=0; i<N; i++) cin >> v[i];

        sort(v.begin(), v.end());
        int x = 0;
        int sum=0;
        for(int i=0; i<N; i++) {
            x = x ^ v[i];
            if (i > 0) sum += v[i];
        }

        cout << "Case #" <<(c+1) << ": ";
        if (x == 0) cout << sum;
        else cout << "NO";
        cout <<endl;
    }
}
