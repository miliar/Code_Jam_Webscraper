
#include <iostream> 
#include <fstream>
#include <math.h>
int res[100000]; 
using namespace std; 
 void aaa(int i){
int j;
  ofstream out("d:\\a.txt"); 
  
  if(!out) { 
    cout << "Cannot open file.\n"; 

   } 
 
 
 for(j=0;j<i;j++){
//  out<<res[j]<<endl;
    out <<"Case #"<<j+1<<": ";
  
  if(res[j]==0) out<<"OFF\n";
  
                else out<<"ON\n";
  
}
  out.close();     
      }
int main() 
{ 

  char ch; 
  int a,b;
  int i,j; 
  float f; 


  ifstream in("d:\\A-small-attempt0.in"); 
  if(!in) { 
    cout << "Cannot open file.\n";  
    return 1; 
  } 
 
  in >> i; 

for(j=0;j<i;j++){
                 in>>a;
                 in>>b;
                 f=(b+1)/pow(2,a);
                 
              if(((f-(int)f)*10)!=0) {
              
                      res[j]=0; cout<<"no\n";}
              else {res[j]=1;cout<<"yes\n";
              
              }
                 
                 
                 
                 }

 aaa(i);
  cout << i << " " << f << " " << ch << endl; 
cin>>f;

  in.close(); 
  return 0; 
}
