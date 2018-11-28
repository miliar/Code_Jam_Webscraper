#include <iostream>
using namespace std;
#define M 1050
int lost[M];
int tree[M*2];
class node
{
public:
    int id;
    int f;
    int c;
};
node nod[M*2];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int c;
    cin>>c;
    int p;
    int n;
    for(int ca=1;ca<=c;++ca)
    {
        int rst=0;
        cin >> p;
        n = 1<<p;
        //cout << n;
        for(int i=0;i<n;++i)
        {
            cin>>lost[i];
            nod[i].id=i;
        }
        int m=n/2;
        int t;
        int haizi=0;
        int idx=n;
        while(m)
        {
            //int preidx=idx;
            for(int i=0;i<m;++i)
            {
                cin>>t;
                nod[idx].id=idx;
                nod[haizi++].f = idx;
                nod[haizi++].f = idx;
                
                nod[idx].c=0;
                ++idx;
            }
            m/=2;
            //haizi=predix;
        }
        nod[haizi].f=0;
        //cout <<"haizi:" <<haizi<<endl;
        for(int i=0;i<n;++i)
        {
            int look=p-lost[i];
            //cout << "for " << i << " Look " << look<<endl;
            for(int j=p;j>0;--j)
            {
                if(look==0)break;
                idx=i;
                for(int k=0;k<j;++k)
                    idx=nod[idx].f;
                //cout << "node:"<<idx<<endl;
                if(nod[idx].c==0)
                {
                    nod[idx].c=1;
                    ++rst;
                }
                --look;
            }
        }
        cout << "Case #"<<ca<<": " <<rst<<endl;
    }
    return 0;
}
