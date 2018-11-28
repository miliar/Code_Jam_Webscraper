#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
    freopen("B-large.in","rt",stdin);
    freopen("b.txt","wt",stdout);
    int N;
    scanf("%d",&N);
    vector<pair<pair<int,int>,int> > vr;
    int tr;
    int A,B;
    vector<int> Ar,Br;
    int a,b;
    int z,x,c,v;
    for(int Q=0;Q<N;Q++)
    {
        vr.clear();
        Ar.clear();
        Br.clear();
        A=0;
        B=0;
        scanf("%d",&tr);
        scanf("%d%d",&a,&b);
        for(int i=0;i<a;i++)
        {
            scanf("%d:%d %d:%d",&z,&x,&c,&v);
            vr.push_back(make_pair(make_pair(x+z*60,v+c*60),1));
        }
        for(int i=0;i<b;i++)
        {
            scanf("%d:%d %d:%d",&z,&x,&c,&v);
            vr.push_back(make_pair(make_pair(x+z*60,v+c*60),2));
        }
        sort(vr.begin(),vr.end());
        for(int i=0;i<vr.size();i++)
        {
            if(vr[i].second==1)
            {
                Br.push_back(vr[i].first.second+tr);
                sort(Ar.begin(),Ar.end());
                int j=0;
                for(;j<Ar.size() && Ar[j]>vr[i].first.first;j++);
                if(j==Ar.size())
                    A++;
                else
                    Ar.erase(Ar.begin()+j);
            }
            if(vr[i].second==2)
            {
                Ar.push_back(vr[i].first.second+tr);
                sort(Br.begin(),Br.end());
                int j=0;
                for(;j<Br.size() && Br[j]>vr[i].first.first;j++);
                if(j==Br.size())
                    B++;
                else
                    Br.erase(Br.begin()+j);
            }
        }
        printf("Case #%d: %d %d\n",Q+1,A,B);
    }
    return 0;
}
