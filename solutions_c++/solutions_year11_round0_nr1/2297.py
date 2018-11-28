#include <iostream>
#include <queue>

using namespace std;
typedef pair<int, int> PII;

int main()
{
    int T;
    cin >> T;
    
    for(int t=1; t<=T; t++)
    {
      int N;
      cin >> N;
      
      int result = 0;
      
      queue<PII> RQ[2];
      int pos[2];
      pos[0] = pos[1] = 1;
      
      for(int j=1; j<=N; j++){
          char who;
          int where;
          cin >> who >> where;
          RQ[(who=='O')?0:1].push(PII(j, where));
      }   
      
      int j=1;
      while(!RQ[0].empty() || !RQ[1].empty())
      {
          bool pushed=false;
          for(int r=0; r<2; r++)
          {
               if(RQ[r].empty())
                   continue;
               if(RQ[r].front().first == j && RQ[r].front().second == pos[r] && !pushed){
                   RQ[r].pop();
                   pushed=true;
                   j++;
                   continue;                       
               }
               if(RQ[r].front().second == pos[r])
                   continue;
               
               pos[r] += (RQ[r].front().second < pos[r]) ? -1 : 1;
          }       
          result++;              
      }
      cout << "Case #" << t << ": " << result << endl;
    }
}
