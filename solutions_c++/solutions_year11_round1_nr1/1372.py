
#include <iostream>
#include <vector>
#include <list>
#include <map>


using namespace std;
//~ for(int i = 0; i < n; ++i)
int main()
{
    int t;
    cin >> t;
    for(int i =0 ; i < t; ++i)
    {
        int n, d, g;
        cin >> n >> d >> g;
        bool flag_hoy = false;
        bool res = false;
        for(int hoy =1 ; hoy <= n; ++hoy)
        {
            for(int ganados_hoy = 0; ganados_hoy <= hoy; ++ganados_hoy)
            {
                flag_hoy = flag_hoy || (ganados_hoy * 100) == hoy * d;
            }
        }
        if(flag_hoy)
        {
            if(g!=100 && g!=0)
            {
                res = true;
            }
            else
            {
                if(g == 0 && d == 0)
                {
                    res = true;
                }
                if(g==100 && d == 100)
                {
                    res = true;
                }
            }
        }
        if(res)
        {
            cout << "Case #" << i + 1 << ": Possible" << endl;
        }
        else
        {
            cout << "Case #" << i + 1 << ": Broken" << endl;
        }
    }
    return 0;
}
