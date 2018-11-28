#include <cstdio>
#include <set>
#include <algorithm>
using namespace std;

int topbit(int x){
    return x>=10?topbit(x/10)*10:1;
}

int main(){
    int cs,lo,hi;
    scanf("%d",&cs);
    for(int no=1;no<=cs;no++){
        scanf("%d%d",&lo,&hi);
        long long ans=0;
        for(int i=lo;i<=hi;i++){
            int x=i,r=topbit(x);
            do{
                if(x>i && x<=hi) ans++;
                x=x%10*r+x/10;
            }while(x!=i);
        }
        printf("Case #%d: %I64d\n",no,ans);
    }
}
