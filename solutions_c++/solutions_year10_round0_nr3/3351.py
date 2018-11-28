#include <iostream>
#include <vector>
#include <fstream>


using namespace std;

ifstream fin("C-small-attempt0.in");
ofstream fout("3.out");

long long int problem3(int R, int k, vector<int> &g) {
                 
         long long int ret=0;        
         
         int i = 0;  
         int c = 0;
         int vuelta=0;
           
         while(R>0) {
           
                   if(c+g[i]<=k && vuelta<g.size() ){
                                 ret+=g[i];
                                 c+=g[i];
                                 if(i+1<g.size()) i++;
                                 else i=0;
                                 vuelta++;                   
                   }        

                  else {
                       R--;
                       c=0;
                       vuelta=0;
                       }  
         }
       
         return ret;
}


int main() {
    
    int C;
    fin >> C;
    
    for(int i=0;i<C;i++) {
    
            int R;
            fin >> R;
            int k;
            fin >> k;
            int gt;
            fin >> gt;
            
            vector<int> g(gt);
                        
            for(int j=0;j<gt;j++) 
                    fin >> g[j];
           
            fout<<"Case #" << i+1 << ": " << problem3(R,k,g)<<endl;        
    }
    
    system("pause");
}
