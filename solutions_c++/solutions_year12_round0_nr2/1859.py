#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>
#include<cstring>


using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size


#define pf printf
#define sf scanf

int main()
{
    //freopen("sample.txt","r",stdin);
    freopen("b.in","r",stdin);
    freopen("b.ans","w",stdout);

    int kase=1;
    int t;
    sf("%d",&t);

    while(t--)
    {
        int n,s,p;
        sf("%d %d %d",&n,&s,&p);
        int i,j,k;
        int scores[105];
        for(i=0;i<n;i++)
            sf("%d", &scores[i]);
        int counter=0;
        int siter;
        for( siter = 0;siter<n;siter++)
        {
            bool surp=true;
            bool countable = false;
            for(i=0;i<=10;i++)
                for(j=i;j<=10 && j<=i+2;j++)
                    for(k=j;k<=10 && k<=i+2;k++)
                    {
                        if ( i+j+k == scores[siter])
                            if (k>=p)
                            {
                                if ( k-i==2 && s > 0)
                                    countable=true;
                                else if ( k-i< 2)
                                    countable=true, surp=false;
                            }
                    }
            if ( countable)
            {
                counter++;
                if ( surp )
                    s--; // charge surprise
            }
        }
        pf("Case #%d: %d\n",kase++,counter);
    }


    return 0;
}
