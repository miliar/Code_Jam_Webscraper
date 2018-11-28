#include <iostream>
#include <fstream>
#include <list>
using namespace std;

#define MAX 1001
#define LL long long
LL i,j,n,m,r,k,tmp,t;
ifstream fin("in.txt");
ofstream fout("out.txt");

int main() {

    fin >> t;
    for (int test=1;test<=t;test++) {

    list<LL> gr;
    fin >> r >> k >> n;
    for (i=0;i<n;i++) {
        fin >> tmp;
        gr.push_back(tmp);
    }

    LL sum(0);
    for (int turn=0;turn<r;turn++) {
            LL curr(0),idx(0);
            while (idx < n) {
                if (*(gr.begin()) + curr <= k) {
                    curr += *(gr.begin());
                    gr.insert(gr.end(),*(gr.begin()));
                    gr.erase(gr.begin());
                    }
                else break;
                idx++;
                }
            sum += curr;
        }
    fout << "Case #" << test << ": " << sum << endl;
    }
}
