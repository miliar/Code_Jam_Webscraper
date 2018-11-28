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


int main()
{
    freopen("a3.in","r",stdin);
    freopen("A-small.out","w",stdout);
    int t;
    cin>>t;
    forn(cc,t)
    {
        int n,m;
        cin >>n>>m;
        vector<string>arr;
        forn(i,n)
        {
            string a = "";
            cin>>a;
            arr.pb(a);
        }
        bool entro = false;
        forn(i,n)
        {
            forn(j,m)
            {
                if (arr[i][j] == '#' )
                {
                    if (j == m -1 || i == n-1)
                    {
                        entro = true;
                        break;
                    }
                    if (arr[i][j+1] != '#' || arr[i+1][j] != '#' || arr[i+1][j+1] != '#')
                    {
                        entro = true;
                        break;
                    }
                    arr[i][j] = '/';
                    arr[i+1][j+1] = '/';
                    arr[i+1][j] = '\\';
                    arr[i][j+1] = '\\';
                }
            }

        }
        cout<<"Case #"<<cc+1<<":"<<endl;
        if (entro)
        {
            cout<<"Impossible"<<endl;
        }
        else
        {
            forn(i,n)
                cout<<arr[i]<<endl;
        }
    }
	return 0;

}
