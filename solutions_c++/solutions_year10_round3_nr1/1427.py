#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#define max 1001
using namespace std;

main()
{
      
      freopen("input.txt", "r", stdin);
      freopen("output.txt", "w+", stdout);
      
      
      int i,j,T,N,K,count,A[max],B[max],C[max];
      cin>>T;
      int x1=0,x2=10;
      int y1,y2;
      int t=1;
      while(T-->0)
      {
                  
       cin>>N;
       for(i=0;i<N;i++)
        {
         cin>>y1>>y2;
         
         
         
         A[i] = y2-y1;
         B[i] = -1;
         C[i] = B[i]*y1;
         
         }
             double det,x,y;
             int count=0;
         for(i=0;i<N;i++)
          {
              det=0;           
           for(j=i+1;j<N;j++)
            {
             det = A[i]*B[j] - A[j]*B[i];
              if(det == 0){
        //Lines are parallel
             }
             else{
               x = (B[j]*C[i] - B[i]*C[j])/det;
               y = (A[i]*C[j] - A[j]*C[i])/det ;
               
               if(x>=0 && x<=1)
               {count++;}
              }
                 
            }
           // cout<<x<<"  "<<y<<endl;
            
            }
            
            cout << "Case #" << t << ": "<<count<<endl;
           // cout<<"x  :"<<x<<"y  :"<<y<<endl;
            t++;
        }
        
        
        system("pause");
}    
