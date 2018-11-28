#include <stdio.h>
#include <string.h>
#include <algorithm>
#define maxn 10010

using namespace std;

char s[maxn][15];
int len[maxn];
char list[30];
int ch[maxn][26];
int ans[110];
int id[maxn];
int tn,cp;
int n,m;
int ansx,ansp;
int cal(int x,int y){
	int res=0;
	for (int i=0;i<len[x];i++)
		if (s[x][i]-'a'==y) res|=1<<i;
	return res;
}
bool cmp(const int &x,const int &y){
	if (len[x]!=len[y]) return len[x]<len[y];
	for (int i=0;i<26;i++){
		if (ch[x][list[i]-'a']!=ch[y][list[i]-'a']) return ch[x][list[i]-'a']<ch[y][list[i]-'a'];
	}
	return 1;
}
void work(int b,int e,int p,int cost){
	if (b==e){
		if (cost<ansx || (cost==ansx && id[b]<ansp)){
			ansx=cost;
			ansp=id[b];
		}
		return;
	}
	int d=list[p]-'a';
	int i,j,k=0;
	for (i=b;i<=e;i++)
		if (ch[id[i]][d]>0) k=1;
	if (!k){
		work(b,e,p+1,cost);
		return;
	}
	for (i=b;i<=e;i=j+1){
		for (j=i;j<e && ch[id[j]][d]==ch[id[j+1]][d];j++);
		if (k && ch[id[i]][d]==0) work(i,j,p+1,cost-1);else work(i,j,p+1,cost);
	}
}
int main(){
	int i,j,k;
	for (scanf("%d",&tn),cp=1;cp<=tn;cp++){
		scanf("%d %d",&n,&m);
		for (i=0;i<n;i++) scanf("%s",s[i]);
		for (i=0;i<n;i++) len[i]=strlen(s[i]);
		for (i=0;i<n;i++)
			for (j=0;j<26;j++) ch[i][j]=cal(i,j);
		for (i=0;i<n;i++) id[i]=i;
		for (i=0;i<m;i++){
			scanf("%s",list);
			sort(id,id+n,cmp);
			ansx=1000;
			for (j=0;j<n;j=k+1){
				for (k=j;k<n-1 && len[id[k+1]]==len[id[k]];k++);
				work(j,k,0,0);
			}
			ans[i]=ansp;
		}
		printf("Case #%d: ",cp);
		for (i=0;i<m-1;i++) printf("%s ",s[ans[i]]);
		printf("%s\n",s[ans[m-1]]);
	}
	return 0;
}