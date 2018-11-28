#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<set>
#include<map>
using namespace std;

int t[110];
int f(int k)
{
	if(k%3==0){
		return k/3;
	}
	else if(k%3==1){
		return k/3+1;
	}
	else{
		return k/3+1;
	}
}
bool is(int k,int p)
{
	if(k==0){
		return false;
	}
	if(k%3==0){
		if(k/3+1==p)
			return true;
		else
			return false;
	}
	else if(k%3==1){
		if(k/3+1==p)
			return true;
		else
			return false;
	}
	else{
		if(k/3+2==p)
			return true;
		else
			return false;
	}
}
int main()
{
	int T,n,s,p,ri=1;
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	while(T--){
		scanf("%d%d%d",&n,&s,&p);
		for(int i=0;i<n;i++){
			scanf("%d",&t[i]);
		}
		int ans=0;
		for(int i=0;i<n;i++){
			if(f(t[i])>=p)
				ans++;
			else if(s&&is(t[i],p)){
				ans++;
				s--;
			}
		}
		printf("Case #%d: %d\n",ri++,ans);
	}
}
