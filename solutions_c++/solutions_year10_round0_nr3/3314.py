#include<iostream>
using namespace std;
#define forn(i,n) for(int i = 0; i < n;i++)
int d[1500];
int re[1500];
int ga[1500];
main()
{
    int t;
    cin>>t;
    forn(kk,t)
    {
        long long r,k,n;
        cin>>r>>k>>n;
        forn(i,n)
        {
            cin>> d[i];
            re[i] = -1;
        }
        int aux = 0;
        long long time = 0;
        long long res = 0;
        while (re[aux%n] == -1 && r > 0)
        {
            re[aux%n] = time;
            ga[aux%n] = res;
            int cc= k;
            int cont = 0;
            while(cc >= d[aux%n] && cont < n)
            {
                res += d[aux%n];
                cc-= d[aux%n];
                aux++;
                cont++;
            }
            r--;
            time++;
        }

        long long dif =  res - ga[aux%n];
        long long dt = time - re[aux%n];
        if (dt > 0)
        {
         //   cout<<r<<" "<<dt<<" "<< dif<<endl;
            res += (r / dt) * dif;
            r = r %dt;
        }
        while (r > 0)
        {
            int cc= k;
            int cont = 0;
            while(cc >= d[aux%n]&& cont < n)
            {
                res += d[aux%n];
                cc-= d[aux%n];
                aux++;
                cont++;
            }
            r--;
        }

        cout<<"Case #"<< kk+1<<": "<<res<<endl;

    }
}
