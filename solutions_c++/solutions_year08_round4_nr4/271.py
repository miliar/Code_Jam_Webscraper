#include <iostream>
#include <fstream>

using namespace std;
int x[10],uz[10];

ifstream fin("d.in");
ofstream fout("d.out");

string s,ss;
int T,K, R = 0x3f3f3f3f;

string schimba( string s)
{
    string rez;
    for (int i = 0; i<K; i++)
        rez+= s[x[i]];
    return rez;
}



void calc(string s)
{
    string rez;
    int l = s.length();
    for (int i = 0; i < l / K; i++)
    {
        string aux = s.substr(0, K);
        s.erase(0, K);
        aux = schimba(aux);
        rez += aux;
    }
    int nr = 1;
    for (int i = 1; i<rez.length(); i++)
        if ( rez[i] != rez[i-1] )
            nr++;
    if ( nr < R )
        R = nr;
}

void back(int k)
{
    if ( k == K)
        calc(s);
    else
    for ( int i = 0; i<K; i++)
    {
        if ( !uz[i])
        {
            x[k] = i;
            uz[i] = 1;
            back(k+1);
            uz[i] = 0;
        }
    }
}

int main()
{
    fin>>T;
    for ( int z = 1; z<=T; z++)
    {
        R = 0x3f3f3f3f;
        fin>>K;
        fin>>s;
        back(0);
        fout<<"Case #"<<z<<": "<<R<<"\n";
    }

    return 0;
}
