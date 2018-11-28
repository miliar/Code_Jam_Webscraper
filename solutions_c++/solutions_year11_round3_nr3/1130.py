#include<iostream>
#include<fstream>
#include<list>
#include<queue>
#include<vector>

using namespace std;

int main()
{
 int T=0;
 ifstream in;
 ofstream out;
 in.open("C-small-attempt0.in");
 out.open("output.txt");
 in>>T;
 
         
         for(int i=1;i<=T;i++)
         {
          int N=0,L=0,H=0;
          in>>N>>L>>H;
            
          int array[N];
          bool check[N];
          for(int j=0;j<N;j++)
          {
           int temp;
           in>>temp;
           
           array[j]=temp;       
          }    
          bool count=false;
          int ans=0;
           while(L<=H)
           {
            for(int m=0;m<N;m++)
            {
             if(array[m]>L)
             {
               if(array[m]%L==0)
               {
                count=true;                
               }
               else
               {
                  count=false;
                  break;    
               }
             }
             
             else
             {
              if(L%array[m]==0)
               {
                count=true;                
               }
               else
               {
                  count=false;
                  break;    
               }   
             }       
            }
            if(count==true){ans=L;L=H;}
             L++;         
           }
           
           if(count==true)
           {
            out<<"Case #"<<i<<": "<<ans<<endl;              
           }
           else
           {
            out<<"Case #"<<i<<": NO"<<endl;   
           }
           
         }
 
 
 
 
 in.close();
 out.close();
 
 //system("pause");
 return 0;   
}
