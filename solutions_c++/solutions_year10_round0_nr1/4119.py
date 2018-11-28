
#include <iostream> 
#include <fstream>
#include <math.h>

using namespace std; 
int main() 
{ 
int i,j;
  
  long long x,y,z;
   

 
 //----------------------------------
  ofstream out("d:\\output\\O2.txt"); 
  
  if(!out) { 
    cout << "error.\n"; 
   return 1; 
   } 
 

  ifstream in("d:\\A-large.in"); 
  if(!in) { 
    cout << "error.\n";  
    return 1; 
  } 
//----------------------------
  in >> i; 

for(j=0;j<i;j++){
             
             
             
                 in>>x;
                 in>>y;
                 
                 
                 out<<"Case #"<<j+1<<": ";
                 
                 
                 
                 
                 
                       z=y%(1ll<<x);
        
           if(z==(1ll<<(x))-1)
           
           
           
           
            {
                          out<<"ON\n";
            }
           
           
           
           
           
           
           
            else
            {
                out<<"OFF\n";
            }             
             
             
             
              }
                 
                 
                 
//           /-------------------  

cin>>i;

  in.close(); 
  return 0; 
}
