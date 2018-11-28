#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b.txt","w",stdout);
    int ti;
    scanf("%d",&ti);
    for(int ca=1;ca<=ti;ca++)
    {
        int N,S,p;
        scanf("%d%d%d",&N,&S,&p);
        int tmp1;
        if(p>=1)tmp1=3*p-2;
        else tmp1=0;
        int tmp2;
        if(p>=2)tmp2=3*p-4;
        else tmp2=1000;
        int fi=0,se=0;
        for(int i=0;i<N;i++)
        {
            int tmp;
            scanf("%d",&tmp);
            if(tmp>=tmp1)fi++;
            else if(tmp>=tmp2)se++;
        }
  //      printf("%d %d\n",fi,se);
        printf("Case #%d: %d\n",ca,fi+min(se,S));
    }
}
