
#include <iostream>
#include <vector>

using namespace std;

int N;
int P[100];
char R[100];

int solve() {
    cin >> N;
    vector <int> orange, blue;
    for(int i = 0; i < N; i++) {
        cin >> R[i] >> P[i];
        if(R[i] == 'O')
            orange.push_back(P[i]);
        else
            blue.push_back(P[i]);
    }

    int total = 0;
    int opos = 1, oi = 0;
    int bpos = 1, bi = 0;
    for(int i = 0; i < N; i++) {
        int odir = 0;
        if(oi < orange.size() && opos < orange[oi])
            odir = 1;
        if(oi < orange.size() && opos > orange[oi])
            odir = -1;

        int bdir = 0;
        if(bi < blue.size() && bpos < blue[bi])
            bdir = 1;
        if(bi < blue.size() && bpos > blue[bi])
            bdir = -1;

        if(R[i] == 'O') {
            while(opos != P[i]) {
                opos += odir;
                if(bi < blue.size() && bpos != blue[bi])
                    bpos += bdir;
                total++;
            }
            if(bi < blue.size() && bpos != blue[bi])
                bpos += bdir;
            total++;

            oi++;
        }
        else {
            while(bpos != P[i]) {
                bpos += bdir;
                if(oi < orange.size() && opos != orange[oi])
                    opos += odir;
                total++;
            }
            if(oi < orange.size() && opos != orange[oi])
                opos += odir;
            total++;

            bi++;
        }
        //printf("at: %d, %d, total: %d\n", opos, bpos, total);
    }

    return total;
}

int main() {
    int T;
    cin >> T;
    for(int i = 0; i < T; i++)
        cout << "Case #" << i+1 << ": " << solve() << endl;

    return 0;
}
