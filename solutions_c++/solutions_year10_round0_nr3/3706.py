#include <iostream>

#define uint unsigned long long int

using namespace std;
int g[1000];

int main()
{
    uint t, R, k, n, r, j, jo, resp;
    cin >> t;
    for(uint i=1; i<=t; i++)
    {
        cin >> R >> k >> n;
        resp=0;
        for(j=0; j<n; j++)
            cin >> g[j];
        j=0;
        for(uint m=0; m<R; m++)
        {
            for(r=0, jo=j; r<=k && ((jo%n)!=(j%n) || j==jo); r+=g[(j++)%n]);
            if(r>k)
            {
                j--;
                r-=g[j%n];
            }
            resp+=r;
        }
        cout << "Case #" << i << ": " << resp << endl;
    }
    return 0;
}
