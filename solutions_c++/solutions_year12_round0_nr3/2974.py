#include <iostream>
#include <cmath>
#include <set>
using namespace std;

int tn;
int a,b;
int n;
const int deg[10] = {1,10,100,1000,10000,100000,1000000,10000000};
set<int> v;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
    
    int i,j;
    cin >> tn;
    for (int t=1;t<=tn;t++)
    {
        cin >> a >> b;
        n = (int)(log(a)/log(10))+1;
        int ans = 0;
        for (i=a;i<b;i++)
        {
            int tmp = i;
            v.clear();
            for (j=1;j<n;j++)
            {
                int tmp1 = tmp%10;
                tmp1 = tmp1*deg[n-1]+tmp/10;
                if (tmp1>i && tmp1<=b && v.find(tmp1)==v.end())
                   ans++;
                tmp = tmp1;
                v.insert(tmp);
            }
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    
}
