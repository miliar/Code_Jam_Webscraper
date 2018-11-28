
#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>
#include<utility>
#include<set>
#include<map>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std ;

int main()
{
   int T ;
   long long N , A[1000] , B[1000];
   ofstream  fout("out2.txt") ;
   ifstream fin("A-large.in");
   int n = 0 ;
   fin >> T ;  
   
   while(T-->0){
   fin >> N ;             
   n++;             
   for(int i = 0 ; i < N ; ++i  ) 
      fin >> A[i] ;        
   for(int i = 0 ; i < N ; ++i  ) 
     fin >> B[i] ;
   
   sort(  A ,A+N  );
   sort(  B , B+N );
   
   long long temp = 0 ;
   for(int i = 0 ; i < N ; ++i  ) 
       temp += A[i] * B[N-1-i];
    
   fout<<"Case #" << n << ": " << temp << endl ;         
   }
   return 0 ;
}
