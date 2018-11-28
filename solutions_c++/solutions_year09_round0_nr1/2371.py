#include <fstream>
#include <string>

using namespace std;

#define DMAX 5000
#define LMAX 16
#define MAXX 500

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.txt");
    int n,l,i,j,y,d,z;
    bool f=false;
    string v;
    string str[DMAX];
    int casei=0;
    fin>>l>>d>>n;
    fin.get();
    for(i=0;i<d;++i)
        fin>>str[i];
    for(i=0;i<n;++i)
    {
        fin>>v;
        casei=0;
        for(j=0;j<d;++j)
        {
            y=0;
            for(z=0;z<l;++z)
            {
                if(v[y]=='(')
                {
                    while(v[y]!=')')
                    {
                        if(v[y]==str[j][z])
                            f=true;
                        ++y;
                    }
                    if(f==false)
                        break;
                    f=false;
                }
                else if(v[y]!=str[j][z])
                    break;
                ++y;
            }
            if(z==l)
                casei++;
        }
        fout<<"Case #"<<i+1<<": "<<casei<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
