#include<iostream>
#include<string>
#include<stdio.h>

using namespace std;

string name[101];
string call[100001];
int main()
{
    int t, n, c;
    cin >> t;


    for(int tt=0; tt<t; tt++)
    {
            cin >> n;

            getline(cin, name[0]);
            for(int i=0; i<n; i++)
            {
                    getline(cin, name[i]);
            }

            cin >> c;
            getline(cin, call[0]);
            for(int i=0; i<c; i++)
            {
                    getline(cin, call[i]);
            }
            
            int now = 0, idx = -1, cnt = 0;
            
            while(now < c)
            {
                      int bestgo = now, bestidx = idx;
                      for(int i=0; i<n; i++)
                      {
                              if (i != idx)
                              {
                                    int tmp = now;
                                    while(tmp < c && call[tmp] != name[i]) tmp++;
                                    if (tmp == c) { now = c; cnt++; break; }
                                    else
                                    {
                                        if (tmp > bestgo)
                                        {
                                                bestgo = tmp; bestidx = i;
                                        }
                                    }
                              }
                      }
                      
                      if (now < c)
                      {
                              now = bestgo; idx = bestidx; cnt++;
                      }
            }
            if (cnt == 0) cnt = 1;
            cout << "Case #" << tt+1 << ": " << cnt - 1 << endl;
    }
    
    return 0;
}
