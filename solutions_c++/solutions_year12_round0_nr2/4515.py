#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int Maximum(int);
int NoMaximum(int);

main()
{
     freopen("B-large.in","r",stdin);
     freopen("rav22_Blarge.txt","w",stdout);
    int t,n,s,p;
    cin >> t;

    for (int iIndex = 1; iIndex <= t; iIndex++)
    {
        cin >> n >> s >> p;
        int M[n];
        for (int i = 0; i < n; i++)
        {
            cin >> M[i];
        }

        int ans = 0;
        for (int i = 0; i < n; i++)
        {
            int maxVal = NoMaximum(M[i]);
            if (maxVal >= p)
            {
                ans++;
            }
            else if (s && M[i] > 1)
            {
                int maxVal = Maximum(M[i]);
                if (maxVal >= p)
                {
                    ans++;
                    s--;
                }
            }
        }
        cout << "Case #" << iIndex << ": " << ans << "\n";
    }
}


int NoMaximum (int M)
{
    if (M % 3 == 0)
    {
        return M/3;
    }
    else if ((M+1) % 3 == 0)
    {
        if ((M+1)/3 >= 1)
        {
            return (M+1)/3;
        }
    }
    else if ((M+2) % 3 == 0)
    {
        if ((M+2)/3 >= 1)
        {
            return (M+2)/3;
        }
    }
    return -1;
}

int Maximum (int M)
{
    if ((M+3) % 3 == 0)
    {
        int d = (M+3)/3;
        if (d <= 10 && d >= 2)
        {
            return d;
        }
    }
    else if ((M+4) % 3 == 0)
    {
        int d = (M+4)/3;
        if (d <= 10 && d >= 2)
        {
            return d;
        }
    }
    else if ((M+2) % 3 == 0)
    {
        int d = (M+2)/3;
        if (d >= 2)
        {
            return d;
        }
    }
    return -1;
}


