#include <fstream>
#include <cmath>

using namespace std;

int main()
{
    ofstream fout("A-large.out");
    ifstream fin("A-large.in");
    int u;
    fin>>u;
    for (int v(0);v<u;v++)
    {
        int n,m;
        fin>>n>>m;
        fout<<"Case #"<<v+1<<": ";
        int k=(1<<n);
        if (m%k==k-1)
            fout<<"ON"<<endl;
        else
            fout<<"OFF"<<endl;
    }
}
