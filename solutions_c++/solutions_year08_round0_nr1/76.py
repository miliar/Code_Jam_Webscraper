#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>

#define ASSERT(condition) if(not (condition)) {int*i=0;*i=0;}

using namespace std;

int read_int() {
    string str;
    getline(cin, str);
    stringstream stream(str);
    int n;
    stream >> n;
    return n;
}

string read_line() {
    string str;
    getline(cin, str);
    return str;
}

int table[100][1024];
string engines[100];
int queries[1000];

int main(void) {
    int N;
    N = read_int();
    for(int CASE = 1; CASE <= N; ++ CASE) {
        int E = read_int();
        for(int i=0;i<E;++i) {
            engines[i] = read_line();
        }
        sort(engines, engines+E);
        int Q = read_int();
        for(int i=0;i<Q;++i) {
            queries[i] = lower_bound(engines, engines+E, read_line()) - engines;
        }
        for(int i=0;i<E;++i) {
            table[i][Q] = Q;
            for(int j=Q-1;j>=0;--j) {
                table[i][j]=table[i][j+1];
                if(queries[j] == i) {
                    table[i][j]=j;
                }
            }
        }
        int resp = 0;
        for(int i=0;i<Q;) {
            int e = 0;
            for(int j=1;j<E;++j) {
                if(table[j][i] > table[e][i]) {
                    e = j;
                }
            }
            if(i>0) {
                resp ++;
            }
            i = table[e][i];
        }
        cout << "Case #" << CASE << ": " << resp << endl;
    }
    return 0;
}
