#include <iostream>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,tci,tc,n,sum,min,now,sxor;
    cin >> tc;
    for (tci = 1;tci <= tc;++tci)
    {
        sum = sxor = 0;
        min = 999999999;
        cin >> n;
        for (i = 0;i < n;++i)
        {
            cin >> now;
            sum += now;
            sxor ^= now;
            if (min > now) min = now;
        }
        if (sxor != 0) cout << "Case #" << tci << ": NO" << endl;
        else cout << "Case #" << tci << ": " << (sum - min) << endl;
    }
    //system("pause");
    fclose(stdin);
    fclose(stdout);
    return 0;
}
