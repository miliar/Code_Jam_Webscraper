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

int A[1000], B[1000];

int main() {
    ifstream in("A-large.in");
    //ifstream in("A-small-attempt0.in");
    //ifstream in("A-small-attempt1.in");
    ofstream out("A-small.out");
    int cases = 0;
    in >> cases;
    for (int i=0; i<cases; i++) {
        int num;
        in >> num;
        for (int i=0; i<num; i++) {
            in >> A[i] >> B[i];
        }
        __int64 intersect = 0;
        for (int i=0; i<num-1; i++)
        {
            for (int j=i+1; j<num; j++) {
                if ((A[i] < A[j] && B[i] > B[j]) || (A[i] > A[j] && B[i] < B[j]))
                   intersect++;
            }
        }
        out << "Case #" << (i+1) << ": " << intersect << "\n";
    }
    out.close();
    in.close();
    return 0;
}
