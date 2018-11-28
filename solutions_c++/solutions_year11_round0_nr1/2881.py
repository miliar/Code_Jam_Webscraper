#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char** argv)
{
    fstream in, out;
    in.open("a.in", ios_base::in);
    out.open("a.out", ios_base::out);
    int T;
    in >> T;
    for (int t = 0; t < T; t++) {
        int N;
        in >> N;
        int ret = 0;
        int bt = 0, ot = 0;
        int bp = 1, op = 1;
        for (int n = 0; n < N; n++) {
            char c;
            int pos;
            in >> c;
            in >> pos;
            if (c == 'O') {
                int delta = abs(pos - op);
                op = pos;
                delta -= ot;
                if (delta < 0) delta = 0;
                delta++;
                bt += delta;
                ot = 0;
                ret += delta;
            } else {
                int delta = abs(pos - bp);
                bp = pos;
                delta -= bt;
                if (delta < 0) delta = 0;
                delta++;
                ot += delta;
                bt = 0;
                ret += delta;
            }
        }
        out << "Case #" << t + 1 << ": " << ret << endl;
    }
    in.close();
    out.close();
	return 0;
}

