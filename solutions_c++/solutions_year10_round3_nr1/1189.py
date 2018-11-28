#include <iostream>
#include<fstream>

using namespace std;

ifstream fin("a+.in");
ofstream fout("a+.out");

struct elem{
    long int x,y;
} v[1002];

int metszi(int i,int j)
{
    if(v[i].x>v[j].x&&v[j].y>v[i].y)
        return 1;
    if(v[i].x<v[j].x&&v[j].y<v[i].y)
        return 1;
    return 0;
}
int t,n;

int main()
{
    fin>>t;
    for(int test=1;test<=t;test++)
    {
        fout<<"Case #"<<test<<": ";
        int db=0;
        fin>>n;
        for(int i=1;i<=n;i++)
        {
            fin>>v[i].x>>v[i].y;
            for(int j=1;j<i;j++)
                if(metszi(i,j)==1)
                    db++;
        }
        fout<<db<<"\n";
        for(int i=1;i<=n;i++)
        {
            v[i].x=0;
            v[i].y=0;
        }
    }
    return 0;
}
