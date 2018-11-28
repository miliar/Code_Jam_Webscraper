#include <iostream>
#include <fstream>
#include <queue>
using namespace std;
int main()
{
    ifstream fin("coaster.in");
    ofstream fout("coaster.out");
    long long t, r, k, n, gi, euros=0, curride=0, grps;
    queue<long long> ppl;
    fin>>t;
    for(int i=0; i<t; i++)
    {
            while (!ppl.empty())
            {
            ppl.pop();
             }

            euros=0;
            fin>>r>>k>>n;
            for(int j=0; j<n; j++)
            {
                    fin>>gi;
                    ppl.push(gi);
            }
            for(int j=0; j<r; j++)
            {
                    grps=0;
                    curride=0;
                    while((curride+ppl.front()<=k)&&(grps<n))
                    {
                                                   curride+=ppl.front();
                                                   ppl.push(ppl.front());
                                                   ppl.pop();
                                                   grps++;
                    }
                    euros+=curride;
            }
            fout<<"Case #"<<i+1<<": "<<euros<<endl;
    }
    fout.close();
    fin.close();
    return 0;
}
