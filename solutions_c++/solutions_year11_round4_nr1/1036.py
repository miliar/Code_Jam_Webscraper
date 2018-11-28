#include <cstdio>
#include <algorithm>

using namespace std;

struct walkway
{
    int B,E,w,len;
};

bool lesss(walkway a,walkway b)
{
    return a.w<b.w;
}

int main()
{
    int T;
    scanf("%d",&T);
    for (int num=1;num<=T;++num)
    {
        int X,S,R,N,wlen=0;
        double t,ans=0;
        walkway W[1010];
        scanf("%d%d%d%lf%d",&X,&S,&R,&t,&N);
        for (int i=0;i<N;++i)
        {
            scanf("%d%d%d",&W[i].B,&W[i].E,&W[i].w);
            W[i].len = W[i].E-W[i].B;
            wlen += W[i].len;
        }
        X -= wlen;
        sort(W,W+N,lesss);
        if (X>t*R)
        {
            ans = t+(X-t*R)*1./S;
            t=0;
        }
        else
        {
            ans = 1.*X/R;
            t-=ans;
        }
        for (int i=0;i<N;++i)
        {
            if (W[i].len>t*(R+W[i].w))
            {
                ans += t+(W[i].len-t*(R+W[i].w))*1./(S+W[i].w);
                t=0;
            }
            else
            {
                ans += 1.*W[i].len/(R+W[i].w);
                t -= 1.*W[i].len/(R+W[i].w);
            }
        }
        printf("Case #%d: %.9lf\n",num,ans);
    }
    return 0;
}
