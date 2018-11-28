#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <map>
using namespace std;

map < pair<int, int> , int> mp;
int main()
{
    int t, i, j;
    int a, b, k, rj, jk, kk;
    long long cnt;
    ifstream inf("c-large.in");
    ofstream ouf("c.out");
    inf >> t;
    for (i=0; i<t; i++)
    {
        inf >> a >> b;
        cnt = 0;
        long long lkk = 1, ljj, num = 0;
        while (lkk<=a)
        {
            lkk *= 10;
            num++;
        }
        int z;
        mp.clear();
        for (j=a; j<=b; j++)
        {
            ljj = j+lkk*j;
            long long shf = 1;
            for (z=0; z<num; z++)
            {
                shf *= 10;
                rj = (ljj/shf) % lkk;
                if ((rj>j) && (a<=rj) && (rj<=b))
                {
                    if (mp[make_pair(j,rj)]!=1)
                    {
                        mp[make_pair(j,rj)]=1;
                        cnt++;
                    }
                }
            }
        }
        ouf << "Case #" << (i+1) << ": " << cnt << endl;
    }
    inf.close();
//    system("pause");
    return 0;
}
