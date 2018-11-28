#include <stdio.h>
#include <algorithm>
#include <string>
#include <map>

#define MOJO 1024
#define oo 0x3f3f3f3f
int voodoo[MOJO][MOJO],v[MOJO];
int N,S,Q;

using namespace std;

int voodoo_doll(int n, int x)
{
    int &mojo = voodoo[n][x];

    if (n == 0) mojo = 0;
    if (v[n] == x) mojo = +oo;

    if (mojo < 0)
    {
        mojo = voodoo_doll(n-1,x);
        for(int i = 0; i < S; i++)
            mojo = min(mojo,voodoo_doll(n-1,i)+1);
    }

    return(mojo);
}

int main(void)
{
    int caso;

    for(scanf("%d",&N), caso = 1; caso <= N; caso++)
    {
        memset(voodoo,-1,sizeof(voodoo));
        scanf("%d",&S);
        map<string,int> m;
        char s[256];
        gets(s); // lixo
        for(int i = 0; i < S; i++)
        {
            gets(s);
            m[string(s)] = i;
        }

        scanf("%d",&Q);
        gets(s); // lixo
        for(int i = 0; i < Q; i++)
        {
            gets(s);
            v[i+1] = m[string(s)];
        }

        int mojo = +oo;
        for(int i = 0; i < S; i++)
            mojo = min(mojo,voodoo_doll(Q,i));

        printf("Case #%d: %d\n",caso,mojo);
    }

    return(0);
}

