#include <iostream>
#include <vector>
#include <queue>
#include <memory>
#include <stack>
#include <cmath>

using namespace std;

int find(double l, double r, int c, int count) {
    if(l*c < r) count++;
    else return count;
    double div = sqrt(l*r);
    return max(find(div, r, c, count), find(l, div, c, count));
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt","w", stdout);
    int T;
    cin >> T;
    
    for(int p=0; p<T; ++p) {
        int l, r, c;
        cin >> l >> r >> c;
        int res = find(l, r, c, 0);
        printf("Case #%d: %d\n", p+1, res);
    }
    
    return 0;
}
