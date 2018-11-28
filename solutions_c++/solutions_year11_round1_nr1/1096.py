#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;
int main()
{
        freopen("A-large.in","r",stdin);
        freopen("cpout1.txt","w",stdout);
        long long t,tt,N,i,j,k;
        double ans1, ans2, Pd, Pg, ans3;
        cin >> tt;
        for(t=1 ; t<=tt ; t++)
        {
                cin >> N >> Pd >> Pg;
                if((Pd>0 && Pg==0) || (Pd==0 && Pg==100)||(Pg==100 && Pd<Pg))
                {
                    cout << "Case #" << t << ": " << "Broken" << endl;
                    continue;
                }
                for(int i=1;i<=N;i++)
                {
                    ans1 = (Pd/100)*i;
                    ans3 = modf(ans1,&ans2);
                    if(ans3!=0)
                    {
                        if(i==N)
                            cout << "Case #" << t << ": " << "Broken" << endl;
                    }
                    else
                    {
                        cout << "Case #" << t << ": " << "Possible" << endl;
                        break;
                    }
                }
        }
        return 0;
}
