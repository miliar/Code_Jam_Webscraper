#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <string>
#include <queue>
using namespace std;
#define forn(i,n) for(int i = 0 ; i < (int) (n) ; i ++)
#define pb push_back
pair<int,int> tocado[2][1100000];
main()
{
    #ifdef ACMTUYO
        freopen("a.in","r",stdin);
    #endif
    int cc;
     int MAX = 1<<30;
    cin >>cc;
    forn(i,2)
         {

             forn(j,1100000){
                tocado[i][j] = *new pair<int,int>(-MAX,0);
                tocado[i][j] = *new pair<int,int>(-MAX,0);
             }
         }
    forn(kk,cc)
    {
        vector<int> aa;

        int n;
        cin>>n;

        int maxx = 0;
        int no = 0;
        int total = 0;
        forn(i,n)
        {
            int aux = 0;
            cin >>aux;
            aa.pb(aux);
            total += aux;
            no = no ^ aux;

        }
        if (no != 0)
        {
            cout<<"Case #"<<kk+1<<": NO"<<endl;
            continue;
        }

        forn(j,1100000)
        {
                tocado[1][j].first = -MAX;
                tocado[0][j].first = -MAX;
             }

        //cout<<"aa";

        int res = -MAX;
        queue<int> cola[n+1];
        cola[0].push(0);
        tocado[0][0] = *new pair<int,int>(0,0);
        forn(i,n)
        {
           // cout<<i<<endl;
            int nu = aa[i];
            int j = (i+1) %2;
            while(!cola[i].empty())
            {
                int aux = cola[i].front();
                cola[i].pop();
                int sump = aux ^ nu;
               // cout<<aux<< " "<< nu <<" "<<sump<< " " << tocado[i%2][aux].first <<endl;
                if (tocado[j][sump].first < tocado[i%2][aux].first + nu)
                {
                    if (tocado[j][sump].first == -MAX)
                        cola[i+1].push(sump);
                    tocado[j][sump].first = tocado[i%2][aux].first + nu;
                    tocado[j][sump].second = tocado[i%2][aux].second;
                }/**/
            //    cout<<tocado[j][aux].first<< " " << tocado[i%2][aux].first-nu<<endl;
                if(tocado[j][aux].first < tocado[i%2][aux].first-nu)
                {
                    if (tocado[j][aux].first == -MAX)
                        cola[i+1].push(aux);
                    tocado[j][aux].first = tocado[i%2][aux].first;
                    tocado[j][aux].second = tocado[i%2][aux].second ^ nu;
                }
                tocado[i%2][aux].first = -MAX;
                tocado[i%2][aux].second = -1;
            }

        }

        forn(j,1100000){
                if (tocado[n%2][j].second ==  j && res < tocado[n%2][j].first && tocado[n%2][j].first != total)
                    res = tocado[n%2][j].first;

             }
        if (res == -MAX)
        {
            cout<<"Case #"<<kk+1<<": NO"<<endl;
            continue;
        }
        cout<<"Case #"<<kk+1<<": "<<res<<endl;


    }

}
