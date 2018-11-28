#include<cstdio>
#include<algorithm>

using std::sort;

int t,n,s,p,c,i;
int score[100];
int ans;

bool judge(const int s,const bool ex,const int m){
	if(s<m)return false;
	int add = ex ? 4 : 2;
	return ((s+add)/3)>=m;
}

int main(){
	//freopen("B.in","r",stdin);
	//freopen("B.out","w",stdout);
	scanf("%d",&t);
	for(c=1;c<=t;c++){
		scanf("%d%d%d",&n,&s,&p);
		ans=0;
		for(i=0;i<n;i++){
			scanf("%d",score+i);
		}
		sort(score,score+n);
		for(i=0;i<n;i++){
			if(s>0){
				if(judge(score[i],true,p)){
					ans++;
					s--;
				}
				continue;
			}
			if(judge(score[i],false,p))ans++;
			
		}
		printf("Case #%d: %d\n",c,ans);
	}
	return 0;
}
