#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

int t, n, s, p, a[200], tot;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> t;
    for (int w = 1; w <= t;++w)
    {
        tot = 0;
        cout << "Case #" << w << ": ";
        cin >> n >> s >> p;
        for (int i = 0; i < n;++i) cin >> a[i];
        sort(a,a+n);
        for (int i = 0;i < n;++i)
        {
        //    cout << a[i] << ' ';
            if (a[i] >= 2 && s)
            {
                if ((a[i]-2)/3+2 >= p)
                { ++tot;
                --s;}

            }
            else {
                    if (a[i] > 0 && (a[i]-1)/3+1 >= p) ++tot;
                    else if (p == 0) tot++;
                 }}
        cout << tot << endl;
    }
    return 0;
}
