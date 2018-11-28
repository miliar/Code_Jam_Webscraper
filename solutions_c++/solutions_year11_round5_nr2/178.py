#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
using namespace std;
int a[10002];
using namespace std;
vector<int>rr;
main(){

    int T,t=0,an,i,j,mi,n,x;
    scanf("%d",&T);
    while(T--){
        rr.clear();
        memset(a,0,sizeof(a));
        an=0;
        scanf("%d",&n);
        for(i=1;i<=n;i++)scanf("%d",&x),a[x]++;
        for(i=1;i<=10000;){
            if(a[i]==0){
                i++;
                continue;
            }
            an=mi=0;
            do{
                an++;
                a[i]--;
                if(a[i]&&!mi)mi=i;
                if(a[i]<a[i+1])i++;
                else break;
            }while(1);
            if(!mi)i++;
            else i=mi;
            rr.push_back(an);
        }
        if(rr.size()==0)an=0;
        else
            for(i=1,an=rr[0];i<rr.size();i++)an=min(an,rr[i]);
        printf("Case #%d: %d\n",++t,an);
    }
}
