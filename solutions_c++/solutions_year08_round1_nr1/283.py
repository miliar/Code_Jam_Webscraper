#include <iostream>
#include <fstream>
using namespace std;
long long x[1000], y[1000];
int n;
int main(){
    int T;
    ifstream cin("A-large.in");
    ofstream cout("out.txt");
    cin >> T;
    for(int t = 1; t <= T; ++ t){
        cin >> n;
        for(int i = 0; i < n; ++ i)
            cin >> x[i];
        for(int j = 0; j < n; ++ j)
            cin >> y[j];
        sort(x, x + n);
        sort(y, y + n, greater<long long>());
        long long ret = 0;
        for(int i = 0; i < n; ++ i)
            ret += x[i] * y[i];
        cout << "Case #" << t << ": " << ret << endl;
    }
    return 0;
}
