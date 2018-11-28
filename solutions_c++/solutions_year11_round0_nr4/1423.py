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
    freopen ("D-large.in","r",stdin);
    freopen ("out.txt","w",stdout);
    
    int T;
    while (cin>>T)
    {
        for (int Case = 1; Case<=T; Case++)
        {
            int N;
            cin>>N;
            int C = 0;
            for (int i=1; i<=N; i++)
            {
                int n;
                cin>>n;
                if (n==i)
                    C++;    
            }
            cout<<"Case #"<<Case<<": "<<(N-C)<<endl;
        }    
    }
    
    
    
    return 0;
}



