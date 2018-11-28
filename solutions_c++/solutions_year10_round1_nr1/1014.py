#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int K, N;

void rotate(vector<string>& v) {
    vector<string> tmp = v;
    for (int y = 0; y < N; ++y) {
        for (int x = 0; x < N; ++x) {
            v[y][x] = tmp[N-x-1][y];
        }
    }
}
void fall(vector<string>& v) {
    for (int y = N-2; y >= 0; --y) {
        for (int x = 0; x < N; ++x) {
            if (v[y][x] != '.') {
                int find = -1;
                for (int k = y+1; k < N; ++k) {
                    if (v[k][x] == '.') find = k;
                }
                if (find != -1) {
                    swap(v[y][x], v[find][x]);
                }
            }
        }
    }
}

void print(const vector<string>& v) {
    for (int y = 0; y < N; ++y) {
        for (int x = 0; x < N; ++x) {
            cout << v[y][x];
        }
        cout << endl;
    }
    cout << endl;
}

bool range(int x, int y) {
    if (0 > x || 0 > y || N <= x || N <= y) return false;
    return true;
}

bool find(const vector<string>& v, char key) {
    for (int y = 0; y < N; ++y) {
        for (int x = 0; x <= N-K; ++x) {
            for (int i = 0; i < K; ++i) {
                if (v[y][x+i] != key) goto DIR_X;
            }
            return true;
        DIR_X:;
        }
    }
    
    for (int y = 0; y <= N-K; ++y) {
        for (int x = 0; x < N; ++x) {
            for (int i = 0; i < K; ++i) {
                if (v[y+i][x] != key) goto DIR_Y;
            }
            return true;        
        DIR_Y:;            
        }
    }
    
    for (int y = 0; y < N; ++y) {
        for (int x = 0; x < N; ++x) {
            for (int i = 0; i < K; ++i) {
                if (!range(x-i, y+i) || v[y+i][x-i] != key) goto DIR_L_DOWN;
            }
            return true;
        DIR_L_DOWN:;            
        }
    }
    
    for (int y = 0; y < N; ++y) {
        for (int x = 0; x < N; ++x) {
            for (int i = 0; i < K; ++i) {
                if (!range(x+i, y+i) || v[y+i][x+i] != key) goto DIR_R_DOWN;
            }
            return true;
        DIR_R_DOWN:;            
        }
    }    
    return false;
    
}

string solve() {
    cin >> N >> K;
    vector<string> v(N);
    for (int i = 0; i < N; ++i) { cin >> v[i]; }
    rotate(v);
    fall(v);
    bool red = find(v, 'R');
    bool blue = find(v, 'B');
    if (red && blue) return "Both";
    if (red) return "Red";
    if (blue) return "Blue";
    return "Neither";
}

int main() {
    int T;
    cin >> T;
    for (int times = 1; times <= T; ++times) {
        cout << "Case #" << times << ": " << solve() << '\r' << endl;
    }
    
    return 0;
}
