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
#define dforsn(i,s,n) for(int i = (int)n-1; i>= (int)(s);i--)
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define esta(a,c) (find(c.begin(),c.end(), a) != c.end())
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
#define MAX 2147483647
#define caso(x,y) "Case #"<<x<<": " <<y<<endl

int a[150000];
int v[150000];
int n,m;
int main()
{
    int tt;
    cin>>tt;
    forn(cc,tt)
    {
        int k, b,t;
        cin>>n>>k>>b>>t;
      //  cout<<n<<" "<<k<<" "<<b<<" "<<t<<" "<<endl;
        forn(i,n)
        {
            cin>>a[i];
         //   cout<<a[i]<<" ";
         /*   if (i != 0)
            if (a[i] <= a[i-1])
                cout<<"mall"<<endl;*/
        }
     //   cout<<endl;
        forn(i,n)
        {
            cin>>v[i];
       //         cout<<v[i]<<" ";
        }
       // cout<<endl;
        int j = n-1;
        int re= 0;
        int mal = 0;
     //   cout<<n<<endl;
   //     cout<<k<<endl;
        while(k > 0 && j >= 0)
        {
            int aux = ((b - a[j]) / v[j]) ;
            if ((b - a[j]) % v[j] != 0 ) aux++;
            //cout<< aux<< " " <<t<<endl;
            if (aux <= t )
            {
                k--;
                re+= mal;
            }
            else mal++;
            j--;
        }
        if (k != 0)
            cout<<caso(cc+1,"IMPOSSIBLE");
        else
            cout<<caso(cc+1, re);
    }
    return 0;
}

