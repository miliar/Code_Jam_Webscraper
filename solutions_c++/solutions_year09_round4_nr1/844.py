#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>

#define MAXN 100000
#define forn(i, n) for (i=0; i<n; i++)

using namespace std;

int tab[64][64];
int c[64];
int num[64];
vector <int>v;
vector <vector<int> >vv;
int main(){
    ifstream in("a.in");
    ofstream out("a.out");
    int t, k=0, i, j, pp, n;
    char cc;
    in>>t;
    while (k<t){
          v.clear();
          vv.clear();
          int res=0;
          k++;
          in>>n;
          forn(i, n){
          v.clear();
          forn(j, n){
                  in>>cc;
                  pp=cc-'0';
                  v.push_back(pp);
          }
          vv.push_back(v);
          }
          //out<<"pepe"<<endl;
          int f, cant;
          forn(i, 50)num[i]=0;
          
          for (f=n-1; f>=0; f--){
              cant=n-1;
//              out<<vv[f][cant];
              while (cant>=0 && vv[f][cant]==0){cant--;}
  //            out<<cant<<endl;
              c[f]=cant;
              for(i=0; i<cant; i++)num[i]++;
              }
         // out<<"pepe"<<endl;
          
          f=0;
          //forn(i, n)out<<num[i]<<endl;
          //out<<endl;
          //forn(i, n)out<<c[i]<<endl;
          while (f<n){
                if (c[f]>f){
//                   out<<"SI"<<endl;
                   i=f;
                   while (c[i]>f)i++;
                   for(i=i; i>f; i--){
                   swap (vv[i], vv[i-1]);
                   swap (c[i], c[i-1]);
                   res++;
                   }
                   }
                else {
  //                 out<<"NO"<<endl;
                     //for (i=n-1; i>c[f]; i--)num[i]--;
                     }
                
                f++;
                }
          
          
          out<<"Case #"<<k<<": "<<res<<endl;
          }
    
    
    
    
    }
