#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;


int main() {

    int tn;
    long long letters[10000];
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	cin>>tn;
	int i, j, noK, noP, noL;

	F0(i,tn)
	{
	    cin>>noP>>noK>>noL;
	    cout<<"Case #"<<i+1<<": ";

        int c=0;
	    F0(j,noL)
	    {
	        cin>>letters[j];
	        if(letters[j]==0)
                c++;
	    }
        if (noP*noK<noL-c)
            cout<<"impossible\n";
        else
        {
            sort(letters, letters+noL, greater<ll>());
            ll ans=0;
            int count=0;
            int l, m;
            F1(l,noP)
            {
                F0(m,noK)
                {
                    if (count==noL)
                        break;
                    ans+=letters[count++]*l;
                }
                if (count==noL)
                    break;
            }
            cout<<ans<<"\n";
        }
	    /*F0(j, noL)
            cout<<letters[j]<<"\n";*/
	}
}
