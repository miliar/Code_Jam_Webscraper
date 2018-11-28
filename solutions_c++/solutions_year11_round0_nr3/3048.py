#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <string>
using namespace std;

int n;
int arr[1005];
int dp[1005];

string ToBin (int sum)
{
    string ret = "";

    while (sum != 0)
    {
        int c = sum % 2;
        ret += (char)(c + '0');
        sum /= 2;
    }

    reverse (ret.begin() , ret.end());
    return ret;
}

int FromBin (string sum)
{
    int ret = 0;
    int prod = 1;

    for (int i=sum.size()-1; i>=0; i--)
    {
        ret += prod * (sum[i] - '0');
        prod *= 2;
    }

    return ret;
}

int Sum (int F , int S)
{
    string f = ToBin (F);
    string s = ToBin (S);

    int sz = max( f.size() , s.size() );
    int fsz = f.size();
    int ssz = s.size();

    for (int i=0; i<sz-fsz; i++)
		f = "0" + f;
    for (int i=0; i<sz-ssz; i++)
		s = "0" + s;

    string ret = "";

    for (int i=0; i<sz; i++)
    {
        int sum = (f[i] - '0') + (s[i] - '0');
        sum %= 2;
        ret += (sum + '0');
    }

    return FromBin (ret);
}

int solve (int ind , int sum1 , int sum2 , int n1 , int n2)
{
    if (ind == n) return (sum1 == sum2 && n1 != 0 && n2 != 0) ? 0 : -1<<30;

    int fS = Sum (sum1 , arr[ind]);
    int sS = Sum (sum2 , arr[ind]);

    int a = solve (ind+1 , fS , sum2 , n1+1 , n2) + arr[ind];
    int b = solve (ind+1 , sum1 , sS , n1 , n2+1);

    return max( a,b );
}

int main ()
{
    FILE *in = fopen ("C.in","r");
    FILE *out = fopen ("C.out","w");

    int t;

    fscanf (in,"%d",&t);

    for (int id=1; id<=t; id++)
    {
        fscanf (in,"%d",&n);
        for (int i=0; i<n; i++)
            fscanf (in,"%d",&arr[i]);

        int ret = solve (0,0,0,0,0);

        fprintf (out,"Case #%d: ",id);
        if (ret <= 0) fprintf (out,"NO\n");
        else fprintf (out,"%d\n",ret);
    }
}
