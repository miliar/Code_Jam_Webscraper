#include <iostream>
using namespace std;

int main()
{
   // freopen("A-large.in.txt", "r", stdin); freopen("out.txt", "w", stdout);
    int cs, n, k;
    cin>>cs;
    for (int i=1; i<=cs; i++)
    {
        cin>>n>>k;
        printf("Case #%d: %s\n", i, ((k+1)%(1<<n))==0?"ON":"OFF");
    }
    return 0;
}
