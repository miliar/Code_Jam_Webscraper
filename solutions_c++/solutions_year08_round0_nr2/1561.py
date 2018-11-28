#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef set<int> se;
typedef pair<int,int> pii;
typedef long long int tint;

#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define all(c) (c).begin(), (c).end()
#define D(a) << #a << "=" << a << " "


#define sz(a) int((a).size())
#define pb push_back
#define fi first
#define sec second



int main () {
  freopen("entrada.in","r",stdin);
  freopen("salida.txt","w",stdout);

  int n;
  int t,na,nb;
  int resa,resb;
  string aux,ss,ww;
  vector<pii> froma,fromb;
  vi toa,tob;
  int ina,inb;
  
  cin>>n;
  
  forn(kk,n) {
    cin>>t>>na>>nb;
    froma.clear();fromb.clear();toa.clear();tob.clear();
    resa=0;resb=0;ina=0;inb=0;
    
    //cout<<"T "<<t<<" NA "<<na<<" NB "<<nb<<endl;
    getline(cin,aux);
    forn(i,na) {
      getline(cin,aux);
      int hora=(aux[1]-'0')+10*(aux[0]-'0');
      int min=(aux[4]-'0')+10*(aux[3]-'0');
      int hh=hora*60+min;
        // cout<<hora<<" "<<min<<endl;
      hora=(aux[7]-'0')+10*(aux[6]-'0');
      min=(aux[10]-'0')+10*(aux[9]-'0');
      int hh2=hora*60+min;
        //cout<<hora<<" "<<min<<endl;

      froma.pb(make_pair(hh,hh2));
    }

    forn(i,nb) {
      getline(cin,aux);
      int hora=(aux[1]-'0')+10*(aux[0]-'0');
      int min=(aux[4]-'0')+10*(aux[3]-'0');
      int hh=hora*60+min;
         //cout<<hora<<" "<<min<<endl;
      hora=(aux[7]-'0')+10*(aux[6]-'0');
      min=(aux[10]-'0')+10*(aux[9]-'0');
      int hh2=hora*60+min;
        //cout<<hora<<" "<<min<<endl;
      fromb.pb(make_pair(hh,hh2));
    }
    //getline(cin,aux);
    /*forn(i,sz(froma)) cout<<froma[i].fi<<" "<<froma[i].sec<<endl;
    forn(i,sz(fromb)) cout<<fromb[i].fi<<" "<<fromb[i].sec<<endl;*/

    for(int time=0;time<=1439;time++) {
      //ACTUALIZAR
      forn(i,sz(toa)) if (toa[i]==time) {
        ina++;
        toa.erase(toa.begin()+i);
        i--;
      }
      forn(i,sz(tob)) if (tob[i]==time) {
        inb++;
        tob.erase(tob.begin()+i);
        i--;
      }
      //ACTUALIZADO

      //SALIDAS
      int cant=0;
      forn(i,sz(froma)) if (froma[i].fi==time) {
        tob.pb(froma[i].sec+t);
        cant++;
        froma.erase(froma.begin()+i);
        i--;
      }
      if (ina>=cant) ina-=cant;
      else {resa+=cant-ina;ina=0;}

      cant=0;
      forn(i,sz(fromb)) if (fromb[i].fi==time) {
        toa.pb(fromb[i].sec+t);
        cant++;
        fromb.erase(fromb.begin()+i);
        i--;
      }
      if (inb>=cant) inb-=cant;
      else {resb+=cant-inb;inb=0;}
      //LISTO SALIDAS
      
    }

    cout<<"Case #"<<kk+1<<": "<<resa<<" "<<resb<<endl;

  }

  return 0;

}


