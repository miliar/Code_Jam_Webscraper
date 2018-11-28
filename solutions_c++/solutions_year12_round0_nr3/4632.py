#include<iostream>
#include<string>
#include<map>
#include<cmath>
using namespace std;

int noofdigits(int n)
{
    int i;
    for(i=0; n>0; n/=10, ++i);

    return i;
}

bool IsRecycled(int n1, int m)
{
    int nod = noofdigits(n1);
    int n = n1;

    do{
        int digit = n%10;
        n /= 10;
        n = (digit * pow(10.0, nod-1)) + n;
        if(n==m)
            return 1;
    }while(n != n1);

    return 0;
}

int pel(int n)
{
    int res = 0;
    while(n>0)
    {
        res *= 10;
        res += n%10;

        n /= 10;
    }

    return res;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;
    cin >> T;

    for(int t=0; t<T; ++t)
    {
        int A, B, res = 0;
        cin >> A >> B;

        ++B;

        for(int i=A; i<B; ++i)
        {
            for(int j=A; j<B; ++j)
            {
                if(i != j && IsRecycled(i, j))
                    res++;
            }
        }

        res /= 2;

        cout << "Case #" << t+1 << ": " << res << endl;
    }

    return 0;
}
