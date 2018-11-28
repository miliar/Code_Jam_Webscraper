#include <stdio.h>
#include <vector>
#include <string>
using namespace std;

bool desc(long long a, long long b) { return a > b; }

int main()
{
    freopen("A.in","r",stdin); freopen("A.out.txt","w",stdout);
    int test;
    scanf("%d", &test);
    for(int t=1; t<=test; t++)
    {
        int n;
        scanf("%d", &n);
        vector <long long> a, b;
        int temp;
        for(int i=0; i<n; i++)
        {
            scanf("%I64d", &temp);
            a.push_back(temp);
        }
        for(int i=0; i<n; i++)
        {
            scanf("%I64d", &temp);
            b.push_back(temp);
        }
        sort(a.begin(), a.end());
        sort(b.begin(), b.end(), desc);
        long long sum = 0;
        for(int i=0; i<n; i++) sum += a[i]*b[i];
        printf("Case #%d: %I64d\n", t, sum);
    }
}
