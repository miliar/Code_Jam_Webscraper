#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#define cin ccin
#define cout ccout
std::ifstream cciinn ("A-large.in");
std::ofstream ccoouutt ("A.txt");
using namespace std;
bool tel (string b, string a){
   bool obert=false;
   int pos=0;
   for (int i=0; i<b.size(); i++){
      if (b[i]==char(40)) obert=true;
      if (b[i]==char(41)){ obert=false; pos++;}
      else {
           if (obert==false and b[i]>='a' and b[i]<='z'){
              if (b[i]!=a[pos]) return false;
              pos++;
           }
           if (obert==true){
              bool ok=false;
              int ku;
              for (ku=i; b[ku]!=char(41); ku++) if (b[ku]==a[pos]) ok=true; 
              if (!ok) return false; 
              i=ku-1;
           }
      }
   }
   return true;     
}
int main (){
    int l,d,n;
    cciinn >>l>>d>>n;
    vector <string> ma;
    while (d--){
          string a;
          cciinn >>a;
          ma.push_back(a);
    }
    for (int i=0; i<n; i++){
       string b;
       cciinn >>b;
       int no=ma.size();
       int pos=0;
       for (int ju=0; ju<ma.size(); ju++){
         if (!tel(b,ma[ju])) no--;
       }
       ccoouutt <<"Case #"<<i+1<<": "<<no<<endl;
     
    }
}
