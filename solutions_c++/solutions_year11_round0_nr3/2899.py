#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char** argv)
{
    fstream in, out;
    in.open("c.in", ios_base::in);
    out.open("c.out", ios_base::out);
    int T;
    in >> T;
    for (int t = 0; t < T; t++) {
        int N;
        in >> N;
        int min = 1000000 + 1;
        int cur = 0, sum = 0;
        for (int i = 0; i < N; i++) {
            int c;
            in >> c;
            cur ^= c;
            sum += c;
            if (c < min) min = c;
        }
        if (cur) {
            out << "Case #" << t + 1 << ": NO" << endl;
        } else {
            out << "Case #" << t + 1 << ": " << sum - min << endl;
        }
    }
    in.close();
    out.close();
	return 0;
}

