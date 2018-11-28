#include  <cstdio> 
#include  <cstdlib> 
#include  <cstring> 
#include  <string> 
#include  <vector> 
#include  <cmath> 
#include  <algorithm> 
#include  <cassert> 
#include  <set> 
#include  <map> 
#include  <queue> 
#include  <iostream> 
#include <fstream> 
using namespace std; 
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )  

typedef long long LL; 
typedef pair<int,int> pii; 

//~ int s[100];

int main()
{
    int cases;
    scanf("%d", &cases);
    for (int casen = 1; casen <= cases; casen++)
    {
        int N, K;
        scanf("%d %d", &N, &K);
        //~ memset(s, 0, sizeof s);
        //~ s[0] = 1;
        //~ while (K--)
        //~ {
            //~ int t = 1;
            //~ for (int i = 1; i <= N; i++)
            //~ {
                //~ if (t)
                    //~ s[i] = !s[i];
                //~ if (s[i])
                    //~ break;
            //~ }
        //~ }
        printf("Case #%d: %s\n", casen, ((K + 1) % (1 << N)) ? "OFF" : "ON");
    }
    return 0;
}
