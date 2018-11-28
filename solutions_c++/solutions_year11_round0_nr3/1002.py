#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;




int main()
{
    int N;
    ifstream in("WWWW.in");
    ofstream out("output.txt");
    in>>N;
    
    for(int i=0; i<N; i++)
    {
         int N2;
         in>>N2;
         long *intvec = new long[N2];
         priority_queue<long> que;
         for(int j=0; j<N2; j++)
         {
             long temp;
             in>>temp;
             intvec[j]=temp;        
         }
         sort(intvec,intvec+N2);
         for(int k=0; k<N2-1; k++)
         {
              long res=0;
              long temp=0;   
              for(int x=N2-1; x>k; x--)
              {
                  res =res^intvec[x];    
              }         
              for(int y=0; y<=k; y++)
              {
                  temp=temp^intvec[y];     
              } 
              if(res==temp)
              {
                  long ans=0;        
                  for(int x=N2-1; x>k; x--)
                  {
                      ans =ans+intvec[x];    
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

    }
    in.close();
    out.close();
    //system("pause");
    return 0;    
}


