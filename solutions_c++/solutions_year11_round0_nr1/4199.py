// 2011/05/08 Naoyuki Hirayama

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int abs(int n) {
    if( n < 0 ) { return -n; }
    return n;
}

void nextline(istream& is) {
    string s;
    getline(is, s);
    cout << "!!!" << s << endl;
}

int main() {
    int lines;
    cin >> lines;
    for (int i = 0 ; i < lines ; ++i) {
        int cols;
        cin >> cols;
        int op = 1;
        int bp = 1;
        int cycle = 0;
        int cache = 0;
        int prev = -1; // 0= O 1= B
        for (int j = 0 ; j < cols ; ++j) {
            string mark;
            int place;
            cin >> mark >> place;
            if( mark == "O") {
                int m = abs(place - op);
                if( prev != 0 ) {
                    m -= cache;
                    if( m < 0 ) m = 0;
                    prev = 0;
                    cache = 0;
                }
                m++;
                cycle += m;
                op = place;
                cache += m;
            } else {
                int m = abs(place - bp);
                if( prev != 1 ) {
                    m -= cache;
                    if( m < 0 ) m = 0;
                    prev = 1;
                    cache = 0;
                }
                m++;
                cycle += m;
                bp = place;
                cache += m;
            }
        }
        cout << "Case #" << (i+1) << ": " << cycle << endl;
    }
}
