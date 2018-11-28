#include <cstdlib>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main(int argc, char *argv[])
{   
    
     
   
    int i;
    ifstream  in(argv[1],ios::in| ios::binary);
    if(!in)
	     {
		 cout<<"cannot open file";
	     return 1;
         }
    ofstream  out(argv[2],ios::out| ios::binary);
    int t;
    
    
    in>>t;//cout<<"test cases---------->"<<t<<endl;;
    int cases=0;
    while(cases<t)
          {   
              int n;
              float mat[100][105];
              in>>n;cout<<"no of teams"<<n;
              for(int i=0;i<n;i++)
              {
                      int w=0;int l=0;
              for(int j=0;j<n;j++)
                  {
                      char ch;
                      in>>ch;
                      while((ch!='.')&&(ch!='1')&&(ch!='0'))in>>ch;
                      if(ch=='.')mat[i][j]=99;
                      if(ch=='1'){mat[i][j]=1;w++;}
                      if(ch=='0'){mat[i][j]=0;l++;}
                  }
                  mat[i][100]=w;//cout<<"wins"<<w<<endl;
                  mat[i][101]=l;//cout<<"loss"<<l<<endl;
                  mat[i][102]=w*1.0/(w+l);cout<<"wp"<<mat[i][102]<<endl;;
              
              }
              
              /* for(int i=0;i<n;i++) 
                {for(int j=0;j<n;j++)cout<<" "<<mat[i][j]<<" ";cout<<endl;}*/
               for(int i=0;i<n;i++)
                   {
                       float owp=0;int div=0;
                       for(int j=0;j<n;j++)
                        {
                              if(mat[i][j]==1)
                               {
                                       
                                  owp=owp+ (mat[j][100])/( mat[j][100]+mat[j][101] -1);div++; 
                              // cout<<j+1<<"ccccccccccccccchhl"<<owp<<endl;                     
                               }
                              if(mat[i][j]==0)
                               {
                                  owp=owp+ (mat[j][100]-1)/(mat[j][100]+ mat[j][101] -1);div++; 
                             //  cout<<j+1<<"ccccccccccccccchhl"<<owp<<endl;                          
                               }
                               
                        }
                        owp=owp/div;
                        mat[i][103]=owp;cout<<mat[i][103]<<endl;
                   }
                   
               for(int i=0;i<n;i++)
                   {
                       float oowp=0;int div=0;
                       for(int j=0;j<n;j++)
                        {
                              if((mat[i][j]==1)||(mat[i][j]==0))
                               {
                                  oowp=oowp+mat[j][103];
                                  div++;                        
                               }
                        
                        }
                        oowp=oowp/div;
                        mat[i][104]=oowp;cout<<mat[i][104]<<endl;
                   }
          
          
          cout<<"Case #"<<cases+1<<":"<<endl;
          for(int i=0;i<n;i++){
                  float rip;
                  rip=0.25 * mat[i][102] + 0.50 * mat[i][103] + 0.25 * mat[i][104];
          cout<<rip<<endl;  
          
          }
          cases++; 
          }

    
    return 1;
    
}
