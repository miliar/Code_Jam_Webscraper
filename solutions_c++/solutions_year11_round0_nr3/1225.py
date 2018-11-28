#include<iostream>
#include<fstream>
#include<vector>
#include <algorithm>

using namespace std;

int main()
{
 int T,N;
 ifstream in;
 ofstream out;
 in.open("C-small-attempt0.in");
 out.open("output.txt");
 in>>T;
 
         for(int i=1;i<=T;i++)
         {
          in>>N;
          long arr[N];
          vector<int> my;
          for(int j=0;j<N;j++)
          {
           in>>arr[j];
          }
          sort(arr,arr+N);
          
          for(int k=0; k<N-1; k++)
         {
              long r=0;
              long p=0;   
              for(int l=N-1; l>k; l--)
              {
                  r =r^arr[l];    
              }         
              for(int m=0; m<=k; m++)
              {
                  p=p^arr[m];     
              } 
              if(r==p)
              {
                  long ans=0;        
                  for(int l=N-1; l>k; l--)
                  {
                      ans =ans+arr[l];    
                  }            
                  my.push_back(ans);
              }
              
               
                            
         }
          
          if(my.empty()==true)
         out<<"Case #"<<i<<": NO"<<endl;
         else
         {
             sort(my.begin(),my.end());
             
             long ans = my[my.size()-1];
             if(ans==0)
             out<<"Case #"<<i<<": NO"<<endl;
             else
             out<<"Case #"<<i<<": "<<ans<<endl;    
         }
          
          
         }
         in.close();
         out.close();
 
 //system("pause");
 return 0;
 
}
