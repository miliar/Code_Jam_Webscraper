#include <stdio.h>
#include <algorithm>

#define INF 1999999999

using namespace std;

struct Node{
	int a,b;
	bool operator<(const Node &o)const{
		return b<o.b;
	}
};

int n;
bool isGet[1005];
Node node[1005];
int ans,nowStar,now;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j;
    int zz,xx;
    scanf("%d",&xx);
    for(zz=1;zz<=xx;zz++){
        scanf("%d",&n);
        for(i=1;i<=n;i++){
            scanf("%d%d",&node[i].a,&node[i].b);
            isGet[i]=0;
        }
        //printf("\n");
        sort(node+1,node+n+1);/*
        for(i=1;i<=n;i++){
        	printf("%d %d\n",node[i].a,node[i].b);
        }*/
        node[n+1].b=INF;
        ans=0;
        nowStar=0;
        now=1;
        bool isChange=1;
        while(isChange){
            isChange=0;
            while(nowStar>=node[now].b){
                if(isGet[now]){
                    nowStar++;
                }else{
                    nowStar+=2;
                }
                ans++;
                now++;
                isChange=1;
            }
            //printf("%d %d %d",now,ans,nowStar);
            for(i=n;i>=now;i--){
            	if(nowStar>=node[i].a && !isGet[i]){
            		isGet[i]=1;
            		nowStar++;
            		isChange=1;
            		ans++;
            		break;
            	}
            }
            //printf("ans%d i%d ns%d\n",ans,i,nowStar);
        }
    	printf("Case #%d: ",zz);
    	if(now!=n+1){
    		printf("Too Bad\n");
    	}else{
    	    printf("%d\n",ans);
    	}
    }
	return 0;
}
/*
1
8
8 12
12 14
11 15
0 5
4 9
0 2
1 5
8 9

4
2
0 1
0 2
3
2 2
0 0
4 4
1
1 1
5
0 5
0 1
1 1
4 7
5 6
*/
