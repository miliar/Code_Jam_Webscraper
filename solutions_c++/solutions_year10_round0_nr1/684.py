#include <iostream>

using namespace std;

int main()
{
    freopen("test.out","w",stdout);
    freopen("test.txt","r",stdin);
    int t; scanf("%d",&t);
   for(int times=1; times<=t;++times){
        int n,k;scanf("%d%d",&n,&k);
        printf("Case #%d: %s\n",times, ((k&((1<<n)-1))== ((1<<n)-1))?"ON":"OFF");

    }
    return 0;
}
