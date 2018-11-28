#include <iostream>
#include <vector>

using namespace std;

int max(int a, int b)
{
    return (a>b)?a:b;
}

int check(int value, int treshold, bool surprising)
{
    int minsum = 0;
    if(surprising)
        minsum = treshold*3-2*2;
    else
        minsum = treshold*3-2;
    if(value < treshold)
        return false;
    int ret = value >= minsum;
    //cout << value << ", " << treshold << ", " << surprising << "; " << minsum << " => " << ret << endl;
    return ret;
}

int getresult(int n, int s, int p, int* res)
{
    if(n == 0 && s == 0)
        return 0;
    if(s > n || s < 0)
        return -1;

    int r = -1;
    int a;

    a = getresult(n-1, s-1, p, res+1);
    if(a != -1)
        r = max(r, a + check(*res, p, true));

    a = getresult(n-1, s, p, res+1);
    if(a != -1)
        r = max(r, a + check(*res, p, false));
    
    return r;
}

int main()
{
    int testcases;
    cin >> testcases;

    for(int i = 0; i < testcases; i++)
    {
        int n, s, p;
        cin >> n >> s >> p;


        vector<int> tops;
        for(int a = 0; a < n; a++)
        {
            int f;
            cin >> f;
            tops.push_back(f);
        }

        int result = getresult(n, s, p, &tops[0]);

        cout << "Case #" << (i+1) << ": " << result << endl;
    }
}

