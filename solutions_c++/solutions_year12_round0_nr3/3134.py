#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("3.in");
ofstream fout("3.out");
int a,b;
long long ans;
int p,q,n,nn;

int main()
{
    int t,i;
    fin >> t;
    for (i=1;i<=t;i++)
    {
        fin >> a >> b;
        ans = 0;
        for (int j=a;j<=b;j++)
        {
            nn = 1;
            while (j>=nn) nn *= 10;
            
            n = 10;
            while (j>=n)
            {
                p = (j%n)*(nn/n) + j/n;
                if ((a<=p)&&(p<=b)&&(p!=j)) ans++;//if (j<p) cout << j <<' '<< p << endl;}
                n *= 10;
            }
        }
        fout << "Case #" << i << ": " << ans/2 << endl;
    }
    return 0;
}
