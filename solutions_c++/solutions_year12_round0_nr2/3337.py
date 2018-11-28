#include<cstdio>

using namespace std;

void solve(){
	int n,m,border; scanf("%d%d%d",&n,&m,&border);
	int ans=0;
	while(n--){
		int sum; scanf("%d",&sum);
		int score1,score2;
		if(sum%3==0){
			score1=sum/3;
			score2=sum/3+(sum==0?0:1);
		}
		else if(sum%3==1){
			score1=sum/3+1;
			score2=sum/3+(sum==1?0:1);
		}
		else{
			score1=sum/3+1;
			score2=sum/3+2;
		}
		if(m>0 && score1<border && border<=score2) m--, score1=score2;
		if(border<=score1) ans++;
	}
	printf("%d\n",ans);
}

int main(){
	int T; scanf("%d",&T);
	for(int t=1;t<=T;t++) printf("Case #%d: ",t), solve();
	return 0;
}
