#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
using namespace std;

typedef long long int lli;

int main()
{
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    int T;
    cin>>T;
    for (int t=1;t<=T;t++)
    {
        int N,W,L;
        cin>>N>>W>>L;
        vector<int> r(N);
        for (int i=0;i<N;i++) cin>>r[i];
        
        vector<pair<int,int> > ps(N);
        for (int i=0;i<N;i++)
            ps[i].first=r[i],ps[i].second=i;
        sort(ps.begin(),ps.end(),greater<pair<int,int> >());
        
        vector<int> px(N),py(N);
        int count=0;
        for (int x=0,dx;x<W;x+=dx)
        {
            dx=ps[count].first;
            for (int y=0,dy;y<=L;y+=dy)
            {
                dy=ps[count].first;
                px[ps[count].second]=x;
                py[ps[count].second]=y;
                count++;
                if (count>=N) break;
                dy+=ps[count].first;
            }
            if (count>=N) break;
            dx+=ps[count].first;
        }
        cout<<"Case #"<<t<<": ";
        for (int i=0;i<N;i++)
            cout<<px[i]<<" "<<py[i]<<(i+1==N?"\n":" ");
        std::cout<<"Case #"<<t<<endl;
        if (count<N)
        {
           std::cout<<"error"<<endl;
           while (std::cin.get()!='q');
        }
    }
    return 0;
}
