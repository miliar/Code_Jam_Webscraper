
#include <iostream>
#include <fstream>
#include <algorithm>
#include <climits>
#include <cstdio>
#include <cmath>




using namespace std;


int array[1100];



int main()
{
    freopen("C-large.in","r",stdin);
    freopen("output.out","w",stdout);

    int T;

    scanf("%d",&T);
    int N;

    for(int loop=1;loop<=T;loop++)
    {
        scanf("%d",&N);
        for(int i=0;i<N;i++)
        scanf("%d",&array[i]);
        int mask=0;
        for(int i=0;i<N;i++)
        mask^=array[i];

        if(0==mask)
        {
            sort(array,array+N);
            int res=0;
            for(int i=1;i<N;i++)
            res+=array[i];
            printf("Case #%d: %d\n",loop,res);
        }
        else
        {
            printf("Case #%d: NO\n",loop);
        }
    }

    return 0;
}
