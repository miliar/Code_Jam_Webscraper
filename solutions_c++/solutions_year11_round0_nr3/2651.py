#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;

void TC(int T)
{
    int N = 0;
    long minv = 10000000;
    long sum = 0;
    long xsum = 0;
    cin >> N;
    for(int i = 0; i < N; ++i) {
        long val = 0;
        cin >> val;
        xsum ^= val;
        sum += val;
        if(val < minv) {
            minv = val;
        }
    }
    cout << "Case #" << (T + 1) << ": ";
    if(xsum != 0) {
        cout << "NO";
    } else {
        cout << (sum - minv);
    }
    cout << endl;
}

int main(int argc, char **argv)
{
    int N = 0;
    cin >> N;
    for(int i = 0; i < N; ++i) {
        TC(i);
    }
    return 0;
}
