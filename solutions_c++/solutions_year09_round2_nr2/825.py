#include <fstream>
using namespace std;

int main(){
    ifstream in("b.in");
    ofstream out("b.out");
    int t, k=0, i, j, l;
    in>>t;
    int cant[10];
    
    while (k<t){
          string s;
          string res="";
          int aux=0;
          in>>s;
          int x=s.length();
          int mejor=10, mejind;
          for (i=x-1; i>=0 && aux==0; i--){
              for (j=x-1; j>i && aux==0; j--){
                  if (s[j]>s[i] && s[j]-'0'<mejor){
//                     out<<s[j]<<' ';
                     mejor=s[j]-'0';
                     mejind=j;
                     }
                  }
              if (mejor!=10){
                 swap(s[i], s[mejind]);
                 

                 for (j=0; j<10; j++)cant[j]=0;
                 res="";
                 for (j=0; j<=i; j++)res+=s[j];

             for (j=i+1; j<x; j++)cant[s[j]-'0']++;
             for (j=0; j<10; j++){
                 for (l=0; l<cant[j]; l++)res+=j+'0';
                 }


                 
                 out<<"Case #"<<k+1<<": "<<res<<endl;
                 aux=1;
                 }
              }
          
          for (i=0; i<10; i++)cant[i]=0;
          if (aux!=1){
             for (i=0; i<x; i++)cant[s[i]-'0']++;
             i=1;
             while (cant[i]==0)i++;
             res+=i+'0';
             res+='0';
             cant[i]--;
             for (i=0; i<10; i++){
                 for (j=0; j<cant[i]; j++)res+=i+'0';
                 }
                 out<<"Case #"<<k+1<<": "<<res<<endl;

             }
          
          
          
          
          k++;
          }
    
    
    
    }
