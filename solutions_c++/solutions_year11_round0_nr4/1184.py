#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int tc = 0; tc < T; tc++) {
        cout << "Case #" << tc+1 << ": ";
        int N;
        cin >> N;
        double w = 0.0;
        for(int i = 0; i < N; i++) {
            int t;
            cin >> t;
            if(t != (i+1)) w++;
        }
        cout.precision(6);
        cout << fixed << w << endl;
    }
    return 0;
}
