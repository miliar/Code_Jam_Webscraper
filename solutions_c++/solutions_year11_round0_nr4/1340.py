#include <iostream>
#include <iomanip>
using namespace std;
double g;

int main()
{
    int z,i,zz,n,k;
    
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> z;
    for (zz=1;zz<=z;zz++)
    {
        cin >> n;
        g=0;
        for (i=1;i<=n;i++)
        {
            cin >> k;
            if (k!=i) g+=1;
        }
        cout << "Case #" << zz << ": ";
        cout << setiosflags(ios::fixed) << setprecision(6) << g << endl;    
    }
}
