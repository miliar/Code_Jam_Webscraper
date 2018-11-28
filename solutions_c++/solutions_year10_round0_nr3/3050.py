#include <iostream>
#include <queue>

using namespace std;

main(){
       int T,R,k,N,x=0;
       cin>>T;
       while (T--){
             x++;      
             queue<int> cola;
             int tot=0;
             cin>>R>>k>>N;
             for (int i=0; i<N;i++){
                 int c;
                 cin>>c;
                 cola.push(c);
             }
             for (int i=0; i<R;i++){
                 int eur=0; 
                 int r=0;   
                 while(((eur+cola.front())<=k) and(r<N)){
                          r++;
                          eur=eur+cola.front();
                          cola.push(cola.front());
                          cola.pop();
                 }   
                 tot=tot+eur;                              
             }
             cout<< "Case #" << x << ": "<<tot<<endl;
       }  
}
