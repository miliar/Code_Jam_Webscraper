#include <iostream>
#include <fstream>

#define maxN(x,y) ((x>y)?(x):(y))

using namespace std;

int main()
{
    ifstream fin("input.in");
    ofstream fout("output.out");

    int t;
    fin>>t;

    for(int i = 1;i<=t;++i)
    {
        int n;
        long min = 9999999;
        long sum = 0;
        long temp;
        long now=0;
        fin>>n;
        for(int j = 0;j!=n;++j)
        {
            fin>>temp;
            sum+=temp;
            if(temp<min) min = temp;
            now^=temp;
        }
        if(now != 0)
        {   
            fout<<"Case #"<<i<<": NO"<<endl;
        }
        else
        {
            fout<<"Case #"<<i<<": "<<sum - min<<endl;
        }
    }
    fin.close();
    fout.close();
    return 0;
}