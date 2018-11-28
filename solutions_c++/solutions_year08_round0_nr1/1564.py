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

int m[128][1024];
vs engines;
map<string,int> number;
vi queries;
int cant=0;

  int mini(int a,int b) {
    cant++;
    if (m[a][b]!=4000) return m[a][b];
    int k;
    for(k=b;k<sz(queries) && queries[k]!=a;k++);
    if (k==b) {m[a][b]=5000;return 5000;} //5000 es infinito, 4000 es no calculado
    if (k==sz(queries)) {m[a][b]=0;return 0;}
    int mm=5000;
    forn(i,sz(engines)) mm=min(mm,mini(i,k));
    m[a][b]=1+mm;
    return 1+mm;

  }


int main () {
	freopen("entrada.in","r",stdin);
	freopen("salida.txt","w",stdout);

  int n,s,q;    string aux;

  
  cin>>n; // cout<<"N "<<n<<endl;
  forn(kk,n) {

        engines.clear();
        queries.clear();
        number.clear();
  
    cin>>s;   //   cout<<"S "<<s<<endl;
    getline(cin,aux); //parche
    forn(jj,s) {
      getline(cin,aux); // cout<<"aux "<<aux<<endl;
      engines.pb(aux);
      number[aux]=jj;
    }

    cin>>q;  ///cout<<"Q?"<<q<<endl;
    getline(cin,aux);
    forn(pp,q) {
      getline(cin,aux);      //cout<<"//"<<aux<<endl;
      queries.pb(number[aux]);
    }

   forn(i,128) forn(j,1024) m[i][j]=4000;

   int menor=5000;
   forn(i,sz(engines)) menor=min(menor,mini(i,0));
   if (q==0) menor=0;
   
   cout<<"Case #"<<kk+1<<": "<<menor<<endl;
  //forn(i,sz(engines)) cout<<"MENOR("<<i<<",0)= "<<mini(i,0)<<endl;
  //TENGO QUE ESCRIBIR EL MENOR DE TODOS ESTOS mini

    /*     cout<<"*****ENGINES*****"<<endl;
  forall(i,engines) cout<<*i<<endl;
  cout<<"*****QUERIES*****"<<endl;
  forall(i,queries) cout<<*i<<endl;  */

   //cout<<"CANTIDAD DE LLAMADAS: "<<cant<<endl;
  }


  
  return 0;

}


