#include <fstream>
using namespace std;

const int Maxn = 1000;

int t, n;
pair<int, int> P[Maxn];

int main()
{
    ifstream fin("a.in");
    ofstream fout("a.out");
    int i, j, k, kiek;
    fin >> t;
    for (i = 1; i <= t; i++) {
        kiek = 0;
        fin >> n;
        for (j = 0; j < n; j++)
          fin >> P[j].first >> P[j].second;
        sort(P, P+n);
        for (j = 0; j < n; j++)
          for (k = j+1; k < n; k++)
            if (P[j].second > P[k].second) kiek++;
        fout << "Case #" << i << ": " << kiek << endl;
    }
    fin.close(); fout.close();
    return 0;
}
