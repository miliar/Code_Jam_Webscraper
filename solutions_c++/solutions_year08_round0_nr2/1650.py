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
#define HP first.first.first
#define MP first.first.second
#define HA first.second.first
#define MA first.second.second
#define E second
#define TH pair< int ,int> 

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("salida.out","w",stdout);
    int casos;
    cin>>casos;
    FOR (cases,casos)
    {
        int time;
        int a,b,n,resp1=0,resp2=0;
        cin>>time>>a>>b;
        n=a+b;
        vector< pair < pair < TH,TH> , int >  > cola(a+b);
        vector< pair < TH , int > > cola2;
        string cadena;
        getline(cin,cadena);
        FOR (i,a)
        {
            int hora,minutos;
            string salida,llegada;
            getline(cin,cadena);
            istringstream flujo(cadena);
            flujo>>salida>>llegada;
            salida[2]=' '; 
            llegada[2]=' '; 
            istringstream flujo2(salida);
            flujo2>>hora>>minutos;            
            cola[i].HP=hora;
            cola[i].MP=minutos;
            istringstream flujo3(llegada);
            flujo3>>hora>>minutos;            
            cola[i].HA=hora;
            cola[i].MA=minutos;
            cola[i].E=0;            
        }
        for (int j=0,i=a;j<b;j++,i++)
        {
            int hora,minutos;
            string salida,llegada;
            getline(cin,cadena);
            istringstream flujo(cadena);
            flujo>>salida>>llegada;
            salida[2]=' '; 
            llegada[2]=' '; 
            istringstream flujo2(salida);
            flujo2>>hora>>minutos;            
            cola[i].HP=hora;
            cola[i].MP=minutos;
            istringstream flujo3(llegada);
            flujo3>>hora>>minutos;            
            cola[i].HA=hora;
            cola[i].MA=minutos;
            cola[i].E=1;            
        }
        sort(ALL(cola));        
        FOR (i,n)
        {
            bool flag=true;
            //revise cola
            FOR (j,SZ(cola2))
            {
                if (cola2[j].E==cola[i].E && (cola2[j].first.first*60+cola2[j].first.second)<=(cola[i].MP+cola[i].HP*60))
                {
                   flag=false;
                   cola2.erase(cola2.begin()+j);
                   break;
                }
            }
            //Pailas
            if (flag)
            {
                if (cola[i].E==0)
                   resp1++;
                else
                   resp2++;                
            }
            int hora1,hora2;            
            hora1=cola[i].HA;
            hora2=cola[i].MA;            
            hora2+=time;
            if (hora2>=60)
            {
                hora1++;
                hora2-=60;
            }                           
            cola2.push_back(pair < TH , int >(TH(hora1,hora2),(cola[i].second+1)%2));
        //    cout<<cola2[0].E<<" "<<cola2[0].first.first<<" "<<cola2[0].first.second<<endl;
        }
        cout<<"Case #"<<cases+1<<": "<<resp1<<" "<<resp2<<endl;
    }
    return 0;
}
