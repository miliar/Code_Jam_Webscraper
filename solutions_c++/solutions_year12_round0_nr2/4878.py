/* B. Dancing With the Googlers [filename: B_small.cpp]

           Codejam :: Qualification Round 2012
          ---------------------------------------------

                      Written in C++ Programming
       Tested and Compiled - Microsoft Windows 7 / Dev-C++ v4.9

*/

/******************************************************
           WRITTEN BY K21G [K-piXjuv-G]
           
         [ nepal.mountpk@msdnnepal.net ]
               [ puncoz@live.com ]
       [ http://www.facebook.com/puncoz ]
*******************************************************/

#include<iostream>
#include<cstdio>

using namespace std;

int main()
 {
  freopen("input.in","r",stdin);
  freopen("output.out","w",stdout);
  
  int T;
  cin>>T;
  
  for(int i=0; i<T; i++)
   {
    int N,S,p;
    cin>>N>>S>>p;   
    
    int t[N+1];
    for(int j=0; j<N; j++)
     {
      cin>>t[j];    
     }
    
     int A[N+1],B[N+1],C[N+1];  
    for(int j=0; j<N; j++)
     {
      int rough;
      if(t[j]<3)
       rough=0;
      else
       rough=t[j]/3;
       
      A[j] = B[j] = C[j] = rough;
      
      int sum = A[j] + B[j] + C[j];
      
       int a,b,c;
       a = 0;
      while(sum != t[j])
       {
        if( a==0 )
         {
          A[j]++;
          a++; 
         }
        else 
         {
          B[j]++; 
         }
        sum = A[j] + B[j] + C[j];   
       }  
     }
     
    int sur = 0;
    int flag = 0;
    while(sur != S)
     {
      for(int j=0; j<N; j++)
       {
        if( A[j]>=(p-1) || B[j]>=(p-1) || C[j]>=(p-1) )
         {
          if(flag==0 && A[j]==B[j] && A[j]!=C[j] && A[j]<10 && A[j]>0)
           {
            A[j]++;
            B[j]--;
            sur++;
            break;    
           }
          else if(flag==1 && A[j]==B[j] && A[j]==C[j] && A[j]<10 && A[j]>0 )
           {
            A[j]++;
            B[j]--;
            sur++;
            break;   
           } 
          else if(flag==2 && A[j]==C[j] && A[j]!=B[j] && A[j]<10 && A[j]>0)
           {
            A[j]++;
            C[j]--;
            sur++;
            break;    
           }
          else if(flag==3 && B[j]==C[j] && A[j]!=B[j] && B[j]<10 && B[j]>0)
           {
            B[j]++;
            C[j]--;
            sur++;
            break;    
           } 
         }
        else
         {
          if(flag==4 && A[j]==B[j] && A[j]!=C[j] && A[j]<10 && A[j]>0)
           {
            A[j]++;
            B[j]--;
            sur++;
            break;    
           }
          else if(flag==5 && A[j]==B[j] && A[j]==C[j] && A[j]<10 && A[j]>0 )
           {
            A[j]++;
            B[j]--;
            sur++;
            break;   
           } 
          else if(flag==6 && A[j]==C[j] && A[j]!=B[j] && A[j]<10 && A[j]>0)
           {
            A[j]++;
            C[j]--;
            sur++;
            break;    
           }
          else if(flag==7 && B[j]==C[j] && A[j]!=B[j] && B[j]<10 && B[j]>0)
           {
            B[j]++;
            C[j]--;
            sur++;
            break;    
           }    
         }   
       } 
      flag++;
      if(flag==8)
       flag=0;      
     }
     
    int y=0; 
    for(int j=0; j<N; j++)
     {
      if(A[j]>=p || B[j]>=p || C[j]>=p)
       y++;    
     }
    
    cout<<"Case #"<<(i+1)<<": "<<y<<endl;                        
   }
      
  return 0;    
 }
