#include <iostream>
using namespace std;
int main(){
    freopen("B-large.in","r",stdin);
	freopen("b-large.out","w",stdout);
    int casenum,n,k,b,t,casei;
    scanf("%d",&casenum);
    for(casei=1;casei<=casenum;casei++){
        int i;
		int ans=0,cur=0;
		int x[100],v[50];
		scanf("%d %d %d %d",&n,&k,&b,&t);
        for(i=0;i<n;i++)scanf("%d",&x[i]);
        for(i=0;i<n;i++)scanf("%d",&v[i]);
        for(i=n-1;i>=0&&cur<k;i--){
            if((b-x[i]) <= v[i]*t){
                cur++;
                continue;
            }
            ans+=k-cur;
        }

        if(cur==k)printf("Case #%d: %d\n",casei,ans);
        else printf("Case #%d: IMPOSSIBLE\n",casei);
    }
//    system("pause");
    return 0;
}

