#include <iostream>
#include <cmath>

using namespace std;

int pow(int a, int b)
{
    int r = 1;
    for (int i = 0; i < b; i++)
        r *= a;
    return r;
}

int is_recyc(int a, int b)
{
    int k;
    int d;
    int s_a, s_b;

    s_a = s_b = 0;

    if (a >= b)
        return 0;

    k=a;
    d = 0;
    while(k>=1)
    {
        s_a +=k%10;
        k=k/10;
        d++;
    }

    k=b;
    while(k>=1)
    {
        s_b +=k%10;
        k=k/10;
    }

    if (s_a != s_b)
        return 0;

    int pair_a, i;
    for (i = 1; i < d; i++) {
        pair_a = (((a % pow(10,i)) * pow(10,d-i))) + (a / pow(10,i));
        if (pair_a == b) {
            //cout << a << " " << pair_a << endl;
            return 1;
        }
    }

    return 0;
}

int main()
{
    int t,N,M;
    cin>>t;
    for(int c=0;c<t;c++) {
        cin>>N>>M;

        int res = 0;
        for (int i = N; i <= M; i++)
            for (int j = N; j <= M; j++) {
                if (is_recyc(i, j) == 1)
                    res++;
            }
        cout <<"Case #"<<c+1<<": "<<res<<endl;
    }
}
