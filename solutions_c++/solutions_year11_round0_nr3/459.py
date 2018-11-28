#include <iostream> 
#include <fstream>
using namespace std; 

int main() { 
 int C[1000];
 int N;
 int tests;
 ifstream input("C-large.in");
 ofstream output("C-large.out");
 input >> tests;
 
 for (int j=0;j<tests;j++)
 {
     input >> N;
     for (int i=0;i<N;i++)
         input >> C[i];
     int total=0;
     for (int i=0;i<N;i++)
         total ^= C[i];
     if (total != 0)
     {
        output << "Case #" << (j+1) << ": NO\n";
        continue;    
     }
     int min=C[0];
     for (int i=0;i<N;i++)
     {
         total += C[i];
         if (C[i]<min)
            min=C[i];
     }
     
     
     output << "Case #" << (j+1) << ": " << (total-min) << "\n";
 }


 return 0; 
}
