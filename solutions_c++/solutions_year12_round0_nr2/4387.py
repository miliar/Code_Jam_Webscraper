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
#define eps 1e-8
using namespace std;

int main ()
{
    //freopen("B-small-attempt0.in","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    int T;
    while ( scanf("%d\n",&T)!=EOF )
    {
        for ( int Case = 1; Case<=T; Case++ )
        {
            int N, S , P;
            cin>> N >> S >> P;
            int res = 0;
            int Point;
            for ( int i=0; i<N; i++ )
            {
                cin>> Point;
                int Div =  Point / 3;
                int Mod = Point % 3;
                if ( Div >= P )
                    res++;
                else if ( P-Div == 1 && Mod !=0 )
                    res++;
                else if ( ( (P-Div == 1 && Mod ==0 && Div != 0) || (P-Div == 2 && Mod == 2) ) && S )
                {
                    res++;
                    S--;    
                }
            }
            cout<<"Case #"<<Case<<": "<<res<<endl;
        }
    }
    return 0;
}

