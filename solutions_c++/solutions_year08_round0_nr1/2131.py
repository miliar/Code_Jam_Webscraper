#include "iostream"
#include "cstring"
#include "algorithm"
#include "string"
#include "map"
#include "stdio.h"
#define N 101
#define M 1001
using namespace std;
map<string,int> list;
map<string,int>::iterator it;
int n,m,cnt[M][N];
void flyfire(){
	#ifndef  ONLINE_JUDGE
	#define ONLINE_JUDGE
		freopen("A-large.in","r",stdin);
		freopen("A-large.out","w",stdout);
	#endif
}
int find(int x,int y){
	int i,min,j;
	for(i=0,min=M;i<n;i++)
		if(i!=x&&min>cnt[y][i])
			min=cnt[y][i],j=i;
	return j;
}
int universe(){
	int i,j,k,min;
	char s[N];
	memset(cnt,0,sizeof(cnt));
	for(i=1,min=0;i<=m;i++){
		gets(s);
		k=list[s];
		min=find(-1,i-1);
		for(j=0;j<n;j++){
			if(j!=k)
				cnt[i][j]=cnt[i-1][min]+1<cnt[i-1][j]?cnt[i-1][min]+1:cnt[i-1][j];
			else if(k==min)
				cnt[i][j]=cnt[i-1][find(k,i-1)]+1;
			else
				cnt[i][j]=cnt[i-1][min]+1;
		}
	}
	for(min=M,i=0;i<n;i++)
		if(cnt[m][i]<min)
			min=cnt[m][i];
	return min;
}
int main(){
	flyfire();
	int t,ncase;
	scanf("%d",&t);
	for(ncase=1;ncase<=t;ncase++){
		int i;
		char s[N];
		scanf("%d\n",&n);
		for(i=0;i<n;i++){
			gets(s);
			list[s]=i;
		}
		scanf("%d\n",&m);
		printf("Case #%d: %d\n",ncase,universe());
	}
	return 0;
}