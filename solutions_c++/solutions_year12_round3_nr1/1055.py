#include <cstdlib>
#include <iostream>
#include <vector>
#define N 1010

using namespace std;

vector <int> a[N];
int b[N];
int d[N];
int n;
bool f(int x)
{
    int i,j,k;
    int l;
    if(d[x])
        return true;
    d[x]=1;
    l=a[x].size();
    for(i=0;i<l;i++)
    {
        if(f(a[x][i]))
            return true;
    }
    return false;
}

int main(int argc, char *argv[])
{
    int i,j,k;
    int t;
    int m,o;
    int x,y,z;
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
    o=1;
    cin>>t;
    while(t--)
    {
        cin>>n;
        a[0].clear();
        memset(b,0,sizeof(b));
        for(i=1;i<=n;i++)
        {
            cin>>m;
            a[i].clear();
            for(j=0;j<m;j++)
            {
                cin>>x;
                a[i].push_back(x);
                b[x]=1;
            }
        }
        for(i=1;i<=n;i++)
        {
            if(!b[i])
            {
       //         cout<<i<<endl;
                memset(d,0,sizeof(int)*(n+1));
                if(f(i))
                    break;
            }
        }
        cout<<"Case #"<<o<<": ";
        if(i<=n)
        {
            cout<<"Yes"<<endl;
        }
        else    
            cout<<"No"<<endl;
        o++;
    }
  //  system("PAUSE");
    return EXIT_SUCCESS;
}
