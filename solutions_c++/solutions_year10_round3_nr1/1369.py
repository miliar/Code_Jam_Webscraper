#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cassert>

using namespace std;

const int maxNwires=1000;
int L[maxNwires],R[maxNwires];
int N;

inline int sign(int x)
{
    return x>0?1: (x<0?-1:0);
}

int main()
{
    cout << "Hello world!" << endl;

    int Tlines;

    ifstream fin("in");
    //ofstream fout("/dev/stdout");
    ofstream fout("out");
    fin>>Tlines;
    for(int t=1;t<=Tlines;++t)
    {
        fin>>N;
        for (int i=0;i<N;++i)
        {
            fin>>L[i]>>R[i];
        }
        if (fin.fail())
        {cerr<<"IN ERROR!";exit(1);}

        //calc
        int count=0;
        for (int i=0;i<N-1;++i)
            for (int j=i+1;j<N;++j)
            {
                int dL=L[i]-L[j];
                int dR=R[i]-R[j];
                assert(dL!=0 && dR!=0);

                if( (dL<0 && dR>0)
                 || (dL>0 && dR<0))
                        ++count;
            }


        fout<<"Case #"<<t<<": ";
        fout<<count<<"\n";
    }

    if (fout.fail())
    {cerr<<"OUT ERROR!";exit(1);}

    return 0;
}
