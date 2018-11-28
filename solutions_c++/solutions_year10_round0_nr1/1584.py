#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int T;
    long long N,K;

    cin >> T;
    for(int C=1;C<=T;C++) {
        cin >> N >> K;

        long long a = (1LL<<N) - 1;

        printf("Case #%d: %s\n", C, (((a&K)==a)?"ON":"OFF"));
    }

    return 0;
}
