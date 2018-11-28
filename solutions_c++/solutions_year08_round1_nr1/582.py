#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;

int n;
long long v1[100010];
long long v2[100010];

int main()
{
    ifstream fin("a.in");
    ofstream fout("a.out");
    int casos;
    fin >> casos;
    for(int C = 1; C<= casos; C++)
    {
        fout << "Case #" << C << ": ";
        fin >> n;
        for(int i = 0; i<n; i++)
            fin >> v1[i];
        for(int i = 0; i<n; i++)
            fin >> v2[i];
        sort(v1, v1+n);
        sort(v2, v2+n);
        reverse(v2, v2+n);
        long long res = 0;
        for(int i = 0; i < n; i++)
            res += v1[i]*v2[i];
        fout << res << endl;
    }
    return 0;
}
