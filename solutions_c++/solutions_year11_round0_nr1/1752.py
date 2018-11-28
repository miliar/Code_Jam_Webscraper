#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    int T, N, P;
    fin >> T;
    char c;
    for (int t = 1; t <=T; ++t) {
        int oseq[100], bseq[100];
        char turn[100];
        fin >> N;
        int oindex = 0, bindex = 0, tindex = 0;
        for (int n = 0; n < N; ++n) {
            fin >> c;
            turn[tindex++] = c;
            fin >> P;
            if (c == 'O')
                oseq[oindex++] = P;
            else
                bseq[bindex++] = P;
        }
        int osize = oindex, bsize = bindex, tsize = tindex;
        oindex = 0;
        bindex = 0;
        tindex = 0;
        int opos = 1, bpos = 1;
        int count = 0;
        int odir, bdir;
        while(tindex < tsize) {
            ++count;
            bool pushed = false;
            odir = oseq[oindex] - opos;
            bdir = bseq[bindex] - bpos;
            if (odir == 0) {
                if (turn[tindex] == 'O') {
                    pushed = true;
                    ++oindex;
                }
            }
            else
                opos += (odir < 0) ? -1 : 1;
            if (bdir == 0) {
                if (turn[tindex] == 'B') {
                    ++bindex;
                    pushed = true;
                }
            }
            else
                bpos += (bdir < 0) ? -1 : 1;

            if (pushed)
                ++tindex;
        }
        fout << "Case #" << t << ": " << count << endl;
    }
}

