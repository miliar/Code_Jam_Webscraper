#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("task3.in");
    ofstream fout("task3.out");
    int total;
    fin >> total;
    for (int brojac = 0; brojac < total; ++brojac)
    {
        int n;
        fin >> n;
        int suma = 0;
        int real_sum = 0;
        int mini = 100000000;
        for (int i = 0; i < n; ++i)
        {
            int broj;
            fin >> broj;
            if (broj < mini) mini = broj;
            suma ^= broj;
            real_sum += broj;
        }
        if (suma != 0)
        {
            fout << "Case #" << brojac + 1 << ": NO" << endl;
        }
        else
        {
            fout << "Case #" << brojac + 1 << ": " << real_sum - mini << endl;
        }
    }
    return 0;
}
