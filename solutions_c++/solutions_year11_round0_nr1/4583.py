#include <cstdio>
#include <iostream>
#include <queue>
using namespace std;

class Node{
public:
	int x,y,k;
	Node(){}
	Node(int x,int y,int k):x(x),y(y),k(k){}
};

queue<Node> t;
const int N=100+2;
const int INF=(1<<30);
int d[N][N][N],a[N];
char col[N];
void init(int n,int m[2]){
	int i,j,k;
	while(!t.empty()) t.pop();
	for(i=0;i<=m[0];i++)
		for(j=0;j<=m[1];j++)
			for(k=0;k<=n;k++)
				d[i][j][k]=INF;
}

int dx[]={-1,0,1};
void relax(int x,int y,int k,int r){
	if(d[x][y][k]>r){
		d[x][y][k]=r;
		t.push(Node(x,y,k));
	}
}

void solve(int case_num){
	
	int n,i,m[2],j,k,x,y;
	m[0]=0;m[1]=0;
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf(" %c%d",&col[i],&a[i]);
		a[i]--;
		if(col[i]=='O') col[i]=0;
		else col[i]=1;
		m[col[i]]=max(m[col[i]],a[i]);
		
	}
	init(n,m);
	
	d[0][0][0]=0;
	t.push(Node(0,0,0));
	
	Node e;
	while(!t.empty()){
		e=t.front();
		//cerr<<e.x<<" "<<e.y<<" "<<e.k<<endl;
		t.pop();
		if(e.k==n){
			printf("Case #%d: %d\n",case_num,d[e.x][e.y][e.k]);
			break;
		}
		for(i=0;i<3;i++){
			x=e.x+dx[i];
			if(x<0||x>m[0]) continue;
			for(j=0;j<3;j++){
				y=e.y+dx[j];
				if(y<0||y>m[1]) continue;
				k=e.k;
				if((x==e.x && col[k]==0 && a[k]==x)||(y==e.y && col[k]==1 && a[k]==y))
					k++;
				relax(x,y,k,d[e.x][e.y][e.k]+1);
			}
		}
	}
	
	
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int t,i;
	scanf("%d",&t);
	for(i=0;i<t;i++)
		solve(i+1);
	return 0;
}
