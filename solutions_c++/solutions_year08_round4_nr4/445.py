#include <stdio.h>
#include <algorithm>
#include <vector>

#define oo 0x3f3f3f3f

using namespace std;

int main(void)
{
    int N,k,caso;
    char S[1024];

    for(scanf("%d",&N),caso = 1; caso <= N; caso++)
    {
        scanf("%d %s",&k,S);
        vector<int> v;

        for(int i = 0; i < k; i++)
            v.push_back(i);

        int mojo = +oo;
        do
        {
            char s[1024];
            strcpy(s,S);

            for(int i = 0; s[i]; i += k)
                for(int j = 0; j < k; j++)
                    s[i+j] = S[i+v[j]];

            int temp = 1;
            for(int i = 1; s[i]; i++)
                if (s[i] != s[i-1]) temp++;

            mojo = min(mojo,temp);

        } while(next_permutation(v.begin(),v.end()));

        printf("Case #%d: %d\n",caso,mojo);
    }

    return(0);
}

