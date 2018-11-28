#include <iostream>
#include <string>
#include <fstream>
using namespace std;

const char f[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int n;
string st;
ifstream fin("A-small-attempt0.in");
ofstream fout("1.txt");

int main()
{
    int n,i;
    char c;
    fin >> n;
    fin.get();
    for (i=1;i<=n;i++)
    {
        getline(fin,st);
        fout << "Case #" << i << ": ";
        for (int j=0;j<st.length();j++)
        {
            if (st[j]==' ') fout << ' ';
            else fout << f[st[j]-'a'];
        }
        fout << endl;
    }
    return 0;
}
