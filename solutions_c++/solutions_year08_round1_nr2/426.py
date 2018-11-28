#include<stdio.h>
#include<vector>
using namespace std;

const int MAX = 2001;

struct node
{
	int num;
	int malt;
};

struct custom
{
	int count;
	node s[MAX];
};

int cmp(const void* p1, const void* p2){
	custom pp1 =*((custom *)p1);
	custom pp2 =*((custom *)p2);
	return pp1.count-pp2.count;
}

int cmp1(const void* p1, const void*p2){
	node pp1 =*((node *)p1);
	node pp2 =*((node *)p2);
	return pp1.malt-pp2.malt;

}

custom str[MAX];
int flag[MAX];
int n,m;


bool solve(int i){
	if(i>=m){
		return true;
	}
	for(int j=0;j<str[i].count;j++){ 
		if(flag[str[i].s[j].num]==-1 || (flag[str[i].s[j].num]==str[i].s[j].malt)){
			int old = flag[str[i].s[j].num];
			
			flag[str[i].s[j].num]=str[i].s[j].malt;
			if(solve(i+1)==true)	return true;
			flag[str[i].s[j].num]=old;

		}
	}
	return false;

}

int main(){
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	int c;
	int i,j;
	
	scanf("%d",&c);
	for(int cc=1;cc<=c;cc++){
		scanf("%d",&n);
		scanf("%d",&m);
		for(i=0;i<n;i++)	flag[i]=-1;
		for(i=0;i<m;i++){
			scanf("%d",&str[i].count);
			for(j=0;j<str[i].count;j++){
				scanf("%d%d",&str[i].s[j].num, &str[i].s[j].malt);
				str[i].s[j].num-=1;
			}
			qsort(str[i].s,str[i].count,sizeof(node),cmp1);
		}
		qsort(str,m,sizeof(custom),cmp);

		if(solve(0)==true){
			printf("Case #%d:",cc);
			for(i=0;i<n;i++)	printf(" %d",flag[i]==-1?0:flag[i]);
			printf("\n");
		}else{
			printf("Case #%d: IMPOSSIBLE\n",cc);
		}

	}

	return 0;
}
