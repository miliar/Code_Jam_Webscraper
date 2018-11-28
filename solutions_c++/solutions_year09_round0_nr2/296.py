#include<stdio.h>
#include<string.h>

struct Node{
	int x,y;
}que[200000];

int map[111][111];
int n,m;
int visit[111][111];
int id[33];
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
int fa[200000];
int col[200000];
int cn;


int hash(int i,int j){
	return i*m+j;
}

int find(int a){
	if(a==fa[a]) return a;
	return fa[a]=find(fa[a]);
}


void unio(int a,int b){
	int x,y;
	x=find(a);
	y=find(b);
	if(x==y) return ;
	fa[x]=y;
}


void bfs(int aa,int bb){
	int xx,yy;
	Node now,temp;
	int b,e;
	int i,j,k,t;
	b=e=0;
	que[e].x=aa; que[e++].y=bb;
	visit[aa][bb]=1;
	while(e>b){
		now=que[b++];
		i=map[now.x][now.y];
		j=-1;
		for(t=0;t<4;t++){
			xx=now.x+dx[t];
			yy=now.y+dy[t];
			if(xx<0||xx>=n||yy<0||yy>=m) continue;
			if(map[xx][yy]<i){
				i=map[xx][yy];
				j=t;
			}
		}
		if(j==-1){		// is a sink
			if(col[hash(now.x,now.y)]==-1)
				col[hash(now.x,now.y)]=cn++;
		}
		else{
			temp.x=now.x+dx[j];
			temp.y=now.y+dy[j];
			unio(hash(now.x,now.y),hash(temp.x,temp.y));
			if(!visit[temp.x][temp.y]){
				visit[temp.x][temp.y]=1;
				que[e++]=temp;
			}
		}
	}
}




int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca,i,j,k,t;
	scanf("%d",&T);
	ca=0;
	while(T--){
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				scanf("%d",&map[i][j]);
				t=hash(i,j);
				fa[t]=t; col[t]=-1;
			}
		}
		cn=0;
		memset(visit,0,sizeof(visit));
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				if(!visit[i][j]) bfs(i,j);
			}
		}

		memset(id,-1,sizeof(id));
		t=0;
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				k=find(hash(i,j));
				if(id[col[k]]==-1) id[col[k]]=t++;
				visit[i][j]=id[col[k]];
			}
		}
		printf("Case #%d:\n",++ca);
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				printf("%c",visit[i][j]+'a');
				if(j<m-1) printf(" ");
				else printf("\n");
			}
		}
	}
	return 0;

}
