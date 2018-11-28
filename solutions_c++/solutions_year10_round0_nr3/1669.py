#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int cases, cas;
    cin >> cases;
    for(cas = 1; cas <= cases; cas++)    
    {
            long long r, n, k;
            cin >> r >> k >> n;
            vector <int> a(n, 0);
            int i, j, t;
            //long long sum = 0;
            //vector <bool> flag(n, false);
            vector <int> end(n, -1);
            vector <long long> pri(n, 0);
            for(i = 0; i < n; i++)
            {
                  cin >> a[i];
                  //sum += a[i];
            }
            i = 0;
            long long curSum = 0;
            long long earned = 0;
            for(int ride = 1; ride <= r; ride++)
            {
                    
                    if(end[i] == -1)        
                    {
                         curSum = 0;
                         for(j = i, t = 0; t < n; t++)          
                         {
                               if(a[j] + curSum <= k)      
                                       curSum += a[j];
                               else
                                   break;
                               j = (j+1)%n;
                         }
                         end[i] = j;
                         pri[i] = curSum;
                         i = j;
                         earned += curSum;
                    }
                    else
                    {
                        earned += pri[i];
                        i = end[i];    
                    }
            }
            cout << "Case #" << cas << ": " << earned << endl;
            
    }
    return 0;
}
