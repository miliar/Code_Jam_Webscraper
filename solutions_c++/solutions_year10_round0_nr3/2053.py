#include <iostream>
using namespace std;
unsigned long long R,k,N;

unsigned long long circle[1001];
int used[1001];
unsigned long long sumsize[1001];
unsigned long long values[1001];
int T;
int main()
{
    cin>>T;
     int i;
      for(i = 1; i <= T; i++)
       {
        cin>>R>>k>>N;
         int j;
          for(j = 1; j <= N; j++)
           cin>>values[j];
          int t = 1;
          memset(used,0,sizeof(used));
          memset(sumsize,0,sizeof(sumsize));
          unsigned long long temp = 0;
          int size = 0;
          unsigned long long ans = 0;
          /*for(j = 1; j <= R; j++) 
           {
            int lvl;
            int help[1001];
            memset(help,0,sizeof(help));
            unsigned long long sum = 0;
             for(lvl = t; sum + values[(lvl > N ? 1 : lvl)] <= k ; lvl++)
              {
               if(lvl > N) lvl = 1;
               if(help[lvl]) break;
               help[lvl] = 1;
               sum += values[lvl];
               t = lvl + 1;
               if(t > N) t = 1;
              }
              
             ans += sum; 
           }
           
           cout<<"Case #"<<i<<": "<<ans<<endl;
           */
          while(used[t] == 0)
           {
            used[t] = size + 1;
             unsigned long long sum = 0;
             int begin = t;
            int help[1001];
            memset(help,0,sizeof(help));
            for(j = t; sum + values[(j > N ? 1 : j)] <= k ; j++)
             {
             if(j > N) j = 1;
             if(help[j] == 1) break;
             t = j;
             help[j] = 1;
             sum += values[j];
             }
             t++;
             if(t > N) t = 1;
             //cout<<size<<" --- > "<<t<<endl;
             temp += sum;
            size++; 
            sumsize[size] = temp;
          //  cout<<t<<" ---> "<<sumsize[size]<<endl;
        //    int help = j + 1;
            //if(
           }
           //cout<<t<<endl;
           //cout<<
          // unsigned long long circle = temp - sumsize[used[t]];
           if(size == used[t]) 
            {
             size++;
             sumsize[size] = sumsize[size - 1] * 2;
            }
          //cout<<t<<" : "<<size<<" : "<<used[t]<<" "<<sumsize[size]<<endl;
           unsigned long long part =  sumsize[used[t] - 1] + (sumsize[size] - sumsize[used[t] - 1])*((R - (used[t] - 1))/(size - (used[t] - 1)));
           
           int bla = (R - (used[t] - 1))%(size - (used[t] - 1));
          
          
          for(j = 1; j <= bla; j++) 
           {
            int lvl;
            int help[1001];
            memset(help,0,sizeof(help));
            unsigned long long sum = 0;
             for(lvl = t; sum + values[(lvl > N ? 1 : lvl)] <= k ; lvl++)
              {
               if(lvl > N) lvl = 1;
               if(help[lvl]) break;
               help[lvl] = 1;
               sum += values[lvl];
               t = lvl + 1;
               if(t > N) t = 1;
              }
              
             part += sum; 
           }
          
          
           
           if(R > size)
           cout<<"Case #"<<i<<": "<<part<<endl;
           else   cout<<"Case #"<<i<<": "<<sumsize[R]<<endl;
          
       }  
    return 0;
}
