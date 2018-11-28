#include<iostream> 
#include<cmath> 
#include<vector> 
#include<algorithm> 
#include<cstdio> 
#include<cstdlib> 
#include<string> 
#include<sstream> 
#include<map> 
#include<queue> 
#include<set> 

#define vi vector<int> 
#define vs vector<string> 

#define REP(i,n) for(int i=0;i<(int) n;i++) 
#define LL long long 

using namespace std;

#define N 50

char A[N][N];

int n;

int main()
{
   int kases;

    cin >> kases;


    for(int kase = 1 ; kase <= kases; ++ kase)
    {
        int pos[N];
        vector<int> v[N];
        bool booked[N];
        cout << "Case #" << kase << ": ";
          
        cin >> n;
    int res = 0;
        REP(i, n) 
        {
            v[i].clear();
            pos[i] = i;
            booked[i] = false;
        }

        REP(i,n)
        {
            int lastOne = -1;
            cin >> A[i];
            REP(j, n)
            {
                
                if(A[i][j] == '1')
                {
                    lastOne = j;
                }
            }
            
            for(int j = max(0, lastOne); j < n; ++j)
            {
                v[j].push_back(i);
            }
        }

        REP(i, n)
        {
            REP(j,v[i].size())
            {
                int node = v[i][j];
                if(!booked[node])
                {
                    booked[node] = true;
                    res += abs(pos[node] - i);
                    for(int k = 0; k < n; ++k)
                    {
                        if(k != node && pos[k] >= min(pos[node], i) && pos[k] <= max(pos[node], i))
                        {
                            if(pos[node] > i)
                            {
                                ++pos[k];
                            }
                            else
                            {
                                --pos[k];
                            }
                        }
                    }
                    pos[node] = i;
                    goto done;
                }
            }
done:;

        }
        cout << res << endl;
      
    }
    return 0;
    
}