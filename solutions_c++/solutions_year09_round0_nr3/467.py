#include <cstdlib>
#include <iostream>
#include <fstream>
#include <map>
#include <cstring>
using namespace std;
string ss="welcome to code jam";

int main(int argc, char *argv[])
{
    long long num[510][22];
    int ll=ss.length();
    int n;
    string s;
    ifstream fin("C-large.in.txt");
    ofstream fout("outputc_large.txt");
    fin>>n;
    getline(fin,s);
    for (int i=1;i<=n;i++)
    {
        getline(fin,s);
        for (int j=0;j<510;j++)
            for (int k=0;k<22;k++) num[j][k]=0;
        int l=s.length();
        if (s[0]==ss[0]) num[0][0]=1;
        for (int j=1;j<l;j++)
        {
            for (int k=0;k<ll;k++)
            {
                if (s[j]!=ss[k])
                    num[j][k]=num[j-1][k];
                else{
                    if (k>0)
                        num[j][k]=(num[j-1][k]+num[j-1][k-1]) % 10000;
                    else
                        num[j][k]=(num[j-1][k]+1) % 10000;
                }
            }
        }
        int tt=num[l-1][ll-1]%10000;
        fout<<"Case #"<<i<<": ";
        if (tt<10) fout<<"000";
        else if (tt<100) fout<<"00";
        else if (tt<1000) fout<<"0";
        fout<<tt<<endl;
    }
    system("pause");
    return 0;
}
