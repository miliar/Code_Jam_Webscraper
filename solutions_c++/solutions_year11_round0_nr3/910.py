#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;

void printarr(long *arr, int len);


int main()
{
    int loop;
    ifstream in("C-large.in");
    ofstream out("output.txt");
    in>>loop;
    
    for(int i=0; i<loop; i++)
    {
         int loop2;
         in>>loop2;//cout<<"loop2: "<<loop2<<endl;
         long *intvec = new long[loop2];
         priority_queue<long> que;
         for(int j=0; j<loop2; j++)
         {
             long temp;
             in>>temp;
             intvec[j]=temp;        
         }
         sort(intvec,intvec+loop2);
         //printarr(intvec,loop2);
         for(int k=0; k<loop2-1; k++)
         {
              long res=0;
              long pqr=0;   
              for(int l=loop2-1; l>k; l--)
              {
                  res =res^intvec[l];    
              }         
              for(int m=0; m<=k; m++)
              {
                  pqr=pqr^intvec[m];     
              } 
              if(res==pqr)
              {
                  long ans=0;        
                  for(int l=loop2-1; l>k; l--)
                  {
                      ans =ans+intvec[l];    
                  }            
                  que.push(ans);
              }
                            
         }
         
         
         if(que.empty()==true)
         out<<"Case #"<<i+1<<": NO"<<endl;
         else
         {
             long ans = que.top();
             if(ans==0)
             out<<"Case #"<<i+1<<": NO"<<endl;
             else
             out<<"Case #"<<i+1<<": "<<que.top()<<endl;    
         }
         /*if(que.empty()==true)
         cout<<"Case #"<<i+1<<": NO"<<endl;
         else
         {
             long ans = que.top();
             if(ans==0)
             cout<<"Case #"<<i+1<<": NO"<<endl;
             else
             cout<<"Case #"<<i+1<<": "<<que.top()<<endl;    
         }*/
         
    }
    in.close();
    out.close();
    //system("pause");
    return 0;    
}

void printarr(long *arr,int len)
{
     for(int i=0; i<len; i++ )
     {
         cout<<arr[i]<<" ";        
     }
     cout<<endl;
          
}
