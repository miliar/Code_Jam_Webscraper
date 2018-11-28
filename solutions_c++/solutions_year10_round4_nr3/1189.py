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

int n,m;
bool ma[1500][1500][2];
int main()
{
    int tt;
    cin>>tt;
    forn(cc,tt)
    {
        forn(i,200)
            forn(j,200)
                forn(k,2)
                    ma[i][j][k] = false;
        cin>>n;
        forn(i,n)
        {
            int x1,x2,y1,y2;
            cin>>x1>>y1>>x2>>y2;
            forsn(j,x1,x2+1)
            {
                forsn(k,y1,y2+1)
                {
                 //   cout<<j<<" "<<k<<endl;
                    ma[j][k][0] = true;
                }
            }
        }
        bool entro = true;
        int k = 0;
        while(entro)
        {
            entro = false;
            forn(i,102)
            {
                forn(j,102)
                    ma[i][j][(k+1)%2] = false;
            }
           /* forn(i,7)
            {
                forn(j,7)
                    cout<<ma[i][j][k%2];
                cout<<endl;

            }
            cout<<endl;*/
            forn(i,102)
            {
                forn(j,102)
                    if (ma[i][j][k%2])
                    {
                        if (ma[i][j-1][k%2] ||ma[i-1][j][k%2])
                        {
                            entro = true;
                            ma[i][j][(k+1)%2] = true;
                        }
                    }
                    else
                    {
                        if (ma[i][j-1][k%2] && ma[i-1][j][k%2])
                        {
                            entro = true;
                            ma[i][j][(k+1)%2] = true;
                        }
                    }
            }
            k++;


        }



        cout<<caso(cc+1, k);
    }
    return 0;
}
