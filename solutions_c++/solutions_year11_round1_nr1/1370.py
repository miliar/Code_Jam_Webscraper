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
    freopen("a3.in","r", stdin);
     freopen("a.out","w", stdout);
    int t;
    cin>>t;
    forn(cc,t)
    {
        int n,d,g;
        cin>>n>>d>>g;
      //  cout<<n<<" "<<d<<" "<<g<<endl;
        string pos = "Possible";
        string impo = "Broken";
        if (d == 100 && g == 100)
            cout<<caso(cc+1,pos);
        else
        {
            if (d == 0 && g == 0)
            {
                cout<<caso(cc+1,pos);
                continue;
            }
            if (d != 0 && g == 0)
            {
                cout<<caso(cc+1,impo);
                continue;
            }


         //   if(1.0/5.0 == 0.2)
           //     cout<<"hola"<<endl;
            if (g == 100)
                cout<<caso(cc+1,impo);
            else
            {
                if (n >= 100)
                    cout<<caso(cc+1,pos);
                else
                {
                    bool entro = false;
                    forsn(i,1,n+1)
                    {
                        forn(j,i+1)
                            if ((double)j/(double)i == (double)d/100.0)
                            {
                                entro= true;
                               // cout<<i<<" "<<j<<endl;
                                break;
                            }

                    }
                    if (entro)
                        cout<<caso(cc+1,pos);
                    else
                        cout<<caso(cc+1,impo);
                }

            }
        }
    }
	return 0;

}
