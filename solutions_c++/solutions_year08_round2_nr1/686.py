#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define FOR(i, x) for (int i = 0; i < x; i++)
#define FORI(i,a, x) for (int i = a; i < x; i++)
#define ALL(x) (x).begin(), (x).end()
#define FORE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())
 
using namespace std;



int main()
{
    freopen("A-small-attempt4.in","r",stdin);
    freopen("salida.out","w",stdout);    
    long long casos;
    cin>>casos;    
    FOR (cases,casos)
    {
        
        long long n, A, B, C, D, x0, y0, M;
        cin>>n>> A>> B>> C>> D>> x0>> y0>> M;
        vector< pair<long long,long long> > arreglo;
        long long X = x0, Y = y0,X1,Y1;
        
     
        arreglo.push_back(pair<long long,long long>(X,Y));
//        cout<<X1<<" "<<Y1<<endl;
        FORI (i,1,n)
        {
          X = (A * X + B) % M;
          Y = (C * Y + D) % M;      
//          cout<<X1<<" "<<Y1<<endl;
          bool flag=true;         
          if (flag)
             arreglo.push_back(pair<long long,long long>(X,Y));
        }
      //  cout<<SZ(arreglo);
        long long resp=0;
        FOR (i,SZ(arreglo))
        {
      //      cout<< arreglo[i].first<<" "<<arreglo[i].second<<endl;
            FORI (j,i+1,SZ(arreglo))
                 FORI (k,j+1,SZ(arreglo))
                      if ((arreglo[i].first+arreglo[j].first+arreglo[k].first)%3==0 && (arreglo[i].second+arreglo[j].second+arreglo[k].second)%3==0)
                          resp++;
        }

        cout<<"Case #"<<cases+1<<": "<<resp<<endl;
    }
    return 0;
}

