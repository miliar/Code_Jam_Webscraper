#include <iostream>
#include <cstdio>
using namespace std;
const int maxn=100000;
char c[maxn][3],d[maxn][2],e[maxn];
int sc,sd,n,r,t1;

bool chck()
{
    if (r > 0)
    for (int i = 0; i < sc; i++)
    if ((c[i][0]==e[r])&&(c[i][1]==e[r-1])||
        (c[i][1]==e[r])&&(c[i][0]==e[r-1])){
            e[--r] = c[i][2];
            return true;
        }
    int x = maxn;
    for (int i = r-1; i > -1; i--)
        for (int j = 0; j < sd; j++)
        if ((d[j][0]==e[r])&&(d[j][1]==e[i])||
            (d[j][1]==e[r])&&(d[j][0]==e[i]))
                if (i < x) x = i;
    if (x != maxn){
        r = - 1;
        return true;
    }
    return false;
}

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>t1;
    for (int t2 = 1; t2 <= t1; t2++){
        r=-1;
        cin>>sc;
        for (int i = 0; i < sc; i++)
            cin>>c[i][0] >>c[i][1] >>c[i][2];
        cin>>sd;
        for (int i = 0; i < sd; i++)
            cin>>d[i][0] >>d[i][1];
        cin>>n;
        for (int i = 0; i < n; i++){
            cin>>e[++r];
            while ((r>-1)&&(chck()));
        }
        cout<<"Case #" <<t2 <<": [";
        if (r >= 0){
            cout<<e[0];
            for (int i = 1; i <= r; i++)
                cout<<", "<<e[i];

        }
        cout<<"]"<<endl;
    }
}
