#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<set>
#include<map>
#include<deque>
#include<functional>
using namespace std;

const int maxn=1024;
const int inf=1000002;
int n;
int h[maxn];
int w[maxn];
int flag[maxn];
int mark[maxn][maxn];
int minh,maxh,minw,maxw;

void input()
{
	int i;
	char s[100];
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d%d",&h[i],&w[i]);
		scanf("%s",&s);
		if(s[0]=='N'){
			scanf("%s",&s);
			flag[i]=0;
		}else{
			flag[i]=1;
		}
	}
}

bool check2(int h1,int w1,int h2,int w2)
{
	int i;

	for(i=0;i<n;i++) if(flag[i]==0){
		if(h1<=h[i] && h[i]<=h2 && w1<=w[i] && w[i]<=w2) return false;
	}
	return true;
}

int check(int x,int y)
{
	int i,j,h1,h2,w1,w2;

	for(i=0;i<n;i++){
		if(x==h[i] && y==w[i]){
			if(flag[i]==0) return -1;
			return 1;
		}
	}
	if(minh<=x && x<=maxh && minw<=y && y<=maxw) return 1;
	h1=min(minh,x);
	h2=max(maxh,x);
	w1=min(minw,y);
	w2=max(maxw,y);
	if(!check2(h1,w1,h2,w2)) return -1;
	
	return 0;
}

void solve()
{
	int i,j,x,y,h1,h2,w1,w2,ans,k,m;
	memset(mark,0,sizeof(mark));
	minh=minw=inf;
	maxh=maxw=0;
	for(i=0;i<n;i++){
		if(flag[i]==1){
			if(h[i]<minh) minh=h[i];
			if(h[i]>maxh) maxh=h[i];
			if(w[i]<minw) minw=w[i];
			if(w[i]>maxw) maxw=w[i];
		}
	}
	scanf("%d",&m);
	for(k=0;k<m;k++){
		scanf("%d%d",&x,&y);
		
		ans=check(x,y);
		if(ans==0){
			printf("UNKNOWN\n");
		}else if(ans<0){
			printf("NOT BIRD\n");
		}else{
			printf("BIRD\n");
		}
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int i,T;
	scanf("%d",&T);
	for(i=1;i<=T;i++){
		input();
		printf("Case #%d:\n",i);
		solve();
	}
	return 0;
}
