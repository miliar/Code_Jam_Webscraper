
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <functional>
#include <sstream>
#include <iostream>
#include <ctime>
#include <algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define _foreach(it, b, e) for(__typeof__(b) it = (b); it != (e); ++it)
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll; // sao dois L's!!!
const double eps = 1e-9;



long long val[1111];
long long parcial[1111];
int foi[1111];
int main ()
{
        int tt;
        scanf("%d",&tt);
        for(int pp=1;pp<=tt;pp++)
        {

            int r,k,n;
            scanf("%d %d %d",&r,&k,&n);
            for(int i=0;i<n;i++)
              {
                   scanf("%lld",&val[i]);
                    foi[i]=0;
              }




            int pos=0;
            int qte=1;
            long long sum=0;

            for(int i=0;i<n;i++)
            {
                sum+=val[i];
            }

            if(sum<=k)
            {
                    cout << "Case #" << pp <<": "<<sum*r<<endl;
            }
            else
            {
                sum=0;
                pos=0;
                while(foi[pos]==0)
                {
                    foi[pos]=qte;
                    long long aux=0;
                    while(aux<=k)//verificar loop
                    {
                            aux+=val[pos];
                            pos=(pos+1)%n;
                    }
                    pos=(pos+n-1)%n;
                    aux-=val[pos];
                    sum+=aux;
                    parcial[qte++]=sum;
                    //cout << parcial[qte-1] << endl;

                }
               // printf("%d\n",qte);
                if(qte>r)
                    cout << "Case #"<< pp<<": "<<parcial[r]<<endl;
                else
                {

                    int gaga=foi[pos];
                    long long ret=0;
                    int x = (r-gaga)/(qte-gaga);
                    int y = (r-gaga)%(qte-gaga);
                   // cout<<parcial[gaga-1]<<" "<<x*(parcial[qte-1]-parcial[gaga-1]);
                    ret=parcial[gaga-1] + x*(parcial[qte-1]-parcial[gaga-1])+parcial[gaga+y]-parcial[gaga-1];
                    cout << "Case #"<< pp<<": "<<ret<<endl;
                }
            }
        }
    return 0;
}
