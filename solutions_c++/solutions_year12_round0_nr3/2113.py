#include <iostream>
#include <fstream>
#include <math.h>
#include <map>

using namespace std;

int t, A, B, len;

void getLength () {
    len = 0;
    int tmp = B;
    while (tmp != 0) {
        len++;
        tmp /= 10;
    }
}

int shift (int x, int k) {
    for (int i = 0; i < k; i++) {
        int last = x % 10;
        x /= 10;
        x = last * pow(10, len-1) +  x;
    }
    return x;
}

int solve (int x) {
    int answ = 0;
    map<int, int> M;
    for (int i = 1; i < len; i++) {
        int shifted = shift(x, i);
        if (shifted >= A && shifted <= B && shifted != x && M.count(shifted) == 0) {
            M.insert(pair <int, int> (shifted, shifted));
            answ++;
        }
    }
    return answ;
}

int main () {
    ifstream fd ("input.txt");
    ofstream fr ("output.txt");

    fd >> t;
    for (int i = 1; i <= t; i++) {
        fd >> A >> B;
        getLength();
        int answ = 0;
        for (int j = A; j <= B; j++) {
            answ += solve(j);
        }
        fr << "Case #" << i << ": " << answ/2 << endl;
    }

    fd.close();
    fr.close();
    return 0;
}
