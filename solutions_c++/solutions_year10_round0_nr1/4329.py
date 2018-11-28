#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream fin("snappers.in");
    ofstream fout("snappers.out");
    long long t, n, k, mxpw;
    bool snappers[100], brk;
    fin>>t;
    for(int i=0; i<t; i++)
    {
        memset(snappers, false, 100);
        mxpw=0;
        fin>>n>>k;
        for(int l=0; l<k; l++)
        {
            mxpw=0;
            for(int j=0; j<n; j++)
            {
                if(snappers[j]==true)
                {
                    mxpw=j+1;
                    snappers[j]=!snappers[j];
                }
                else if (j==mxpw)
                {
                    snappers[j]=!snappers[j];
                    break;
                }
            }
        }
        for(int j=0; j<n; j++)
        {
            if(snappers[j]==false)
            {
            brk=true;
            break;
            }
            else brk=false;
        }
        if(brk==true)
        {
            fout<<"Case #"<<i+1<<": OFF"<<endl;
        }
        else fout<<"Case #"<<i+1<<": ON"<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
