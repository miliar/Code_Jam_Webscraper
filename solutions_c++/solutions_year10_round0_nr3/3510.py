#include <iostream>
#include <queue>
using namespace std;

int main()
{
    freopen("in.in", "r", stdin);
	freopen("in.out", "w", stdout);
    int t, total, R, k, N, temp, temp1;
    cin >> t;
    for(int i = 1; i <= t; i ++)
    {
            queue<int> q;
            total = 0;
            cin >> R >> k >> N;
            for(int j = 0; j < N; j ++)
            {
                    cin >> temp;
                    q.push(temp);
            }
            
            for(int j = 1; j <= R; j ++)
            {
                  temp = 0;
                  for(int m = 1; m <= N; m ++)
                  {
                      temp1 = q.front();
                      if(temp1 <= (k - temp))
                      {
                          total += temp1;
                          temp += temp1;
                          q.pop();
                          q.push(temp1);     
                      }  
                      else
                      break;
                  }
            }
            
            cout << "Case #" << i << ": " << total << endl;
    }
    return 0;
}
