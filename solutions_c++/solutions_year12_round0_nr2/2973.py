#include<cstdio>
#include<cstring>
#include<cmath>
#include<queue>
#include<stack>
#include<map>
#include<algorithm>
using namespace std;

int a,b,c;
int ans;
int p[105];

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int Case;
    int h=1;
    scanf("%d",&Case);
    while(Case--) {
        ans=0;
        int ans1=0,ans2=0;
        scanf("%d%d%d",&a,&b,&c);
        int temp1=c*3-2;
        int temp2=c*3-4;
        if(temp1<0) temp1=0;
        if(temp2<0) temp2=0;
        for(int i=0;i<a;i++) {
                scanf("%d",&p[i]);
        }
        for(int i=0;i<a;i++) {
                if(p[i]>=temp1) {
                                ans1++;
                }
                else if(p[i]<temp1&&p[i]>=temp2) {
                                ans2++;
                }
                if(p[i]==0&&temp2==0&&c!=0) {
                                ans2--;
                }
                                
        }
        if(ans2>=b)
                ans=ans1+b;
        else
                ans=ans1+ans2;
        printf("Case #%d: %d\n",h++,ans);
    }
    return 0;
}
