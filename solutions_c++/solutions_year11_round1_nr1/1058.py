#include<cmath>
#include<iostream>
#include<string>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<map>

using namespace std;

int main()
{
    int t, count;
    cin >> t;
    count=0;
    long long n;
    double pd, pg=0;
    double wd,wg,td,tg;
    while (count<t)
    {
        count++;
        cout << "Case #" << count << ": ";
        cin >> n >> pd >> pg;
        wd=0; wg=1;
        if (n>100)
        {
            wd=pd; wg=100;
        }
        else
        {
        while (wg<n)
        {
            if (wd*100/wg==pd)
                break;
            else
            {
                if (wd*100/wg>pd)  wg++;
                if (wd*100/wg<pd)  wd++;                
            }
        }
        }
        if (wd*100/wg!=(double)pd)  
        {
            cout << "Broken" <<endl;
            continue;
        }
        else
        {
            td=0;tg=0;
            if (!((pd!=0 && pg==0)||(pd!=100 && pg==100)))
            {
            while (tg<n*100)
            {
                if ((wd+td)*100/(wg+tg)==pg)
                    break;                
                else
                {
                    if ((wd+td)*100/(wg+tg)>pg)  tg++;
                    if ((wd+td)*100/(wg+tg)<pg) { tg++;td++;}  
                }                
            }
            }
            if ((wd+td)*100/(wg+tg)==pg)
                cout << "Possible" << endl;
            else cout << "Broken" << endl;
        }

    }
    
}







