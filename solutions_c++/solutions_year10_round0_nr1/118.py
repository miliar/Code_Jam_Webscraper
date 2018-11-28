#include <iostream>

using namespace std;

int main()
{
    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);
    int t;
    cin >> t;
    for (int casenum=1;casenum<=t;casenum++)
    {
        cout <<"Case #"<< casenum << ": ";
        int n,k;
        cin >> n >>k;
        n=1 << n;
        if (k % n==n-1) cout << "ON" << endl;
            else cout << "OFF" << endl;
    }
}
