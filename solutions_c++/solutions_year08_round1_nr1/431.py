#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long huge;

int main(void)
{
    int caso,N,T;

    for(caso = 1, scanf("%d",&T); caso <= T; caso++)
    {
        vector<huge> v1,v2;
        huge mojo;

        scanf("%d",&N);
        for(int i = 0; i < N; i++)
        {
            v1.push_back(0);
            scanf("%lld",&v1[i]);
        }

        for(int i = 0; i < N; i++)
        {
            v2.push_back(0);
            scanf("%lld",&v2[i]);
        }

        sort(v1.begin(),v1.end());
        sort(v2.rbegin(),v2.rend());

        mojo = 0;

        for(int i = 0; i < N; i++)
            mojo += v1[i]*v2[i];

        printf("Case #%d: %lld\n",caso,mojo);
    }

    return(0);
}

