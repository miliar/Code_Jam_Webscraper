#include <fstream>
#include <set>
#include <map>
using namespace std;

int main(){
    ifstream in("a.in");
    ofstream out("a.out");
    
    int t, k=0, i, j;
    in>>t;
    string basura;
    getline (in, basura);
    
    while (k<t){
          k++;
          set <char> conj;
          map <char, int> m;
          conj.clear();
          m.clear();
          string s;
          getline (in, s);
          int x=s.length();
          
          for (i=0; i<x; i++)conj.insert(s[i]);
          int base=conj.size();
          if (base<2)base=2;
          //base++;
          
          long long int val[x];
          val[0]=1;
          m[s[0]]=1;
          i=1;
          int cont=2;
          while (i<x && s[i]==s[0]){val[i]=1; i++;}
          
          if (i<x){
          val[i]=0;
          m[s[i]]=0;
          i++;
          }
          
          
          while (i<x){
                if (m.count(s[i])!=0){
                   val[i]=m[s[i]];
                   }
                else {
                     val[i]=cont;
                     m[s[i]]=cont;
                     cont++;
                     }
                
                i++;
                }
          
          long long int res=0;
          long long int pot=1;
  //        for (i=0; i<x; i++)out<<val[i];
//          out<<endl;
          for (i=x-1; i>=0; i--){
    //          out<<res<<' ';
              res+=pot*val[i];
              pot*=base;
              }
          out<<"Case #"<<k<<": "<<res<<endl;
          
          }
    
    
    }
