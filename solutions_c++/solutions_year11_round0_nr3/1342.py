#include <iostream>
using namespace std;
const int big=1000000000;
int g,mymin,n,sum,k;

int main()
{
    int z,zz,i;
    
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> z;
    for (zz=1;zz<=z;zz++)
    {
        cin >> n;
        mymin=big;g=0;sum=0;
        for (i=1;i<=n;i++)
        {
            cin >> k;
            sum+=k;
            g= (g ^ k);
            if (k<mymin) mymin=k;
        }
        cout << "Case #" << zz << ": ";
        if (g==0) cout << sum-mymin << endl;
        else cout << "NO" << endl;    
    }
}
