#include<stdio.h>
#include<string.h>
#include<math.h>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
using namespace std;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int kase;
    scanf("%d",&kase);
    for(int kases=1;kases<=kase;kases++){
        int n,s,p;
        scanf("%d%d%d",&n,&s,&p);

        int ST = p+max(0,p-1)+max(0,p-1);
        //int ED = p+min(10,p+1)+min(10,p+1);

        int st = p+max(0,p-2)+max(0,p-2);
        //int ed = p+min(10,p+2)+min(10,p+2);
        //printf("==%d==\n",st);
        int ans=0;
        while(n--){
            int v;
            scanf("%d",&v);
            if(v>=ST){
                ans++;
            }
            else if(s && v>=st){
                s--;
                ans++;
            }
        }
        printf("Case #%d: ",kases);
        printf("%d\n",ans);
    }
	return 0;
}
