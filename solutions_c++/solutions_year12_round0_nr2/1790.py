#include <fstream>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)

int main(int argc, char const *argv[]) {
    ifstream in ("B-large.in");
    ofstream out ("B-large.out");

    int t;
    in >> t;
    REP(ca,t) {
        int n, s, p, gp, so = 0;
        in >> n >> s >> p;
        REP(i,n) {
            in >> gp;
            if ((gp+2)/3 >= p) so++;
            else if ((gp+4)/3 >= p && gp && s) {
                so++;
                s--;
            }
        }
        out << "Case #" << ca+1 << ": " << so << endl;
    }

    return 0;
}
