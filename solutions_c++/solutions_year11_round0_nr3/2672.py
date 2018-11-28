#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <queue>
#include <deque>
#include <vector>
#include <cstdlib>
#include <cstdlib>
#include <cstdio>
#include <sstream>
#include <stack>
#include <set>
#include <functional>
#include <map>
#define eps 1e-3
using namespace std;


int main ()
{
    freopen ("C-small-attempt0.in","r",stdin);
    freopen ("out.txt","w",stdout);
    
    int T;
    while (cin>>T)
    {
        for (int Case = 1; Case<=T; Case++)
        {
            int N;
            cin>>N;
            int sum = 0;
            vector <int> V(N);
            for (int i=0; i<N; i++)
            {
                cin>>V[i];
                sum+=V[i];
            }
            
            
            int res = 0;
            for (int i=0; i<(1<<N); i++)
            {
                int temp1 = 0,temp2 = 0;
                int t_sum = 0;
                for (int j=0; j<N; j++)
                {
                    if (i&(1<<j))
                    {
                        temp1 = temp1 ^ V[j] ;
                        t_sum += V[j];   
                    }    
                    else
                        temp2 = temp2 ^ V[j] ;
                }    
                if (temp1==temp2 && t_sum != sum && t_sum!=0)
                {
                    res = max(res, t_sum);
                    res = max (res,sum-t_sum);
                }
            }
            if (res)
                cout<<"Case #"<<Case<<": "<<res<<endl;
            else
                cout<<"Case #"<<Case<<": NO"<<endl;
        
        }    
    }
    
    
    
    return 0;
}



