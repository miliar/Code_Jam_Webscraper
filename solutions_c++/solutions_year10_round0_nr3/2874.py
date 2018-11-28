#include<iostream>
#include<conio.h>
#include<fstream>
#include<sstream>
#include<string>
#include<queue>
using namespace std;
#define __int64 long long

template <class Item>
string toStr(Item x) { stringstream m; m << x; return m.str(); }

int main() {
    ifstream in("C-small-attempt1.in");
    ofstream out("C-small.out");
    int cases = 0;
    in >> cases;
    for (int i=0; i<cases; i++) {
        __int64 R, k, N, total = 0, cost = 0;
        in >> R >> k >> N;
        queue<__int64> q;
        for (int j=0; j<N; j++) {
            __int64 temp; in >> temp; total += temp;
            q.push(temp);
        }   
        while (R > 0) {
              __int64 current = 0;
              if (total > k) {
                  while ( (current+q.front()) <= k ) {
                        current += q.front();
                        q.push(q.front());
                        q.pop();
                  }
              } else {
                  current = total;
              }
              cost += current;
              R--;
        }
        out << "Case #" << (i+1) << ": " << cost << "\n";
    }
    out.close();
    in.close();
    return 0;
}
