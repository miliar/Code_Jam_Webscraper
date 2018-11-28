#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
#include<map>
#include<list>
#include<cmath>
#include<set>

using namespace std;
#define forn(i,n) for(int i=0;i<(n);i++)
#define forsn(i,s,n) for(int i = (int)s; i< (int)(n);i++)
#define dforn(i,n) for(int i=(int)(n-1);i>=0;i--)
#define dforsn(i,s,n) for(int i = (int)n; i>= (int)(s);i--)
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define esta(a,c) (find(c.begin(),c.end(), a) != c.end())
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
#define MAX 2147483647
#define caso(x,y) "Case #"<<x<<": " <<y<<endl

int a[150000];

bool de[1500];
int es(int n)
{
    vector<int> se ;

    forn(i,n)
        if (de[i])
            se.pb(i);
    se.pb(n);
    int aux = se.size();
    while(aux != 1)
    {
        int mejori = -1;
        forn(i,se.size())
        {
            if (aux == se[i])
            {
                mejori = i;
            }
        }
        if (mejori == -1)
            return 0;
        aux = mejori+1;
    }
    return 1;
}
int r(int i, int n)
{
    if (i == n-1)
        return es(n);
    de[i] = false;
    int mejor = r(i+1,n)%100003;
    de[i] = true;
    mejor = (mejor + r(i+1,n))%100003 ;
    de[i] = false;
    return mejor%100003;
}


int main()
{
    int tt;
    cin>>tt;
    int re[28];
    forn(i,27)
    {
        if (i >2)
            re[i] = r(2,i);
    }
    forn(cc,tt)
    {
        int n ;
        cin>>n;
        n++;
        cout<<caso(cc+1, re[n] );
    }
    return 0;
}

