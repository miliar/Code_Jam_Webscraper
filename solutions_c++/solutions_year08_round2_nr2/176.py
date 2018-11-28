#include <iostream>
using namespace std;
int s[1000];
int a,b,p,C;
int find(int x)
{
    if (s[x]==-1)
        return x;
    s[x]=find(s[x]);
    return s[x];
}
int gcd(int x,int y)
{
    if (y==0) return x;
    return gcd(y,x %y);
}
bool check(int x,int y)
{
     int w,i;
     w=gcd(x,y);
     for (i=2;i*i<=w;i++)
         if (w % i==0)
         {
             if (i>=p) return true;
             while (w % i==0)
                 w /= i;
         }
     if (w>=p) return true;
     else return false;
}
int main()
{
    int Ct,i,j,k,a,b,x,y;
    bool flag;
    int total;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    cin>>C;
    for (Ct=1;Ct<=C;Ct++)
    {
        cin>>a>>b>>p;
        total=0;
        for (i=a;i<=b;i++)
            s[i]=-1;
        for (i=a+1;i<=b;i++)
        {
            x=find(i);
            for (j=a;j<i;j++)
            if (check(i,j))
            {
               y=find(j);
               if (y!=x)
                   s[y]=x;
            }
        }
        for (i=a;i<=b;i++)
           if (s[i]==-1)
               total++;
        cout<<"Case #"<<Ct<<": "<<total<<endl;
    }
    return 0;
}
