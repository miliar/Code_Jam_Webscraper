#include<string>
#include<cmath>
using namespace std;
int T, N, Q;
int rel[8];

int sim()
{
    bool jail[N+1];
    for(int i =0;i<N+1;i++)
      jail[i] = true;
              int c =0;
    for(int i =0;i<Q;i++)
    {
        jail[rel[i]] = false;
        int r = rel[i]+1;
        int l = rel[i]-1;
        for(int j =r;j<=N && jail[j];j++)
          c++;
        for(int j =l;j>=1 && jail[j];j--)
          c++;
    }
    return c;
}
int main()
{
    scanf("%d", &T);
    for(int c = 1;c<=T;c++)
    {
        scanf("%d%d", &N,&Q);
        for(int i=0;i<Q;i++)
        {
            scanf("%d", &rel[i]);
        }
        sort(rel, rel+Q);
        int m=1000000000;
        do
        {
            m= min(m,  sim());
        }while(next_permutation(rel, rel+Q));

        printf("Case #%d: %d\n", c, m);
    }
}
