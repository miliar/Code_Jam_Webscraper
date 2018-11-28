#include <iostream>
#include <cmath>
#include <string>

using namespace std;

string solve()
{
    __int64 n, k, t;
    scanf("%I64d %I64d", &n, &k);
    
    t=1LL<<n;
    if( (k%t)==(t-1LL) ) return "ON";
    else return "OFF";         
}

int main()
{
    freopen("A-large.in", "r", stdin);
    
    freopen("A-large.out", "w", stdout);
    
    int cases, caseid;
    
    scanf("%d", &cases);
    for(caseid=1; caseid<=cases; ++caseid) 
        printf("Case #%d: %s\n",caseid, solve().c_str());
        //cout << "Case #" << caseid << ": " << solve() << endl;
    return 0;    
}
