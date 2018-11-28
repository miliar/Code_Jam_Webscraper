#include <iostream>
#include <vector>

using namespace std;

double myabs(double x) {
    if (x<0) return -x;
    return x;
}

int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        vector<int> vpos;
        vector<int> vcnt;

        int C,D;
        cin >> C>>D;
        for(int i=0; i<C;i++) {
            int P,V;
            cin >> P>>V;
            vpos.push_back(P);
            vcnt.push_back(V);
        }

        double hi = 1e20;
        double lo = 0;
        for(int iter=0; iter<300; iter++) {
            double tm = (hi +lo)/2;

            bool works = true;
            double prev = -1e200;
            for(int i=0; i<vpos.size(); i++) {
                if (i > 0 && vpos[i-1] >= vpos[i]) cout << "BAD INPUT"<<endl;
                double pos = vpos[i];
                for(int j=0; j<vcnt[i]; j++) {
                    double npos = pos - tm;
                    if (npos < prev + D) {
                        npos = prev + D;
                        if (works && myabs(npos - pos) > tm) {
                            works = false;
                        }
                    }
                    prev = npos;
                }
            }

            if (works) hi = tm;
            else lo = tm;
        }

        cout << "Case #" <<(c+1) << ": ";
        printf("%0.10f", (lo+hi)/2);
        cout<<endl;
    }
}
