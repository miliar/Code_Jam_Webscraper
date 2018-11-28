#include<stdio.h>
#include<string.h>
#include<math.h>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
using namespace std;
const int maxn = 2000001;
vector<int> adj[maxn];
int now=1;
int l=1;
void gen(int k){
    int t=k;
    for(int i=1;i<=l;i++){
        int c = t % 10;
        t/=10;
        t+=c*now;
        if(t>k)adj[k].push_back(t);
    }
}
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    for(int i=1;i<=2000000;i++){
        if(10*now<=i){
            now*=10;
            l++;
        }
        gen(i);
        sort(adj[i].begin(),adj[i].end());
    }
    int kase;
    scanf("%d",&kase);
    for(int kases=1;kases<=kase;kases++){
        int a,b;
        scanf("%d%d",&a,&b);
        int ans=0;
        for(int i=a;i<=b;i++)
            for(int j=0;j<adj[i].size();j++)
                if(adj[i][j]<=b){
                    ans++;
                    if(j && adj[i][j]==adj[i][j-1])ans--;
                    //printf("%d %d\n",i,adj[i][j]);
                }else{
                    break;
                }
        printf("Case #%d: ",kases);
        printf("%d\n",ans);
    }
	return 0;
}
