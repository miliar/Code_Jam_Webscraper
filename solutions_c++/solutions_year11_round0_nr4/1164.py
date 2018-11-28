#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    //freopen("input.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    int t;
    int n;
    cin >> t;
    for(int i=1; i<=t; i++)
    {
        cin >> n;
        double ans=0;
        int a;
        for(int j=1; j<=n; j++)
        {
            cin >> a;
            if(a!=j)
                ans++;
        }
        printf("Case #%d: %.6lf\n", i, ans);
    }
}
