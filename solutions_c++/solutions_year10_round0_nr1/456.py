#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
int cicle(int n) {
    return 1 << n;
}
int solution(int n, int k) {
    k %= cicle(n);
    if (k == cicle(n) - 1) return 1;
    return 0;
}
void scase(int casen) {
    int n, k;
    cin >> n >> k;
    cout << "Case #" << casen << ": " << (solution(n, k) ? "ON" : "OFF") << endl;
}
int main(int argc, char **argv) {
    int cases;
    cin >> cases;
    for (int c = 1; c <= cases; c++) scase(c);
    return 0;
}

