#include <iostream> 
#include <fstream>
using namespace std; 

int main() { 
 int T,C,D,N,INV;
 string c[36];
 string d[28];
 string n;
 string inv;
 int tests;
 ifstream input("B-large.in");
 ofstream output("B-large.out");
 input >> tests;
 
 for (int j=0;j<tests;j++)
 {
     {
           input >> C;
           for (int i=0;i<C;i++)
               input >> c[i];
           input >> D;
           for (int i=0;i<D;i++)
               input >> d[i];
           input >> N;
           input >> n;
           
           inv.clear();
           for (int i=0;i<N;i++)
           {
               if (inv=="")
               {
                  inv=n[i];
                  i++;
               }
               if (i==N)
                  break;
               inv+=n[i];
               for (int k=0;k<C;k++)
               {
                   if( ((*(inv.end()-1)==c[k][0]) && (*(inv.end()-2)==c[k][1])) || ((*(inv.end()-1)==c[k][1]) && (*(inv.end()-2)==c[k][0]))   )
                   {
                    inv.erase(inv.end()-1);
                    *(inv.end()-1)=c[k][2];
                   }
               }
               for (int k=0;k<D;k++)
               {
                   if( *(inv.end()-1)==d[k][0] )
                   {
                       for (int l=0;l<(inv.length()-1);l++)
                       {
                           if (inv[l]==d[k][1])
                           {
                               inv.clear();
                               break;
                           }               
                       }
                   }
                   if( *(inv.end()-1)==d[k][1] )
                   {
                       for (int l=0;l<(inv.length()-1);l++)
                       {
                           if (inv[l]==d[k][0])
                           {
                               inv.clear();
                               break;
                           }               
                       }
                   }
                       
               }
           }
     }
     
 if(inv.length()==0)
 {
      output << "Case #" << (j+1) << ": []\n";
 }
 else
 {    
 output << "Case #" << (j+1) << ": [";
 for (int l=0;l<(inv.length()-1);l++)
 {
     output << inv[l] << ", ";
 }
 output << *(inv.end()-1) << "]\n"; 
 }
 }

 return 0; 
}
