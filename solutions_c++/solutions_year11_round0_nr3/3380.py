#include <cstdlib>
#include <iostream>
#include <fstream>
using namespace std;
int num[1000][20];
int no[1000];
int L;
int Max= -1;


void solve(int pos, int B1C, int B1F [], int B2C , int B2F[])
{
     if(pos == L)
     {
            bool equal = true;
            for(int i=0; i< 20; i++)
                    if(B1F[i] != B2F[i])
                              {
                                        equal = false;
                                        break;
                              }
            if(equal && (B2C!= 0))
             {
                     if((B1C >= B2C) && (B1C > Max)) Max = B1C;                        
             }
     }
     else
      {
             int temp1[20], temp2[20];
             for(int i=0; i< 20; i++)
             {
                     temp1[i] = (B1F[i]+num[pos][i]) % 2;
                     temp2[i] = (B2F[i]+num[pos][i]) % 2;
             }
             solve(pos+1, B1C+no[pos], temp1, B2C, B2F);
             
             solve(pos+1, B1C, B1F, B2C+no[pos], temp2);
            
      }     
}


int main(int argc, char *argv[])
{
   ifstream cin("Test.txt");
    ofstream cout("Output.txt");
    
    int TestNum;
    cin >> TestNum;
    
    for(int j = 0; j < TestNum; j++)
    {
       Max= -1;
       int k;
       cin >> L; 
       for(int n=0; n<L; n++)
                       for(int m=0; m<20; m++)
                               num[n][m] = 0; 
       for(int i=0; i< L; i++)
       {
               
               cin >> no[i];
               k = no[i];
               int w = 524288, p = 19; 
               while(k != 0)
               {
                         if(k >= w)
                         {
                                k -= w;
                                num[i][p] = 1;                              
                         }  
                         w = w/2;
                         p--;                                                    
               }
       }
       
       int f1[20]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};  
       int f2[20]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};  
       solve(0, 0, f1, 0, f2);
       if(Max == -1)
              cout << "Case #"<< j+1 << ": NO" << endl;
       else  
             cout << "Case #"<< j+1 << ": " << Max << endl;
    }
  /*  for(int n=0; n<L; n++)
                      { for(int m=0; m<20; m++)
                               cout << num[n][m] ;cout << endl;}
  */  
    system("PAUSE");
    return EXIT_SUCCESS;
}
