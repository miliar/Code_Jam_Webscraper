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
int n,m;
set<string> ma;
int main()
{
    int tt;
    cin>>tt;
    forn(cc,tt)
    {
        ma.clear();
        cin>>n>>m;
        ma.insert("");
        forn(i,n)
        {
            string ss;
            cin>>ss;
            string aux = "";
            forn(j,ss.size())
            {
                if(ss[j] == '/')
                {
                    ma.insert(aux);
                }
                aux+=ss[j];
            }
            ma.insert(aux);
        }
        int cont = 0;
        forn(i,m)
        {
            string ss;
            cin>>ss;
            string aux = "";
            forn(j,ss.size())
            {
                if(ss[j] == '/')
                {
                    if (ma.find(aux) == ma.end())
                    {
                        cont++;
                //        cout<<aux<<endl;
                        ma.insert(aux);
                    }
                }
                aux+=ss[j];
            }
            if (ma.find(aux) == ma.end())
                    {
                   //     cout<<aux<<endl;
                        cont++;
                        ma.insert(aux);
                    }
        }


        cout<<caso(cc+1, cont );
    }
    return 0;
}
