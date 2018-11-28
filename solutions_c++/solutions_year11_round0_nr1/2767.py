#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T, N;
    string str;

    getline(cin,str);
    sscanf(str.c_str(),"%d",&T);

    for(int TT=0; TT<T; ++TT)
    {
        getline(cin,str);
        istringstream strin(str);
        strin >> N;
        char r;
        long long x;
        long long b = 1, ab = 0, o = 1, ao = 0, cnt = 0;
        for(int i=0; i<N; ++i)
        {
            strin >> r >> x;
            if(r == 'O')
            {
                long long d = ao + abs(x - o);
                if(d > ab)
                {
                    ao = d + 1;
                }
                else
                {
                    ao = ab + 1;
                }
                o = x;
            }
            else if(r == 'B')
            {
                long long d = ab + abs(x - b);
                if(d > ao)
                {
                    ab = d + 1;
                }
                else
                {
                    ab = ao + 1;
                }
                b = x;
            }
        }
        printf("Case #%d: %lld\n",TT+1,max(ao,ab));
    }

    return 0;
}
