//#include<iostream>
#include<cstdlib>
#include<fstream>

using namespace std;

int main()
{
    int t;
    ifstream fin("A-small-attempt4.in");
    ofstream fout("output.out");
    string as,g,eng="abcdefghijklmnopqrstuvwxyz ",geng="ynficwlbkuomxsevzpdrjgthaq ";
    fin>>t;
    getline(fin,as);
    for(int i=0;i<t;i++)
    {
        getline(fin,g);
        fout<<"Case #"<<i+1<<": ";
        for(int j=0;j<g.length();j++)
            for(int k=0;k<=26;k++)
                if(g[j]==geng[k])
                {
                    fout<<eng[k];
                    break;
                }
        if(i!=t-1)
            fout<<endl;
    }
    return 0;
}
