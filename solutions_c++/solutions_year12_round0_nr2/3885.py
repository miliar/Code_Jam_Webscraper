#include <iostream>
#include <fstream>
using namespace std;

fstream fin,fout;

int t,n,ans,p,s;
int ma,mi;
int a[100];

int main()
{
    fin.open("B-small-attempt0.in",ios::in);
    fout.open("ans2.out",ios::out);
    fin >> t;
    for (int l = 0; l < t; l++)
    {
        fin >> n >> s >> p;
        ans = 0;
        for (int i = 0; i < n; i++)
        {
            fin >> a[i];
            mi = a[i] / 3;
            if (mi * 3 == a[i]) ma = mi; else ma = mi + 1;
            if (ma >= p) ans++;
            else
                if (mi*3 + 1 != a[i] && s > 0 && ma + 1 >= p && mi > 0)
                {
                    ans++;
                    s--;
                }
        }
        fout << "Case #" << l+1 << ": "<< ans << endl;
    }
    fout.close();
}
