#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("input.in");
    ofstream fout("output.out");

    int t;
    fin>>t;
    for(int ca = 1 ;ca<=t;++ca)
    {
        int n;
        fin>>n;
        int count = 0;
        int temp;
        for(int i=1;i<=n;++i)
        {
            fin>>temp;
            if(temp!=i)
                ++count;
        }
        fout<<"Case #"<<ca<<": "<<count<<".000000"<<endl;
    }

    fin.close();
    fout.close();
    return 0;
}