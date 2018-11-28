#include <fstream>

using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int tests;
    fin >> tests;
    for (int t = 1; t <= tests; t++)
    {
        int n, k;
        fin >> n >> k;
        fout << "Case #" << t << ": " << (((k % (1 << n)) == (1 << n) - 1) ? "ON" : "OFF") << endl;
    }
    fout.close();
    return 0;
}