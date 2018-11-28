#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
using namespace std;
struct S{
    int pos;
    char type[5];
}s[110];
struct BFS{
    int bpa,bpb,bnow,bstep;
}bfs[1000010]; int w,l;
int T,n,v[110][110][110],f=0;
void enq(int aa,int bb,int nn,int sp){
    if(aa<=0 || aa>100 || bb<=0 || bb>100) return;
    if(v[aa][bb][nn]) return;
    v[aa][bb][nn] = 1;
    bfs[l].bpa = aa;
    bfs[l].bpb = bb;
    bfs[l].bnow = nn;
    bfs[l].bstep = sp;
    l++;
}
int Solve(){
    int now,pa,pb,sp;
    memset(v,0,sizeof(v));
    l=0;
    enq(1,1,0,0);
    for(w=0;w!=l;w++){
	now = bfs[w].bnow;
	pa = bfs[w].bpa;
	pb = bfs[w].bpb;
	sp = bfs[w].bstep;
	if(now==n){
	    return sp;
	}
	if(s[now].type[0]=='O' && s[now].pos==pa){
	    for(int i=-1;i<=1;i++){
		enq(pa,pb+i,now+1,sp+1);
	    }
	}
	if(s[now].type[0]=='B' && s[now].pos==pb){
	    for(int i=-1;i<=1;i++){
		enq(pa+i,pb,now+1,sp+1);
	    }
	}
	for(int i=-1;i<=1;i++){
	    for(int j=-1;j<=1;j++){
		enq(pa+i,pb+j,now,sp+1);
	    }	
	}
    }

}
int main(){
    scanf("%d",&T);
    while(T--){
	scanf("%d",&n);
	for(int i=0;i<n;i++){
	    scanf("%s %d",s[i].type,&s[i].pos);
	}
	printf("Case #%d: %d\n",++f,Solve());
    }
}
