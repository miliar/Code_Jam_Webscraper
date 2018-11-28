#include<algorithm>
#include<cmath>
#include<cstdio>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<vector>

#define forn(i,n) for(int i=0;i<(int)n;i++)
#define dforn(i,n) for(int i=(int)n-1;i>=0;i--)
#define all(v) v.begin(),v.end()

using namespace std;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int casos;
    cin >> casos;
    for(int casito = 1; casito <= casos; casito++)
    {
        int n,a=1000000,b,c=0,sum=0;
        cin >> n;
        forn(i,n)
        {
            cin >> b;
            if(b<a)
                a = b;
            c^=b;
            sum += b;
        }
        sum -= a;
        cout << "Case #"<< casito << ": ";
        if(c==0)
            cout << sum << endl;
        else
            cout << "NO" << endl;
    }
}
