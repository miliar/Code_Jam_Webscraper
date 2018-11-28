#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

int main(){

    ifstream in("A-large.in");
    ofstream out("A-large.out");
    int l, d, n, cont=0;
    in>>l>>d>>n;
//    cout<<l<<' '<<d<<' '<<n<<endl;
    int pep;
  //  cin>>pep;
    vector <string>v;
    vector <int>r;
    string s;
    int i, j, k, ll;
    
    for (i=0; i<d; i++){
        in>>s;
        v.push_back(s);
        r.push_back(1);
        }
    
    k=0;
    
  
    while (k<n){
          cont=0;
          //cout<<"K "<<k<<endl;
          //cin>>pep;
          for (i=0; i<r.size(); i++)r[i]=1;
          
          out<<"Case #"<<k+1<<": ";
          in>>s;
          i=0;
          
          while (i<s.size()){
            //    cout<<"I "<<i<<endl;
              //  cin>>pep;
                if (s[i]!='('){
                               
                   for (j=0; j<v.size(); j++){

                       if (v[j][cont]!=s[i]){r[j]=0;}
                       }
                   i++;
                   }
                else {
                     for (j=0; j<v.size(); j++){
                         if (r[j]==1){
                            r[j]=0;
                            for (ll=i+1; s[ll]!=')'; ll++){
                                if (v[j][cont]==s[ll]){r[j]=1;}
                                }
                            }
                         }
                     while (s[i]!=')')i++;
                     i++;
                     }
                cont++;
                }
          
          int res=0;
          
          for (i=0; i<r.size(); i++){
              res+=r[i];
              }
          
          out<<res<<endl;
          
          k++;
          }
  
    }

