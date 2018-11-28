#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<vector>
using namespace std;
char in[110][110];
int r,c;
inline int f(int x,int y){return (x+r)%r*c+(y+c)%c;}
inline int val(int i,int j,int dir){
    if(in[i][j]=='-'){
	if(dir)return f(i,j-1);
	else return f(i,j+1);
    }else if(in[i][j]=='|'){
	if(dir)return f(i-1,j);
	else return f(i+1,j);
    }else if(in[i][j]=='/'){
	if(dir)return f(i-1,j+1);
	else return f(i+1,j-1);
    }else if(in[i][j]=='\\'){
	if(dir)return f(i-1,j-1);
	else return f(i+1,j+1);
    }
}
vector<int> ed[11000];
vector<int> ine[11000];
bool del[11000],deld[11000];
inline void dd(vector<int>& x,int ii){
    int n=x.size(),i;
    for(i=0;i<n;i++)if(x[i]==ii)break;
    if(n==1){
	x.clear();
	return;
    }
    if(i!=n-1)swap(x[i],x[n-1]);
    x.pop_back();
}
int rr[11000];
int pre[21000];
inline int find(int x){return pre[x]==x?x:pre[x]=find(pre[x]);}
inline void unions(int x,int y){x=find(x);y=find(y);if(x!=y)pre[x]=y;}
int main(){
    int t,cas=1,i;
    scanf("%d",&t);
    rr[0]=1;
    for(i=1;i<=10000;i++)rr[i]=(rr[i-1]*2)%1000003;
    while(t--){
	int j,k;
	scanf("%d%d",&r,&c);
	for(i=0;i<r;i++)scanf("%s",in[i]);
	memset(del,0,sizeof(del));
	memset(deld,0,sizeof(deld));
	for(i=0;i<r*c;i++){ed[i].clear();ine[i].clear();}
	for(i=0;i<r;i++){
	    for(j=0;j<c;j++){
		int x=f(i,j);
		for(k=0;k<2;k++){
		    ed[x].push_back(val(i,j,k));
		    ine[val(i,j,k)].push_back(x);
		}
	    }
	}
	bool f=1;
	int ans=-1;
	while(f){
	    f=0;
	    for(i=0;i<r*c;i++){
		if(!deld[i]){
		    if(ine[i].size()==0)goto out;
		    if(ine[i].size()==1){
			dd(ed[ine[i][0]],i);
			deld[i]=1;
			f=1;
		    }
		}
		if(!del[i]){
		    if(ed[i].size()==0)goto out;
		    if(ed[i].size()==1){
			dd(ine[ed[i][0]],i);
			del[i]=1;
			f=1;
		    }
		}
	    }
	}
	ans=0;
	for(i=0;i<2*r*c;i++)pre[i]=i;
	for(i=0;i<r*c;i++)if(!del[i]){
	    for(j=0;j<ed[i].size();j++){
		int y=ed[i][j];
		unions(y+r*c,i);
	    }
	}
	for(i=0;i<r*c;i++)if(!deld[i]){
	    for(j=0;j<ine[i].size();j++){
		int y=ine[i][j];
		unions(y,i+r*c);
	    }
	}
	for(i=0;i<r*c;i++){
	    if(!del[i]&&pre[i]==i)ans++;
	    if(!deld[i]&&pre[i+r*c]==i+r*c)ans++;
	}
out:;
	printf("Case #%d: %d\n",cas++,ans==-1?0:rr[ans]);
    }
}

