#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream ifile("C-small.in");
    ofstream ofile("C-samll.txt");
    int t, r, k, n;
    ifile >> t;
    for(int i=0;i<t;++i)
    {
        ifile >> r >> k >> n;
        int *group = new int[n];
        for(int j=0;j<n;++j)
            ifile >> group[j];
        int ptr = 0;
        int euros = 0;
        for(int times=0;times<r;++times)
        {
            int rided = 0;
            for(int j=0;j<n;++j)
            {
                int tmp = rided;
                tmp += group[ptr];
                if(tmp <= k)
                {
                    rided = tmp;
                    ptr = (ptr+1 == n ? 0 : ptr+1);
                }
                else
                    break;
            }
            euros += rided;
        }
        ofile << "Case #" << i+1 << ": " << euros << endl;
    }
    return 0;
}
