// google code jam C

#include <iostream>
#include <fstream>
using namespace std;

const int MAXN = 1100;

int key[MAXN], n;

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
    ofstream fout("cout.txt", ios::out);
    int testcase, sum;
    fin >> testcase;
    for (int test = 1; test <= testcase; test++)
    {
        fin >> n;
        for (int i = 1; i <= n; i++)
        {
            fin >> key[i];
            sum = i == 1 ? key[i] : (sum ^ key[i]);
        }
        fout << "Case #" << test << ": ";
        if (sum != 0)
            fout << "NO" << endl;
        else
        {
            int ans = 0;
            qs(1, n);
            for (int i = 2; i <= n; i++)
                ans += key[i];
            fout << ans << endl;
        }
    }
    fout.close();
    fin.close();
    return 0;
}

