#include<iostream>
#include<fstream>
#include<sstream>
#include<cstring>
#include<vector>
#include<utility>
#include<cmath>

//#include<>
using namespace std;

#define for_n(i,n) for( (i)=0;(i)<(n);(i)++)
#define lli long long int
#define ulli unsigned long long int

int main()
{
    int T;
    ifstream fin("in.txt");
    ofstream fout("out2.txt");
    fin>>T;int t;
    for_n(t,T)
    {
              int R,C;int flag=0;int i,j;
              fin>>R>>C;
              int** A = new int*[R];
              for_n(i,R) A[i]=new int[C];
              i=0;j=0;
              for_n(i,R)
              {
                        for_n( j,C)
                        {
                                  char d;
                                  fin>>d;
                                  if(d=='#')
                                  A[i][j]=1;
                                  if(d=='.')A[i][j]=0;
                        } 
              }
              i=0;j=0;
              for_n( i ,R){
                        for_n( j,C)
                        {
                                  if(j!= (C-1) && i!=(R-1) && A[i][j]==1 && A[i][j+1]==1 && A[i+1][j] == 1 && A[i+1][j+1] == 1)
                                  {
                                               A[i][j]=2 ; A[i][j+1]=3 ; A[i+1][j] = 3 ; A[i+1][j+1] = 2;
                                  }
                        }
              }
              i=0;j=0;
              for_n( i,R)
              {
                        for_n( j,C)
                        {
                                  if(A[i][j]== 1){ flag=1;break;}
                        }
              }
              
              if(flag==1)
              {
                         cout<<"Case #"<<t+1<<":\nImpossible\n";
                         fout<<"Case #"<<t+1<<":\nImpossible\n";
              }
              else
              {
                      cout<<"Case #"<<t+1<<":\n";
                      fout<<"Case #"<<t+1<<":\n";
                       for_n( i,R)
                        {
                        for_n( j,C)
                        {
                                 if(A[i][j]==0){cout<<".";fout<<".";}
                                 if(A[i][j]==2){cout<<"/";fout<<"/";}
                                 if(A[i][j]==3){cout<<"\\";fout<<"\\";}
                                 
                        }
                        cout<<"\n";
                        fout<<"\n";
                        }
                        
              }
              
    }
                       
                         
                                                                                          
                                                       
   
    int y;cin>>y;
    return 0;
}
