#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char s[20];

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("out.txt","w",stdout);


    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        int N;
        scanf("%d",&N);
        int pB = 1, timB = 0, pO = 1, timO = 0;
        int ret = 0;
        for(int i = 0; i < N; i++)
        {
            int x;
            scanf("%s%d",s,&x);
            if(s[0]=='O')
            {
                int tmp = max(0, abs(x-pO)-timB)+1;
                pO = x;
                ret += tmp;
                timO += tmp;
                timB = 0;
            }
            else
            {
                int tmp = max(0, abs(x-pB)-timO)+1;
                pB = x;
                ret += tmp;
                timB += tmp;
                timO = 0;
            }
        }
        printf("Case #%d: %d\n",++cas,ret);
    }

    return 0;
}
