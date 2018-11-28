#include <cstdio>
#include <string>
using namespace std;

typedef long long ll;

int isOn(ll what, ll start, ll row)
{
    if (row%(2*start) >= start)
       return 1;
       
    return 0;
}

int main()
{
    string test = "A-large";
    
    FILE *InputFile = freopen(("c:/codejam/2010/" + test + ".in").c_str(), "r", stdin);
    FILE *OutputFile = freopen(("c:/codejam/2010/" + test + ".out").c_str(), "w", stdout);
    
    int t, n, k;
    scanf("%d", &t);
    
    for (int i=0; i<t; i++)
    {
        scanf("%d %d", &n, &k);        
        
        int result = 1;
        ll start = 1;
        
        for (int j=0; j<n; j++)
        {
            result &= isOn((ll)(j+1), start, (ll)k);            
            start *= 2;
        }
        
        printf("Case #%d: ", i+1);
        if (result == 0)
           printf("OFF\n");
        else
           printf("ON\n");
    }
    
    return 0;
}
