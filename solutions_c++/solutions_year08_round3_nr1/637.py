#include <algorithm>
#include <cstdio>

#define MAXN 1000000

using namespace std;

int Freq[MAXN+1];

int main()
{
    int NTest;
    scanf("%d",&NTest);
    for(int TestNum=1;TestNum<=NTest;TestNum++)
    {
        int NKey,KeyLen,N,Answer=0;
        scanf("%d %d %d",&KeyLen,&NKey,&N);
        for(int q=0;q<N;q++)scanf("%d",Freq+q);
        sort(Freq,Freq+N);
        int q=N-1;
        for(int e=1,w=0;q>=0;q--)
        {
            if(e>KeyLen)break;
            Answer+=Freq[q]*e;
            w++;
            if(w==NKey)
            {
                w=0;
                e++;
            }
        }
        if(q>=0)printf("Case #%d: Impossible\n",TestNum);
        else printf("Case #%d: %d\n",TestNum,Answer);
    }
    return 0;
}
