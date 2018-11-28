#include <iostream>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>
#include <sstream>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define mp make_pair
#define tr(i,v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)
void tst()
{
        int n;
        cin >> n;
        vector<int> w(n),p(n);
        for(int i=0;i<n;i++)
            cin >> w[i];
        for(int i=0;i<n;i++)
            cin >> p[i];
        vector<int> ind(n);
        for(int i=0;i<n;i++)
            ind[i] = i;

        for(int it=0;it<=n;it++)
        {
            for(int i=0;i+1<n;i++)
            {
                int j = i+1;
                if( 
                        (100*w[i] + (100-p[i])*w[j] > 100*w[j]+(100-p[j])*w[i])
                        || 
                        (100*w[i] + (100-p[i])*w[j] > 100*w[j]+(100-p[j])*w[i] && ind[i]>ind[j])
                  )
                {
                    swap(w[i],w[j]);
                    swap(p[i],p[j]);
                    swap(ind[i],ind[j]);
                }
            }
        }
        for(int i=0;i<n;i++)
            cout << ' ' << ind[i];

        cout << endl;
}

int main()
{
    int t;
    cin >> t;
    for(int i=1;i<=t;i++)
    {
        cout << "Case #" << i << ":";
        tst();
    }
}
