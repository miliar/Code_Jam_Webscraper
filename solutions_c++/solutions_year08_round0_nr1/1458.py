#include <iostream>
#include <string>

using namespace std;

int main(){
    int n,s,q,i,j,k;
    cin >> n;
//    cout << n << " casos" << endl;
    for(i = 0; i < n ; i++){
          cin >> s;
  //        cout << s << " engines"<< endl;
          string d;   
          getline(cin, d);
          string engine[s];
          int check[s];
          int count = 0;
          int sw= 0;
          for(j = 0; j < s ; j++) {
                getline(cin, engine[j]);
               // cout << "leyendo engine "<< engine[j]<< " \n";
          }
          for(j = 0; j < s ; j++) check[j]= 0;
          cin >> q;
          getline(cin, d);
    //      cout << q << " queries"<< endl;
          for(k = 0; k < q ; k++) {     
                string query;
                getline(cin,query);                
      //          cout << "leyendo query " << query << endl; 
                int aux;
                for(aux = 0; aux < s; aux++){
                        if (query.compare(engine[aux]) == 0){
                           if (check[aux] == 0){
                              check[aux]= 1;
                              count++;
                              //cout << "la cuenta es " << count <<" y s es "<< s << endl;
                              if (count == s){
                                // cout << "entro" << endl;       
                                 for(j = 0; j < s ; j++) check[j]= 0;
                                 check[aux] = 1;
                                 count = 1;
                                 sw++;
                              }
                              break;
                           } 
                        }
                }
          }
          cout << "Case #"<<(i+1)<<": "<<sw<< endl;
    }
    return 0;    
}
