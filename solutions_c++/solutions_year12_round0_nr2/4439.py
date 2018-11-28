#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

bool check1(int x, int p)
{
     int res = x%3;
     int y = x/3;
     if (res!=0) y++;
     if (y>=p) return true;
        else return false;
}

bool check2(int x, int p)
{
     int res = x%3;
     int y = x/3+res;
     if (y>=p || (res==0 && y!=0 && y+1==p)) return true;
        else return false;
}

int min(int a, int b)
{
    if (a<b) return a; else return b;
}
     
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,s,p,a[110];
    bool b[110];
    cin>>t;
    for (int i=0; i<t; i++)
    {
        cin>>n>>s>>p;
        memset(a,0,sizeof(a));
        for (int j=0; j<n; j++) b[j] = false;    
        for (int j=0; j<n; j++) cin>>a[j];
        int k=0;
        for (int j=0; j<n; j++)
            if (check1(a[j],p)) {b[j] = true; k++;}
        int k1=0;
        for (int j=0; j<n; j++)
            if (!b[j] && check2(a[j],p)) k1++;
        k += min(k1,s);
        cout<<"Case #"<<i+1<<": "<<k;
        if (i!=t-1) cout<<endl;
        }
    //system("pause");
    return 0;
}
