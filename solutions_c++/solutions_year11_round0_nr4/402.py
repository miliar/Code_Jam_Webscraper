// google code jam d

#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

const int MAXN = 1100;

int key[MAXN], list[MAXN], n;

void qs(int l, int r)
{
    int i = l, j = r, x = key[(l + r) >> 1];
    do
    {
        while (i < r && key[i] < x) i++;
        while (l < j && key[j] > x) j--;
        if (i <= j)
        {
            int t = key[i];
            key[i] = key[j];
            key[j] = t;
            i++, j--;
        }
    } while (i <= j);
    if (i < r)
        qs(i, r);
    if (l < j)
        qs(l, j);
}

int main()
{
    char filename[100];
    cin >> filename;
    ifstream fin(filename, ios::in);
    ofstream fout("dout.txt", ios::out);
    int testcase;
    fin >> testcase;
    for (int test = 1; test <= testcase; test++)
    {
        fin >> n;
        for (int i = 1; i <= n; i++)
        {
            fin >> key[i];
            list[i] = key[i];
        }
        qs(1, n);
        double ans = 0;
        for (int i = 1; i <= n; i++)
            if (key[i] != list[i])
                ans += 1;
        fout << "Case #" << test << ": " << setiosflags(ios::fixed) << setprecision(6) << ans << endl;
    }
    fout.close();
    fin.close();
    return 0;
}
