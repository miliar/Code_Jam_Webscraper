#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    int t,it;
    int n,i,j;
    long long int lcm,res,l,h,a[10006],ok;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> t;
    for (it = 1;it <= t;++it)
    {
        res = 1;
        cin >> n >> l >> h;
        for (i = 0;i < n;++i) cin >> a[i];
        cout << "Case #" << it << ": ";
        for (i = l;i <= h;++i)
        {
            ok = 1;
            for (j = 0;j < n;++j)
                if ((i % a[j] != 0) && (a[j] % i != 0))
                {
                    ok = 0;
                    break;
                }
            if (ok)
            {
                cout << i << endl;
                break;
            }
        }
        if (ok == 0) cout << "NO" << endl;
    }
//    system("pause");
    fclose(stdin);
    fclose(stdout);
    return 0;
}
