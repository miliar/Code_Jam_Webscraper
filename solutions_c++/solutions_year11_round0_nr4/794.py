#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("task4.in");
    FILE* fout = fopen("task4.out", "w");
    int total;
    fin >> total;
    for (int brojac = 0; brojac < total; ++brojac)
    {
        int N;
        fin >> N;
        vector<int> niz(N);
        vector<int> original(N);
        for (int i = 0; i < N; ++i)
        {
            fin >> niz[i];
            original[i] = niz[i];
        }
        std::sort(niz.begin(), niz.end());
        int ans = 0;
        for (int i = 0; i < N; ++i)
        {
            if (niz[i] != original[i])
                ++ans;
        }
        double out = ans;
        fprintf(fout, "Case #%d: %.6f\n", brojac + 1, out);
    }
    return 0;
}
