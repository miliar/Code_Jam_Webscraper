#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

int main()
{
    ifstream cin("Text Messaging Outrage-A-large.in");
    ofstream cout("Text Messaging Outrage-A-large.out");
    int test_cases,p,k,l,aux;
    long long pos;
    long long result;
    cin>>test_cases;
    
    for(int i=1;i<=test_cases;i++)
    {
        result=0;
         cin>>p>>k>>l;
         long long vector[l];
         for(int j=0;j<l;j++)
         cin>>vector[j];
         
         sort(vector,vector+l);
         
         pos=1;
         aux=k;
         for(int j=l-1;j>=0;j--)
         {
          
          result+=vector[j]*pos; 
          aux--;
          if(aux==0)
          {
          pos++;
          aux=k;      
          }
           
         }
       
         
         cout<<"Case #"<<i<<": "<<result<<endl;  
       
    }
    

    
    return EXIT_SUCCESS;
}
