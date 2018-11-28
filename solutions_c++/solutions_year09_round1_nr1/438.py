#include <stdio.h>
#include <string.h>
const int SIZE = 1000;
const int BASE = 11;
const int INF = 1<<25;
const int MARK = 1<<BASE;
int dp[BASE][SIZE];
bool tmp[SIZE];
bool used[BASE];
void init();
bool check(int ,int );
int small(int ,int);
int work();
int mem[MARK];
int mkmark(){
	int i;
	int ret=0;
	for (i=0;i<BASE;i++){
		if (used[i])
			ret|=(1LL<<i);
	}
	return ret;
}
int main(){
	//freopen("../../dat.in","r",stdin);
	memset(dp,-1,sizeof(dp));
	memset(mem,-1,sizeof(mem));
	int cas;
	scanf("%d",&cas);
	int i;
	for (i=1;i<=cas;i++){
		init();
		int ans = work();
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
int work(){
	int ind = mkmark();
	if (mem[ind]!=-1){
		return mem[ind];
	}
	int i,j;
	for (i=2;i<INF;i++){
		bool ok=true;
		for (j=2;j<BASE;j++){
			if (used[j]){
				memset(tmp,false,sizeof(tmp));
				if (!check(i,j)){
					ok=false;
					break;
				}	
			}
		}
		if (ok){
			mem[ind]=i;
			return i;
		}
	}
}
void init(){
	memset(used,false,sizeof(used));
	int pos;
	char ch;
	while (true){
		scanf("%d",&pos);
		used[pos]=true;
		if (scanf("%c",&ch)==EOF)
			break;
		if (ch=='\n')
			break;
	}
}
int small(int num,int base){
	int sum=0;
	while (num>0){
		int pos= num%base;
		sum+=(pos*pos);
		num/=base;
	}
	return sum;
}
bool check(int num,int base){
	if (num==1){
		return (dp[base][num]=1);
	}
	if (num<SIZE){
		if(dp[base][num]!=-1){
			return dp[base][num];
		}
		if (tmp[num]){
			return (dp[base][num]=0);
		}else{
			tmp[num]=true;
			int next = small(num,base);
			return (dp[base][num]=check(next,base));
		}
		
	}else{
		int next = small(num,base);
		return check(next,base);
	}
		
}