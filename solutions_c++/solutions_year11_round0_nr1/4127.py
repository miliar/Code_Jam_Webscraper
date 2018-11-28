#include<iostream>

using namespace std;

// DFS之后按照结束访问时间反向排序,
// 如果在DFS过程中出现后向边(成环),则无法TOPO
#define N 128
#define INF 1000000000
#define NaN -1

int n,m,pos,mk[N],ord[N]; //ord[1..n]
int mat[N][N];//mat[1..n] NaN for edge not exist
bool topo;

void dfs(int v)
{
	if(mk[v]<0){ topo=false; return ;}
	if(mk[v]>0) return ;
	else mk[v]=-1;
	for(int w=1; topo && w<=n; w++)
		if(mat[v][w]>0) dfs(w);
	ord[pos--]=v; mk[v]=1;
}
void toposort(){
	topo=true; pos=n;
	memset(mk,0, sizeof(mk));
	for(int i=1;topo && i<=n; i++)
		if(!mk[i]) dfs(i);
}
void init(){
	for(int i=1;i<=n;i++)
		for(int j=i+1;j<=n;j++)
			mat[i][j]=mat[j][i]=NaN;
}

int kp;//关键路径长度
int ve[N];//结点最早发生时间 max{ve[i]+mat[i][j]}
int vl[N];//结点最晚发生时间 min{vl[j]-mat[i][j]}

char ob[N];
int lab[N];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int cas, cas_n;
	scanf("%d\n", &cas);
	for(int cas_n=1; cas_n<=cas; cas_n++)
	{

		scanf("%d ", &m);
		//printf("%d\n", m);
		n = m + 1;
		init();
		for(int i=1;i<=m;i++)
		{
			scanf("%c %d ", &ob[i], &lab[i]);
			//printf("%c %d\n", ob[i], lab[i]);
		}
		int past_o_pos = 1;
		int past_b_pos = 1;
		int index_o = -1;
		int index_b = -1;
		for (int i=1;i<=m;i++)
		{
			if(ob[i] == 'O'){
				if(index_o == - 1){
					mat[n][i] = abs(lab[i] - past_o_pos) + 1;
					//printf("%d -> %d:%d\n", n, i, mat[n][i]);
					past_o_pos = lab[i] ;
					index_o = i;
				}else{
					mat[index_o][i] = abs(lab[i] - past_o_pos) + 1;
					//printf("%d -> %d:%d\n", index_o, i, mat[index_o][i]);
					past_o_pos = lab[i];
					index_o = i;
				}

			}else{
				if(index_b == - 1){
					mat[n][i] = abs(lab[i] - past_b_pos) + 1;
					//printf("%d -> %d:%d\n", n, i, mat[n][i]);
					past_b_pos = lab[i] ;
					index_b = i;
				}else{
					mat[index_b][i] = abs(lab[i] - past_b_pos) + 1;
					//printf("%d -> %d:%d\n", index_b, i, mat[index_b][i]);
					past_b_pos = lab[i];
					index_b = i;
				}
			}
		}
		char last_color = ob[1];
		char cur_color;
		for (int i = 2; i<=m ; i++){
			cur_color = ob[i];
			if (last_color != cur_color){
				mat[i-1][i] = 1;
			}
			last_color = cur_color;
		}

		toposort();

		memset(ve,0,sizeof(ve));
		for(int i=2;i<=n;i++){
			int v=ord[i];
			int max=-1;
			for(int j=1;j<i;j++){
				int u=ord[j];
				if(mat[u][v]>0){
					int tmp=ve[u]+mat[u][v];
					if(tmp>max) max=tmp;
				}
			}
			ve[v]=max;
		}
		vl[ord[n]]=kp=ve[ord[n]];
		for(int i=n-1;i>=1;i--){
			int v=ord[i];
			int min=INF;
			for(int j=n;j>i;j--){
				int u=ord[j];
				if(mat[v][u]>0){
					int tmp=vl[u]-mat[v][u];
					if(tmp<min) min=tmp;
				}
			}
			vl[v]=min;
		}
		printf("Case #%d: %d\n", cas_n, vl[m]);
	}
	return 0;
}
