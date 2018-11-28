#include<iostream>
#include <iomanip>
#include<vector>
#include<set>
#include<map>

using namespace std;
typedef vector<char> CharVec;
typedef vector<CharVec> CharVecVec;
typedef vector<long double> DblVec;

#define NP '.'
#define WON '1'
#define LOST '0'

int main()
{
    int T;
    cin >> T;
   
    for(int n =0; n<T; ++n)
    {
       int N;
       cin >> N;
       CharVecVec matrix;
       for(int i=0; i< N; ++i)
       {
               CharVec temp;
               for(int j=0; j< N; ++j)
               {
                   char c;
                   cin  >> c;
                   temp.push_back(c); 
               }
               matrix.push_back(temp); 
       }
       
       
       DblVec wpvec;
       DblVec playedvec;
       for(int i=0; i<N; ++i)
       {
          long double wp =0;
          long double played = 0;     
          for(int j=0; j< N; ++j)
          {
              if(matrix[i][j] == WON)
              {
                     wp++;         
              } 
              if(matrix[i][j] != NP)
              {
                     played++;         
              }   
          }
          wpvec.push_back(wp/played);
          playedvec.push_back(played);      
       }
       
       DblVec owpvec;
       for(int i=0; i<N;++i)
       {
          long double owp =0;    
          for(int j=0; j< N; ++j)
          {
              if(matrix[i][j] != NP)
              {
                    if(matrix[j][i]==WON)          
                       owp += (wpvec[j]*playedvec[j]-1)/(playedvec[j]-1);
                    else
                       owp += (wpvec[j]*playedvec[j])/(playedvec[j]-1);          
              }   
          }
          owpvec.push_back(owp/playedvec[i]);  
       }
       
       DblVec oowpvec;
       for(int i=0; i<N;++i)
       {
          long double oowp =0;    
          for(int j=0; j< N; ++j)
          {
              if(matrix[i][j] != NP)
              {
                  oowp += owpvec[j];            
              }
          }
          oowpvec.push_back(oowp/playedvec[i]);  
       }
       cout << "Case #" <<n+1<<":" <<"\n";
       for(int i=0; i<N;++i)      
       cout << 0.25 * wpvec[i] + 0.50 * owpvec[i] + 0.25 * oowpvec[i] <<"\n"; 
    }
    
}
