#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
#define MAXN 10010
#define ll long long

class vein
{
    public:
        ll d,l;
}v[MAXN];

bool cmp(vein a,vein b)
{
    return a.d<b.d;
}
int T,N,D;
ll f[MAXN];

int main()
{
    freopen("out.txt","w",stdout);
    freopen("in.in","r",stdin);
    cin>>T;
    int t=0;
    while(T--)
    {
        memset(f,0,sizeof(f));
        cin>>N;
        for(int i=0;i<N;i++) cin>>v[i].d>>v[i].l;
        sort(v,v+N,cmp);
        cin>>D;

        f[0]=v[0].d+min(v[0].d,v[0].l);
        for(int i=1;i<N;i++) for(int j=0;j<i;j++)
        {
            if(f[j]>=v[i].d)
            {
                f[i]=max(f[i],v[i].d+min(v[i].d-v[j].d,v[i].l));

            }
        }
        ll reach=0;

        for(int i=0;i<N;i++) reach=max(reach,f[i]);
        cout<<"Case #"<<++t<<": ";
        if(reach<D) cout<<"NO"<<endl;
        else cout<<"YES"<<endl;
    }
    //while(1);
    return 0;
}
