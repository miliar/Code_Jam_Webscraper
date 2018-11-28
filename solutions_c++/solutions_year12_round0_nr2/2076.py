#include <iostream>
#include <fstream>

using namespace std;

int abs (int a) {
    return a < 0 ? -a : a;
}

int solve (int n, int s, int p, int t[101]) {
    int answ = 0;
    for (int i = 0; i < n; i ++) {
        int m = t[i] / 3;
        bool brk = false;

        for (int x = max(0, m-2); !brk && x <= m+2; x++) {
            for (int y = max(0, m-2); !brk && y <= m+2; y++) {
                for (int z = max(0, m-2); !brk && z <= m+2; z++) {
                    if (x+y+z == t[i]) {
                        if (abs(z-x) < 2 && abs(z-y) < 2 && abs(y-x) < 2 && (x >= p || y >= p || z >= p)) {
                            answ++;
                            brk = true;
                            //cout << x << " " << y << " " << z << endl;
                        }
                    }
                }
            }
        }


        for (int x = max(0, m-2); !brk && x <= m+2; x++) {
            for (int y = max(0, m-2); !brk && y <= m+2; y++) {
                for (int z = max(0, m-2); !brk && z <= m+2; z++) {
                    if (x+y+z == t[i]) {
                        if (s && abs(z-x) < 3 && abs(z-y) < 3 && abs(y-x) < 3 && (x >= p || y >= p || z >= p)) {
                            answ++;
                            s--;
                            brk = true;
                           // cout << x << " " << y << " " << z << endl;
                        }
                    }
                }
            }
        }
    }
    return answ;
}

int main () {
    ifstream fd ("input.txt");
    ofstream fr ("output.txt");

    int n;
    fd >> n;
    for (int i = 1; i <= n; i++) {
        int n, s, p, t[101] = {};
        fd >> n >> s >> p;
        for (int j = 0; j < n; j++) {
            fd >> t[j];
        }
        fr << "Case #" << i << ": " << solve(n, s, p, t) << endl;
    }

    fd.close();
    fr.close();
    return 0;
}
