#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int T;
    cin>>T;
    int i,j;
    for(i=0;i<T;i++)
    {
     int N, s, p, t;//[110];
     cin>>N;
     cin>>s;
     cin>>p;
     int pass = 0;
     for(j=0;j<N;j++)
     {
      cin>>t;
      int rata = t/3;
      int sisa = t%3;
      if(rata>=p)
       pass++;
      if(rata<=p-3)
       continue;
      
      if(rata==p-1)
      {
       if(sisa>=1)
        pass++; 
       else 
       { 
            if(s>0 && rata>=1) {s--; pass++;}
       }
        
      }
      
      if(rata==p-2)
      {
       if(s>0 && rata>=1 && sisa==2){ s--; pass++;}
      }
     
     }
      
     
     cout<<"Case #"<<i+1<<": "<<pass<<endl;
    }

    return 0;
}
