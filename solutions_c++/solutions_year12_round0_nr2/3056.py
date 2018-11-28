#include <iostream>


using namespace std;

int main()
{
    int T;

    cin >> T;

    for (int k=1; k<=T; k++) {
        int N, S, p;
        cin >> N >> S >> p;
        int ans = 0;
        for (int i=0; i<N; i++) {
            int x;
            cin >> x;
            if (x>=3*p-2) ans++;
            else if (x>=3*p-4 && S>0 && p>1) {ans++; S--;}
        }
        cout << "Case #" << k <<": ";
        cout << ans << endl;
    }
    return 0;
}

