#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>

#define maxn 111
#define maxm 1111
#define maxnheap 2222222
#define maxC 1000000000

using namespace std;

int test,n,m,nheap,res;
int a[maxn];
int b[maxn];
string c[maxm];
int d[maxn][maxn][maxn];
int pos[maxn][maxn][maxn];
struct list {
	int i,j,k;
};
list heap[maxnheap];
int rear,front;
list Queue[maxnheap];
bool fr[maxn][maxn][maxn];
int path[]={0,-1,1};

void input(){
	int i,j,v,t;
	string s,p;
	getline(cin,s);
	m=0;
	t=0;
	i=0;
	while (i<s.length()){
		if (s[i]==' '){
			i++;
			continue;
		}
		p="";
		for (j=i;j<s.length();j++)
			if (s[j]!=' '){
				p=p+s[j];
				v=j;
			}else break;
		t++;
		if (t==1) n=atoi(p.c_str()); else{
			m++;
			c[m]=p;
		}
		i=v+1;
	}
	n=0;
	for (i=1;i<=m;i++)
		if (i%2==1){
			n++;
			if (c[i]=="O") a[n]=1; else a[n]=2;
			b[n]=atoi(c[i+1].c_str());
		}
}

bool ok(int u,int v){
	int d1,d2;
	d1=d[heap[u].i][heap[u].j][heap[u].k];
	d2=d[heap[v].i][heap[v].j][heap[v].k];
	if (d1<d2) return true; else return false;
}

void swap(int u,int v){
	list t;
	t=heap[u];
	heap[u]=heap[v];
	heap[v]=t;
	pos[heap[u].i][heap[u].j][heap[u].k]=u;
	pos[heap[v].i][heap[v].j][heap[v].k]=v;
}

void up(int node){
	int c;
	if (node==1) return;
	c=node/2;
	if (ok(node,c)){
		swap(node,c);
		up(c);
	}
}

void down(int node){
	int c;
	if (2*node>nheap) return;
	c=2*node;
	if ((c<nheap)&&(ok(c+1,c))) c++;
	if (!ok(c,node)) return;
	swap(node,c);
	down(c);
}

void push(int i,int j,int k){
	nheap++;
	heap[nheap].i=i;
	heap[nheap].j=j;
	heap[nheap].k=k;
	pos[i][j][k]=nheap;
	up(nheap);
}

void pop(int node){
	heap[node]=heap[nheap];
	pos[heap[node].i][heap[node].j][heap[node].k]=node;
	nheap--;
	up(node);
	down(node);
}

void init_heap(){
	int i,j,k;
	memset(pos,0,sizeof(pos));
	for (i=0;i<=n;i++)
		for (j=1;j<=100;j++)
			for (k=1;k<=100;k++)
				d[i][j][k]=maxC;
	nheap=0;
	d[0][1][1]=0;
	push(0,1,1);
}

void update(int i,int j,int k,int ii,int jj,int kk){
	if (d[ii][jj][kk]>d[i][j][k]+1){
		d[ii][jj][kk]=d[i][j][k]+1;
		if (pos[ii][jj][kk]==0) push(ii,jj,kk); else
			up(pos[ii][jj][kk]);
	}
}

void process(){
	int i,j,k,u,v,jj,kk;
	while (nheap>0){
		i=heap[1].i;
		j=heap[1].j;
		k=heap[1].k;
		pop(1);
		if (i==n){
			res=d[i][j][k];
			break;
		}
		for (u=0;u<3;u++)
			for (v=0;v<3;v++){
				jj=j+path[u];
				kk=k+path[v];
				if ((jj>=1)&&(jj<=100)&&(kk>=1)&&(kk<=100))
					update(i,j,k,i,jj,kk);
			}
		if ((a[i+1]==1)&&(j==b[i+1]))
			for (v=0;v<3;v++){
				kk=k+path[v];
				if ((kk>=1)&&(kk<=100))
					update(i,j,k,i+1,j,kk);
			}
		if ((a[i+1]==2)&&(k==b[i+1]))
			for (u=0;u<3;u++){
				jj=j+path[u];
				if ((jj>=1)&&(jj<=100))
					update(i,j,k,i+1,jj,k);
			}
	}
}

void push_queue(int i,int j,int k,int w){
	front++;
	Queue[front].i=i;
	Queue[front].j=j;
	Queue[front].k=k;
	d[i][j][k]=w;
	fr[i][j][k]=false;
}

void BFS(){
	int i,j,k,u,v,w,jj,kk;
	memset(fr,true,sizeof(fr));
	rear=0;
	front=0;
	d[0][1][1]=0;
	push_queue(0,1,1,0);
	res=maxC;
	while (rear!=front){
		rear++;
		i=Queue[rear].i;
		j=Queue[rear].j;
		k=Queue[rear].k;
		if (i==n){
			res=min(res,d[i][j][k]);
			continue;
		}
		w=d[i][j][k]+1;
		for (u=0;u<3;u++)
			for (v=0;v<3;v++){
				jj=j+path[u];
				kk=k+path[v];
				if ((jj>=1)&&(jj<=100)&&(kk>=1)&&(kk<=100))
					if (fr[i][jj][kk])
						push_queue(i,jj,kk,w);
			}
		if ((a[i+1]==1)&&(j==b[i+1]))
			for (v=0;v<3;v++){
				kk=k+path[v];
				if ((kk>=1)&&(kk<=100))
					if (fr[i+1][j][kk])
						push_queue(i+1,j,kk,w);
			}
		if ((a[i+1]==2)&&(k==b[i+1]))
			for (u=0;u<3;u++){
				jj=j+path[u];
				if ((jj>=1)&&(jj<=100))
					if (fr[i+1][jj][k])
						push_queue(i+1,jj,k,w);
			}
	}
}

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	scanf("%d\n",&test);
	int i;
	for (i=1;i<=test;i++){
		input();
		init_heap();
		//process();
		BFS();
		cout<<"Case #"<<i<<": "<<res<<"\n";
	}
}
