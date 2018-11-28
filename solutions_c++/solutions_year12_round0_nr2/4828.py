#include<iostream>
#include<math.h>
#include<fstream>
using namespace std;
int main(){
   int T;
   cin>>T;
   for(int t=1;t<=T;t++){
           int n,s,p;
           cin>>n>>s>>p;
           int term,count=0;
           for(int i=0;i<n;i++){
                   cin>>term;
                   if(term<p) continue;
                   if((term/3)>=p) count++;
                   else if((term/3)==(p-1) && (term%3)>=1) count++;
                   else if((term/3)==(p-1) && s>0) { count++; s--; }
                   else if((term/3)==(p-2) && s>0 && (term%3)>=2) { count++; s--; }
           }
           cout<<"Case #"<<t<<": "<<count<<endl;
   }
   return 0;
}
