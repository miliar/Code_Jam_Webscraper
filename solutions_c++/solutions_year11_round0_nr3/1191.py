#include <iostream>

using namespace std;

int N;
unsigned long C[1000];

bool is_possible()
{
    unsigned long sum = 0;
    for(int i = 0; i < N; i++) {
        sum ^= C[i];
    }
    return sum == 0;
}

unsigned long max_value()
{
    unsigned long sum = 0;
    unsigned long smallest = 100000000;
    for(int i = 0; i < N; i++) {
        sum += C[i];
        if(C[i] < smallest) smallest = C[i];
    }
    return sum - smallest;
}

int main()
{
    int T;
    cin >> T;
    for(int tc = 0; tc < T; tc++) {
        cout << "Case #" << tc+1 << ": ";
        cin >> N;
        for(int i = 0; i < N; i++) {
            cin >> C[i];
        }
        if(!is_possible()) {
            cout << "NO" << endl;
        } else {
            cout << max_value() << endl;
        }
    }
    return 0;
}
