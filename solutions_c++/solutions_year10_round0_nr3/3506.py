#include<iostream>
using namespace std;

long doSim(int N, int k, int R, int g[])
{
   long money =0;  
   int ptr = -1; 
   for(int r=0; r<R; ++r)
   {
       long sum =0;
       int count =0;    
       while(1)
       {  
          if(count>=N) break;       
          int curgrpSize = g[(ptr+1)%N];
          if(sum + curgrpSize > k) break;
          ++ptr;
          count++; 
          sum+=curgrpSize;
       }
       money+= sum;
   }
   return money;
}

int main()
{
    int t;
    cin >> t;
    for(int i =0; i < t; ++i)
    {
          int N;
          int k,R;
          cin >> R >> k >> N;
          //cout << R << k << N;
          int g[1000];
          for(int j=0; j< N; ++j)
          {
            cin>>g[j];
            //cout<<g[j];
          } 
          
          long  money = doSim(N,k,R,g); 
          cout << "Case #" << i+1 <<": "<<money<<"\n";
    } 
    return 0;
}
