#include<iostream>
#include<fstream>
#include<queue>
using namespace std;
int main()
{
    ifstream fin("input.in");
    ofstream fout("output.txt");
    int noc,n,i=1,j=0,gi,t;
    long long r,k,pound;
    queue <int> g;
    fin>>noc;
    while(i<=noc)
    {
        pound=0;
        fin>>r>>k>>n;;
        for(j=0;j<n;j++)
        {
            fin>>gi;
            g.push(gi);
        }
        while(r)
        {
            j=k;
            t=g.size();
            while(j>=g.front() && t>0)
            {
                pound=pound+g.front();
                j=j-g.front();
                g.push(g.front());
                g.pop();
                t=t-1;
            }
            r--;
        }
        fout<<"Case #"<<i<<": "<<pound<<endl;
        while(!g.empty())
        g.pop();
        i++;
    }
}
