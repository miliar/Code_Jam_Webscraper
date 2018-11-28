#include <iostream>
using namespace std;
int res[2000000],curr,n,h,tree[3000000],l,r;
void create_tree(){
	for(h=1;h<n;h*=2);
	memset(tree,0,sizeof(tree));
	for(int i=h;i<h+n;i++)tree[i]=1;
	for(int i=h-1;i>=1;i--)tree[i]=tree[i*2]+tree[i*2+1];
}
int find(int x,int y,int nr){
	if( l<=x && y<=r )return tree[nr];
	int ret=0,s=(x+y)/2;
	if( max(l,x)<=min(r,s))ret+=find(x,s,nr*2);
	if( max(l,s+1)<=min(r,y))ret+=find(s+1,y,nr*2+1);
	return ret;
}
int pocz(int ile,int nr){
	tree[nr]--;
	if(nr>=h)return nr-h;
	if(tree[nr*2]>=ile)return pocz(ile,nr*2);
	else return pocz(ile-tree[nr*2],nr*2+1);
}
void solve(int y){
	int x=(y)%(n-y)+1;
	l=curr+1;r=n-1;
	int ret=find(0,h-1,1);
	if( ret >= x ){
		curr=pocz(n-y-ret+x,1);
	}else{
		x-=ret;
		curr=pocz(x,1);
	}
}
int main(){
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++){
		memset(res,-1,sizeof(res));
		scanf("%d",&n);
		create_tree();
		curr=-1;
		for(int i=0;i<n;i++){
			solve(i);
			res[curr]=i+1;
		}
		int k;
		printf("Case #%d: ",test);
		scanf("%d",&k);
		for(int i=0;i<k;i++){
			int x;
			scanf("%d",&x);
			printf("%d ",res[x-1]);
		}
		printf("\n");
	}
	return 0;
}
