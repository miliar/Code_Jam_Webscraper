#include <iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
    long t, i, j, k, num, dig;
    float a[21][200], b[21], ks, mks, pc;
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small-attempt0.out");
    fin>>t;
    for(i=1;i<=t;i++)
    {
        fin>>a[i][0]>>b[i];
        for(j=1;j<=(int)a[i][0];j++)
            fin>>a[i][j];
    }
    for(i=1;i<=t;i++)
    {
        mks = a[i][0] + b[i] + 2;
        for(j=1;j<=(int)a[i][0];j++)
        {
            pc=1;
            for(k=1;k<=((int)a[i][0]-j);k++)
            {
                pc=pc*a[i][k];
            }
            ks = pc*(b[i]-a[i][0] + (float)j + (float)j +1) + (1-pc)*(b[i]-a[i][0] + (float)j + (float)j + b[i] + 2);
            if(ks<mks)
                mks =ks;
        }
        pc=1;
        for(k=1;k<=(int)a[i][0];k++)
        {
            pc=pc*a[i][k];
        }
        ks = pc*(b[i]-a[i][0] +1) + (1-pc)*(b[i] - a[i][0] + 1 + b[i] + 1);
        if(ks<mks)
            mks = ks;
        if(b[i]+2 < mks)
            mks = b[i] + 2;
        num = mks;
        dig = 0;
        for(;num;)
        {
                  dig++;
                  num = num/10;
        }
        dig += 6;
        fout<<"Case #"<<i<<": "<<setprecision(dig)<<mks<<endl;
    }
    return 0;
}
