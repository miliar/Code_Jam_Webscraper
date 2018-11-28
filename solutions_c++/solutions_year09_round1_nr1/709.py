#include <iostream>
#include <sstream>
#include <vector>
#include <string>
using namespace std;

int T;
vector<int> B;
bool h[11][10000000], visited[11][10000000];
int K;

bool happy(int n);
bool happybase(int n,int b);

int main() {
    string line;
    int b;

    cin >> T;
    getline(cin,line);
    for (int t = 1; t <= T; t++) {
        B.clear();
        getline(cin,line);
        istringstream sin(line);
        while (sin >> b)
            B.push_back(b);

        for (int i = 0; i < B.size(); i++) {
            visited[B[i]][1] = true;
            h[B[i]][1] = true;
            for (int j = 2; j < 100000; j++)
                visited[B[i]][j] = false;
        }
        K = 2;
        while (true) {
            if (happy(K)) {
                cout << "Case #" << t << ": " << K << endl;
                break;
            }
            K++;
        }
    }
    
    return 0;
}

bool happy(int n) {
    for (int i = 0; i < B.size(); i++)
        if (!happybase(n,B[i]))
            return false;
    return true;
}

bool happybase(int n,int b) {
    if (visited[b][n])
        return h[b][n];

    visited[b][n] = true;
    h[b][n] = false;
    int cur = n, next = 0;
    while (cur > 0) {
        next += (cur%b) * (cur%b);
        cur /= b;
    }
    return h[b][n] = happybase(next,b);
}
