#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
using namespace std;
struct move
{
    int x;
    int rob;
};
struct block
{
    int time;
    int time_st;
};
vector<move> v;
vector<block> res;
int main()
{
    ifstream cin("a.txt");
    ofstream cout("b.txt");
    char c;
    int n, k, i, j, x, r;
    int rob[3];
    move z;
    block q;
    cin>>k;
    for (i=0;i<k;++i)
    {
        cin>>n;
        rob[1]=1;
        rob[2]=1;
        v.clear();
        v.reserve(n);
        r=0;
        for (j=0;j<n;++j)
        {
            cin>>c>>z.x;
            if (c=='O')
            {
                z.rob=1;
            }
            else
            {
                z.rob=2;
            }
            v.push_back(z);
        }
        res.clear();
        res.reserve(n);
        for (j=0;j<n;++j)
        {
            x=v[j].rob;
            q.time=0;
            q.time_st=abs(v[j].x-rob[x]);
            while (v[j].rob==x && j<n)
            {
                q.time+=(abs(v[j].x-rob[x])+1);
                rob[x]=v[j].x;
                ++j;
            }
            --j;
            res.push_back(q);
        }
        for (j=0;j<res.size();++j)
        {
            if (j!=0)
            {
                res[j].time-=min(res[j].time_st, res[j-1].time);
            }
            r+=res[j].time;
        }
        cout<<"Case #"<<(i+1)<<": "<<r<<endl;
    }
    return 0;
}
