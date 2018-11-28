#include <iostream>
#include <fstream>
using namespace std;

fstream fin,fout;

int t,a,b,ans,tim,tmp,xxx,mul;
int f[2000001];

int main()
{
    fin.open("C-small-attempt0.in",ios::in);
    fout.open("C_ans.out",ios::out);
    fin >> t;
    for (int l = 0; l < t; l++)
    {
        ans = 0;
        fin >> a >> b;
        mul = 1;
        for (int i = a; i <= b; i++) f[i] = 0;
        for (int i = a; i <= b; i++)
            if (f[i] == 0)
            {
                tmp = i;
                xxx = 0;
                tim = 1;
                while (i >= mul*10) mul *= 10;
                while (true)
                {
                    f[tmp] = 1;
                    xxx = tmp % 10;
                    tmp = tmp / 10 + xxx * mul;
                    if (tmp != i)
                    {
                        if (tmp >= a && tmp <= b) tim++;
                    }
                    else break;
                }
                ans += tim * (tim - 1) / 2;
            }
        fout << "Case #" << l+1 << ": " << ans << endl;
    }
    fout.close();
}
