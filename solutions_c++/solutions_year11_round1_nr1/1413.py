#include <fstream>

using namespace std;

int gcd(int a, int b) {
    if (a == 0)
        return b;
    return gcd(b % a, a);
}

int main(int argc, char** argv) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    int T;
    fin >> T;

    for (int t = 1; t <= T; ++t) {
        int N, PD, PG;
        bool possible = true;
        fin >> N >> PD >> PG;
        fout << "Case #" << t << ": ";
        if ( (100/gcd(PD,100) > N) || (PG==0&&PD!=0) || (PG == 100 && PD != 100) )
            fout << "Broken";
        else
            fout << "Possible";
        fout << endl;
    }
}

