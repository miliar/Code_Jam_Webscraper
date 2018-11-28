#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>


using namespace std;

const int MAXN = 2000;

int Pos[MAXN];
int main()
{
    //freopen("test.in","r",stdin);

    freopen("c-large.in","r",stdin);
    freopen("c-large.out","w",stdout);
    int T;
    cin>>T;
    int tc=1;
    for(;tc<=T;tc++) {
        int n;
        cin>>n;
        int xor_result = 0,sum=0;
        for(int i = 0; i < n; i++) {
            cin>>Pos[i];
            xor_result^=Pos[i];
            sum+=Pos[i];
        }
        sort(Pos,Pos+n);
        sum-=Pos[0];
        if(xor_result!=0) printf("Case #%d: NO\n",tc);
        else printf("Case #%d: %d\n", tc, sum);
    }
    return 0;
}
