#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
long long tst()
{
    int n;
    cin >> n;
    vector<long long> a(n);
    vector<long long> b(n);
    for(int i=0;i<n;i++)
        cin >> a[i];
    for(int i=0;i<n;i++)
        cin >> b[i];
    sort(a.begin(),a.end());
    sort(b.rbegin(),b.rend());
    long long ans=0;
    for(int i=0;i<n;i++)
        ans += a[i]*b[i];
    return ans;
}
int main()
{
    int n;
    cin >> n;
    for(int i=1;i<=n;i++)
        cout << "Case #" << i << ": " << tst() << endl; 
}
