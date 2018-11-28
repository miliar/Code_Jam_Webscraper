#include <iostream>
#include <cmath>
#include <map>
using namespace std;

#define mset(a,x) memset(a,x,sizeof(a))
typedef long long i64;
const int INF=INT_MAX/2;

int S,Q;
map<string,int> no;
int used[101];
char buf[10001];

int main()
{
    freopen("C:\\A-large.in.txt","r",stdin);
    freopen("C:\\A-large.out.txt","w",stdout);
    int T,kcase(0);
    scanf("%d",&T);getchar();
    while(T--){
        mset(used,0);
        scanf("%d",&S);getchar();
        for(int i=0;i<S;i++){
            gets(buf);
            no[string(buf)]=i;
        }
        scanf("%d",&Q);getchar();
        int cnt=0,res=0;
        for(int i=0;i<Q;i++){
            gets(buf);
            int x=no[string(buf)];
            if(!used[x]){
                cnt++;
                if(cnt<S){
                    used[x]=1;
                }
                else {
                    res++;
                    mset(used,0);
                    cnt=1;
                    used[x]=1;
                }
            }
        }
        printf("Case #%d: %d\n",++kcase,res);
    }
}
