#include <fstream>
using namespace std;

int t, n, k;

int main()
{
    ifstream fin("task.in");
    ofstream fout("task.out");
    int i;
    fin >> t;
    for (i = 1; i <= t; i++) {
        fin >> n >> k;
        n = (1 << n) - 1;
        fout << "Case #" << i << ": ";
        if ((k & n) == n) fout << "ON\n"; else fout << "OFF\n";
    }
    fin.close();
    fout.close();
    return 0;
}
