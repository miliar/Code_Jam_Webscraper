#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <math.h>
#include <map>

using namespace std;

ifstream fin("C-large.in");
ofstream fout("C-large.out");

int N, a[1005];
int main() {
    int T;
    fin>>T;
    for(int k = 1;k<=T;++k) {
        fin>>N;
        for(int i = 0;i<N;++i) {
            fin>>a[i];
        }
        sort(a,a+N);
        int s = 0, res = 0;
        for(int i = 1;i<N;++i) {
            res += a[i];
            s^=a[i];
        }
        fout<<"Case #"<<k<<": ";
        if(a[0] != s) fout<<"NO"<<endl;
        else fout<<res<<endl;
    }
    return 0;
}
