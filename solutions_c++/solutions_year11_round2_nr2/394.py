#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <cstdio>
#include <cmath>
#include <cstring>




using namespace std;


int P[1000],V[1000];
int array[1100000];
int C,D;






int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);


    int T;
    scanf("%d",&T);

    for(int loop=1;loop<=T;loop++)
    {
        scanf("%d%d",&C,&D);

        for(int i=0;i<C;i++)
        {
            scanf("%d%d",&P[i],&V[i]);
        }

        int cnt=0;
        for(int i=0;i<C;i++)
        {
            while(V[i])
            {
                array[cnt++]=P[i];
                V[i]--;
            }
        }
        double tmp;
        double res=0;
        tmp=0;
        int start=0;
        double acc=0;
        for(int i=1;i<cnt;i++)
        {
            if(D>array[i]-array[i-1])
            {
                tmp+=double(D-array[i]+array[i-1]);
            }
            else
            {
                if(res<tmp+acc)
                res=tmp+acc;
                tmp=0;
                if(double(array[i]-array[start])<acc+double(i-start)*double(D))
                {
                    acc=acc+double(i-start)*double(D)-double(array[i]-array[start]);
                }
                else
                {
                    acc=0;
                }
                start=i;
            }
        }
        if(res<tmp+acc)
        res=tmp+acc;
        res/=2;
        printf("Case #%d: %0.10lf\n",loop,res);

    }











    return 0;
}
