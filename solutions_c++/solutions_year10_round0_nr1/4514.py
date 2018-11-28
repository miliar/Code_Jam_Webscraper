#include<iostream>
#include<conio.h>
#include<fstream>
#include<sstream>
#include<string>
#include<queue>
#include<math.h>
using namespace std;
#define __int64 long long

template <class Item>
string toStr(Item x) { stringstream m; m << x; return m.str(); }

int main() {
    ifstream in("A-small.in");
    ofstream out("A-small.out");
    int cases = 0;
    in >> cases;
    for (int i=0; i<cases; i++) {
        __int64 N, K, m = 0; double ans = 0;
        in >> N >> K;
        bool on = false;
        while (ans < K) {
              ans = (m * pow(2,N)) - 1;
              on = (K == ans);
              m++;
              if (on) break;
        }
        string st = (on) ? "ON" : "OFF";
        out << "Case #" << (i+1) << ": " << st << "\n";
    }
    out.close();
    in.close();
    return 0;
}
