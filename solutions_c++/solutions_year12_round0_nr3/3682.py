#include <iostream>
#include <cstring>
#include <cmath>
#include <set>
using namespace std;

int digits(int n) {
    int k = 0;
    do {
        k++;
        n/=10;
    } while(n);
    return k;
}

int main() {
    int t;
    cin >> t;
    int m[8];
    m[0] = 1;
    for (int i = 1; i < 8; i++) {
        m[i] = m[i-1] * 10;
    }
    
    int kase = 0;
    while(t--) {
        set < pair<int,int> > s;
        int a, b;
        cin >> a >> b;
        int count = 0, d = digits(a);
        for (int i = a; i <= b; i++) {
            for (int j = 1; j < d; j++) {
                int new_num = ((i%m[j])*m[d-j])+(i/m[j]);
                if(a <= i && i < new_num && new_num <= b) { 
                    if (s.find(make_pair(min(i,new_num), max(i,new_num))) != s.end())
                        continue;
                    s.insert(make_pair(min(i,new_num), max(i,new_num)));
                    count++;
                }
            }
        }
        cout << "Case #" << ++kase << ": " << count << endl;
    }
}
