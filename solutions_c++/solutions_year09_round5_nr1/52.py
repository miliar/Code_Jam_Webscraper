#include<iostream>
#include<vector>
#include<string>
#include<cmath>
#include<algorithm>
#include<sstream>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
struct State{
	int x[5],y[5],depth;
	bool danger;
};
const int maxh=1<<22;
bool u[maxh];
State ht[maxh],queue[maxh/2],st,en;
int p,q,found;
int n0,n1,ti,ca,n,m;
char g[20][20];
bool ok[14][14];
bool gx[5][5];
bool isDanger(State s){
	memset(gx,0,sizeof(gx));
	int i,j,k;
	fr(i,0,n0-1)
		fr(j,i+1,n0-1)
			if(abs(s.x[i]-s.x[j])+abs(s.y[i]-s.y[j])==1)
				gx[j][i]=gx[i][j]=true;
	fr(i,0,n0-1)
		gx[i][i]=true;
	fr(k,0,n0-1)
		fr(i,0,n0-1)
			fr(j,0,n0-1)
				if(gx[i][k]&&gx[k][j])
					gx[i][j]=true;
	fr(i,0,n0-1)
		fr(j,0,n0-1)
			if(!gx[i][j])
				return true;
	return false;
}
int cal(State r){
	int value=0,j;
	fr(j,0,n0-1)
		value=(value*511+r.x[j]*51+r.y[j])&(maxh-1);
	return value;
}
bool same(State a,State b){
	int i;
	fr(i,0,n0-1)
		if(a.x[i]!=b.x[i]||a.y[i]!=b.y[i])
			return false;
	return true;	
}
int hash(State r){
	int i=cal(r);
	while(u[i]&&!same(r,ht[i]))
		i=(i+1)&(maxh-1);
	ht[i]=r;
	return i;
}
void transform(State &s){
	int i,j;
	fr(i,0,n0)
		fr(j,i+1,n0-1)
			if(s.x[i]>s.x[j]||s.x[i]==s.x[j]&&s.y[i]>s.y[j]){
				swap(s.x[i],s.x[j]);
				swap(s.y[i],s.y[j]);
			}
}
bool isFinal(State s){
	int i;
	fr(i,0,n0-1)
		if(s.x[i]!=en.x[i]||s.y[i]!=en.y[i])
			return false;
	return true;
}
void add(State s){
	int w=hash(s);
	if(u[w])
		return;
	u[w]=true;
	queue[++q]=s;
	if(isFinal(s))
		found=q;
}
void extend(State s){
	memset(ok,true,sizeof(ok));
	int i,j;
	fr(i,0,n+1)
		fr(j,0,m+1)
			if(g[i][j]=='#')
				ok[i][j]=false;
	fr(i,0,n0-1)
		ok[s.x[i]][s.y[i]]=false;
	State t;
	fr(i,0,n0-1){
		if(ok[s.x[i]][s.y[i]-1]&&ok[s.x[i]][s.y[i]+1]){
			t=s;
			t.y[i]++;
			t.danger=isDanger(t);
			transform(t);
			t.depth=s.depth+1;
			if(!t.danger||!s.danger)
				add(t);
			t=s;
			t.y[i]--;
			t.danger=isDanger(t);
			transform(t);
			t.depth=s.depth+1;
			if(!t.danger||!s.danger)
				add(t);
		}
		if(ok[s.x[i]-1][s.y[i]]&&ok[s.x[i]+1][s.y[i]]){
			t=s;
			t.x[i]++;
			t.danger=isDanger(t);
			transform(t);
			t.depth=s.depth+1;
			if(!t.danger||!s.danger)
				add(t);
			t=s;
			t.x[i]--;
			t.danger=isDanger(t);
			transform(t);
			t.depth=s.depth+1;
			if(!t.danger||!s.danger)
				add(t);
		}
	}
}
int BFS(State s){
	memset(u,found=q=0,sizeof(u));
	p=1;
	for(add(s);p<=q&&found==0;p++)
		extend(queue[p]);
	return found;
}
void init(){
	int i,j;
	cin>>n>>m;
	memset(g,'#',sizeof(g));
	n0=n1=0;
	char s[20];
	fr(i,1,n){
		scanf("%s",s+1);
		fr(j,1,m){
			g[i][j]=s[j];
			if(g[i][j]=='o'||g[i][j]=='w'){
				st.x[n0]=i;
				st.y[n0++]=j;
			}
			if(g[i][j]=='x'||g[i][j]=='w'){
				en.x[n1]=i;
				en.y[n1++]=j;
			}
		}
	}
	st.danger=en.danger=false;
	transform(st);
	transform(en);
}
void work(){
	st.depth=0;
	int ans=BFS(st);
	if(ans==0)
		printf("-1\n");
	else
		printf("%d\n",queue[ans].depth);
}
int main(){
	freopen("a2.in","r",stdin);
	freopen("a2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		init();
		printf("Case #%d: ",ti);
		work();
	}
}