#include<cstdio>
#include<algorithm>
#include<string>
#include<iostream>
#include<vector>
#include<cstring>
using namespace std;
#define out(x) cout<<#x<<": "<<(x)<<endl;
inline int Rint(){int x; scanf("%d",&x); return x; }

#define Two(x) ( 1 << (x) )
int main()
{
    
    freopen("large.in","r",stdin);
    freopen("large.out","w",stdout);
    int T = Rint();
    int O = 0;
    while ( T -- )
    {
           int n = Rint(),
               k = Rint();
           k &= ( Two(n) - 1 );
           
           printf("Case #%d: ",++O);
           puts( k == (Two(n) - 1) ? "ON" : "OFF");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
