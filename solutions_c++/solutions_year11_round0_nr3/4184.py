#include<fstream>
using namespace std;

ifstream fin;
ofstream fout;

int main()
{
    fin.open("vstup.txt");
    fout.open("vystup.txt");

    int n,q,a;
    fin >> n;

    for(int i=0;i<n;i++)
    {

    int min=1000100;
    unsigned long long sucet=0;
    int vys=0;

    fin >> q;

    for(int j=0;j<q;j++)
        {
            fin >> a;
            vys=vys^a;
            sucet = sucet+a;
            if(a<min) min=a;
        }
    if(vys==0) fout << "Case #" << i+1 << ": " << sucet-min << endl;
    else fout << "Case #" << i+1 << ": NO" << endl;
    }

    return 0;
}
