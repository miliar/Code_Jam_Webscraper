#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

map<pair<int, long long>, long long> open;

long long solve(int *a, int n, int th, int idx)
{
    if(idx == n)
        return 1;
    typedef map<pair<int, long long>, long long>::iterator iterator;
    iterator it = open.find(make_pair(idx, th));
    if(it != open.end())
        return it->second;

    long long cnt = 0;
    if(a[idx] > th) {
        cnt += solve(a, n, a[idx], idx+1);
    }
    cnt += solve(a, n, th, idx+1);
    cnt %= 1000000007;
    open.insert(make_pair(make_pair(idx, th), cnt));
    return cnt;
}

int main()
{
    int t;
    cin >> t;
    for(int ii=0;ii<t;ii++) {
        open.clear();
        long long n, m, x, y, z;
        int a[1000];
        cin >> n >> m >> x >> y >> z;
        for(int i=0;i<m;i++)
            cin >> a[i];

        int b[1000];
        for(int i=0;i<n;i++) {
            b[i] = a[i%m];
            a[i%m] = (x*a[i%m] + y*(i+1))%z;
        }
/*
        for(int i=0;i<n;i++)
            cout << b[i] << ' ';
        cout << endl;
*/
        cout << "Case #" << ii+1 << ": " << solve(b, n, -1, 0)-1 << endl;
    }

    return 0;
}
