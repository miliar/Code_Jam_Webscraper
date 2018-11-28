//#include <iostream>
//#include <algorithm>
//using namespace std;
//
//const int size=1100;
//struct DDD
//{
//    int id;
//    int va;
//}ddd[size];
//int a[size];
//bool b[size];
//int ans;
//int n;
//bool cmp(struct DDD a,struct DDD b){
//    return a.va<b.va;
//}
//void init(){
//    scanf("%d",&n);
//    for(int i=1;i<=n;i++)
//    {
//        scanf("%d",&ddd[i].va);
//        ddd[i].id=i;
//    }
//    sort(ddd+1,ddd+n+1,cmp);
//
//    for(int i=1;i<=n;++i)
//    {
//        a[ddd[i].id]=i;
//    }
//}
//void init(int kkk){
//    scanf("%d",&n);
//    for(int i=1;i<=n;i++)
//    {
//        scanf("%d",a+i);
//    }
//}
//void getans(){
//    ans=0;
//    memset(b,false,sizeof(b));
//    for(int i=1;i<=n;i++)
//    {
//        if(a[i]==i||b[i])continue;
//        int t=a[i];
//        while(t!=i)
//        {
//            ans+=2;
//            b[t]=true;
//            t=a[t];
//        }
//    }
//}
//int main()
//{
////    freopen("D-small-attempt3.in","r",stdin);
////    freopen("out3","w",stdout);
//    int t;
//    scanf("%d",&t);
//    for(int i=1;i<=t;i++)
//    {
//        init(1);
//        getans();
//        printf("Case #%d: %d.000000\n",i,ans);
//    }
//    return 0;
//}


#include <iostream>

using namespace std;

int a[10000];

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("out111555.txt", "w", stdout);
    int cases, sum, u, i, n;
    scanf("%d", &cases);
    for(u = 1; u <= cases; u++)
    {
        sum = 0;
        scanf("%d", &n);
        if(n == 1)
        {
            scanf("%d", &a[0]);
            printf("Case #%d: 0.000000\n", u);
            continue;
        }
        for(i = 1; i <= n; i++)
        {
            scanf("%d", &a[i]);
            if(a[i] == i)
                sum++;
        }
        printf("Case #%d: %d.000000\n", u, n - sum);
    }
    return 0;
}
