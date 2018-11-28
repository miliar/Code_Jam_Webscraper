#include <string>
#include <vector>
#include <fstream>

using namespace std;
typedef long long int LL;

int main(int argc, char** argv)
{
    fstream in, out;
    in.open("c.in", ios_base::in);
    out.open("c.out", ios_base::out);
    int T;
    in >> T;
    for (int t = 0; t < T; t++) {
        int N, L, H;
        in >> N >> L >> H;
        vector<LL> fs;
        for (int n = 0; n < N; n++) {
            int f;
            in >> f;
            fs.push_back(f);
        }
        int ok = 0;
        for (int f = L; f <= H; f++) {
            bool curOk = true;
            for (int i = 0; i < N; i++) {
                if (fs[i] % f && f % fs[i]) {
                    curOk = false;
                    break;
                }
            }
            if (curOk) {
                ok = f;
                break;
            }
        }
        out << "Case #" << t + 1 << ": ";
        if (ok) {
            out << ok << endl;
        } else {
            out << "NO" << endl;
        }
    }
    in.close();
    out.close();
	return 0;
}

