#include<iostream>
#include<map>
#include<math.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef vector<int>::iterator iv;
typedef map<string,int>::iterator im;


int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int c=1, t, n, m, i, j, L, R, a[100];
    cin >> t;
    while(t--)
    {
        cin >> n >> L >> R;
        for(i=0; i<n; i++)
            cin >> a[i];
        for(i=L; i<=R; i++)
        {
            for(j=0; j<n; j++)
                if(a[j] % i && i % a[j])
                    break;
            if(j == n)
            {
                printf("Case #%d: %d\n", c++, i);
                break;
            }
        }
        if(i == R + 1)
            printf("Case #%d: NO\n", c++);
    }
}
