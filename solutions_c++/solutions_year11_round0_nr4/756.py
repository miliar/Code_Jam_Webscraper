#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    //*
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);//*/
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;++t)
    {
        int N, x, res=0;
        scanf("%d",&N);
        vector<int> a, b;
        for (int i=0;i<N;++i)
        {
            scanf("%d",&x);
            a.push_back(x);
        }
        b = a;
        sort(b.begin(),b.end());
        for (int i=0;i<N;++i)
            if (a[i]!=b[i])
                res++;
        printf("Case #%d: %d.000000\n", t, res);
    }
    //*
    fclose(stdin);
    fclose(stdout);//*/
    return 0;
}
