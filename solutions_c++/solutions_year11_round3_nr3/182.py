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
    freopen("c.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int t;
    cin>>t;
    forn(cc,t)
    {
        int n,l,h;
        cin>>n>>l>>h;
        vector<int> note;
        forn(i,n)
        {
            int a;
            cin>>a;
            note.pb(a);

        }
        int res = -1;
        forsn(i,l,h+1)
        {
            bool bien = true;
            forn(j,n)
            {
                if (((double)note[j] / (double)i != (int)((double)note[j] / (double)i ) ) && ((double)i / (double)note[j] != (int)((double)i/ (double)note[j]  ) ))
                {
                    bien = false;
                    break;
                }
            }
            if (bien)
            {
                res = i;
                break;
            }



        }
        if (res != -1)
            cout<<caso(cc+1,res);
        else
            cout<<caso(cc+1,"NO");
    }
	return 0;

}
