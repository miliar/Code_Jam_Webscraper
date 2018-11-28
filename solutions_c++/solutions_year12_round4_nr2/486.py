#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <list>
#include <utility>
#include <string>

class Found{};

using namespace std;

typedef pair<int,int> pdd;

vector<pair<int, int> > r;
vector<pdd > pos;

typedef long long ll;

bool check(int x, int y, int W, int L, int k)
{
    if(x<0 || y<0 || x>W || y>L)
        return false;
    for(int i=0; i<=k; i++)
    {
        long long R=r[k+1].first+r[i].first;
        long long Ds= ll(x-pos[i].first)*ll(x-pos[i].first) + ll(y-pos[i].second)*ll(y-pos[i].second) ;
        if(  R*R > Ds )
            return false;
    }
    return true;
}

pair<int, int> f(int x, int y, int r, int dir)
{
    if(dir==1)
        x+=r;
    if(dir==2)
        y+=r;
    if(dir==3)
        x-=r;
    if(dir==0)
        y-=r;

    return make_pair(x,y);
}


int main()
{
    ifstream in("C:\\Users\\Olexandr\\Desktop\\B-large.in");
    ofstream out("C:\\Users\\Olexandr\\Desktop\\output.txt");
    int T;
    in>>T;


    for(int t=0; t<T; t++)
    {
        out<<"Case #"<<(t+1)<<": ";
        
        int N,W,L;
        in>>N>>W>>L;
        r.resize(N);
        for(int i=0; i<N; i++)
        {
            in>>r[i].first;
            r[i].second=i;
        }

        sort(r.rbegin(), r.rend());

        pos.resize(N);
        int y=0, x=0;
        int dir=1;
        for(int i=0; i<N; i++)
        {
            pos[i]=make_pair(x,y);
            if(i!=N-1)
            {
                int nx=f(x,y,r[i].first+r[i+1].first, dir).first;
                int ny=f(x,y,r[i].first+r[i+1].first, dir).second;
                if(  check(nx, ny, W, L, i) )
                {
                    x=nx;
                    y=ny;
                }
                else
                {
                    dir++;
                    dir%=4;
                    x=f(x,y,r[i].first+r[i+1].first, dir).first;
                    y=f(x,y,r[i].first+r[i+1].first, dir).second;
                }
            }

        }
        vector<pdd > result(N);
        for(int i=0; i<N; i++)
        {
            result[r[i].second]=pos[i];
        }

        sort(pos.begin(), pos.end());
        for(int i=0; i<N; i++)
        {
            out<<result[i].first<<' '<<result[i].second<<(i==N-1?'\n':' ');
        }
    }
    system("pause>nul");
    return 0;
}