#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// n,n-1,n-2 : 3n-3
// n-2,n-2,n : 3n-4
// n,n,n-2 : 3n-2

int getMaximumIfSumOfNonSuprisingTriplet (int M)
{
    if (M % 3 == 0)
    {
        // d,d,d
        return M/3;
    }
    else if ((M+1) % 3 == 0)
    {
        // d,d-1,d
        if ((M+1)/3 >= 1)
        {
            return (M+1)/3;
        }
    }
    else if ((M+2) % 3 == 0)
    {
        // d-1,d,d-1
        if ((M+2)/3 >= 1)
        {
            return (M+2)/3;
        }
    }
    return -1;
}

int getMaximumIfSumOfSurprisingTriplet (int M)
{
    // max value with surprising
    if ((M+3) % 3 == 0)
    {
        // d,d-1,d-2
        int d = (M+3)/3;
        if (d <= 10 && d >= 2)
        {
            return d;
        }
    }
    else if ((M+4) % 3 == 0)
    {
        // d-2,d-2,d
        int d = (M+4)/3;
        if (d <= 10 && d >= 2)
        {
            return d;
        }
    }
    else if ((M+2) % 3 == 0)
    {
        // d,d,d-2
        int d = (M+2)/3;
        if (d >= 2)
        {
            return d;
        }
    }
    return -1;
}

// algorithm
// 1. we will first try to get every sum from a NS triplet and check what maxVal we can get from it
// 2. if this way, we are able to get N more than (n-s) NS triplets which have maxVal >= p,
// 3. then we need to convert d = N-(n-s) triplets to S triplets, but we will try to convert as many of those which have maxVal >= p for S triplet config
// 4. if in 2, we get N <= (n-s) NS triplets with maxVal >= p or after 3
// 5. find maxVal for all remaining triplets in S config and find how many <= S have maxVal >= p

main()
{
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
            int maxVal = getMaximumIfSumOfNonSuprisingTriplet(M[i]);
            if (maxVal >= p)
            {
                ans++;
            }
            else if (s && M[i] > 1)
            {
                int maxVal = getMaximumIfSumOfSurprisingTriplet(M[i]);
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
