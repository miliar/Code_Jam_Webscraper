#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<assert.h>
#include<stdarg.h>
#include<time.h>
#include<string>
#include<map>
#include<set>
#include<algorithm>
#include<vector>
using namespace std;
char leet[]="oieastbg";
inline int ton(char c){
    int i;
    for(i=0;i<8;i++)if(leet[i]==c)return i;
    return -1;
}
char in[1010];
bool g[50][50];
int cnt[50];//out-in
int main(){
    int t,cas=1,i,j;
    scanf("%d",&t);
    while(t--){
        int k;
        scanf("%d",&k);
        if(k!=2){
            fprintf(stderr,"not small");
            return 0;
        }
        scanf("%s",in);
        memset(cnt,0,sizeof(cnt));
        memset(g,0,sizeof(g));
        int tc=0;
        for(i=1;in[i];i++){
            int x1=in[i-1]-'a';
            int x2=in[i]-'a';
            g[x1][x2]=1;
            int y1=ton(in[i-1])+26;
            int y2=ton(in[i])+26;
            if(y1>25&&y2>25){
                g[y1][y2]=1;
            }
            if(y1>25){
                g[y1][x2]=1;
            }
            if(y2>25){
                g[x1][y2]=1;
            }
        }
        int a=0,b=0;
        for(i=0;i<50;i++)for(j=0;j<50;j++){
            if(g[i][j]){
                a++;
                cnt[i]++;
                cnt[j]--;
            }
        }
        for(i=0;i<50;i++)if(cnt[i]>0)b+=cnt[i];
        printf("Case #%d: %d\n",cas++,a+1+max(b-1,0));
    }
}

