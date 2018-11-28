#include<cstdio>
#include<cstring>
using namespace std;
#define abs(x) ((x)<0?-(x):(x))
#define max(x,y) ((x)>(y)?(x):(y))
int t,n,i,j,cost_t,l;
int pos[100],cur[100];
char c;
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&t);
	for(l=1;l<=t;l++){
		scanf("%d",&n);
		cost_t=0;
		pos['O']=pos['B']=1;
		cur['O']=cur['B']=0;
		for(i=1;i<=n;i++){
			while(c=getchar(),c!='O' && c!='B');
			scanf("%d",&j);
			cur[c]+=abs(pos[c]-j);
			pos[c]=j;
			cur[c]=max(cur['O'],cur['B'])+1;
		}
		printf("Case #%d: %d\n",l,max(cur['O'],cur['B']));
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
