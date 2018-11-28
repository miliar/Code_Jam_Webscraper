#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

char who[100];
int where[100];

int a[100];
int b[100];
int am, bm;
int ai, bi;
int ap, bp;

int acloser(int aw, int bw) {
    return abs(ap - aw) - abs(bp - bw);
}

int main() {
    ifstream in("A-large.in");
    ofstream out("a.out");
    
    int Z, N;
    int t;
    
    in >> Z;
    for(int z = 0; z < Z; z++) {
        in >> N;
        am = 0;
        bm = 0;
        t = 0;
        for(int i = 0; i < N; i++) {
            in >> who[i];
            in.get();
            in >> where[i];    
            if (who[i] == 'O') {
                a[am++] = where[i];
            }
            else {
                b[bm++] = where[i];
            }
        }
        for(int i = am; i < 100; i++) a[i] = a[am-1];
        for(int i = bm; i < 100; i++) b[i] = b[bm-1];
        ap = 1;
        bp = 1;
        ai = 0;
        bi = 0;
        t = 0;
        for(int i = 0; i < N; i++) {

            if (acloser(a[ai], b[bi]) < 0) {
                if (who[i] == 'O') {
                    t += abs(ap - a[ai]) + 1;
                    if (bp > b[bi]) bp -= (abs(ap - a[ai]) + 1);
                    else if (bp < b[bi]) bp += (abs(ap - a[ai]) + 1);
                    ap = a[ai++];
                    //cout << "O pressed button " << a[ai-1] << ", B moved" << endl;
                }
                else {
                    t += abs(bp - b[bi]) + 1;
                    ap = a[ai];
                    bp = b[bi++];
                    //cout << "B pressed button " << b[bi-1] << ", O waited" << endl;
                }
            }
            else if (acloser(a[ai], b[bi]) > 0){
                if (who[i] == 'B') {
                    t += abs(bp - b[bi]) + 1;
                    if (ap > a[ai]) ap -= (abs(bp - b[bi]) + 1);
                    else if (ap < a[ai]) ap += (abs(bp - b[bi]) + 1);
                    bp = b[bi++];
                    //cout << "B pressed button " << b[bi-1] << ", O moved" << endl;
                }
                else {
                    t += abs(ap - a[ai]) + 1;
                    ap = a[ai++];
                    bp = b[bi];
                    //cout << "O pressed button " << a[ai-1] << ", B waited" << endl;
                }
            }
            else {
                t += abs(bp - b[bi]) + 1;
                ap = a[ai];
                bp = b[bi];
                if (who[i] == 'O') ai++;
                else bi++;
                //cout << "both waiting" << endl;
            }
            //cout << t << ": " << ap << " " << bp << endl;
        }
        out << "Case #" << z + 1 << ": " << t << endl;
        //cout << "Case #" << z + 1 << ": " << t << endl;
    }

    return 0;
}
