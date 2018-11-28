/*
 1185 �ڱ����
 fengyu05
 ״̬ѹ��DP + �������� + DFSԤ���� + �����Լ�֦
**
  1.ȷ��״̬ѹ���ı�ʾ
  2.ȷ��״̬
  3.�ж�����״̬�Ƿ����ת��
  4.ת��
*/
#include<iostream>
#include<algorithm>
#include<cassert>
using namespace std;
int countbit(int x){
	int re=0;
	while(x>0){
		re+=x%2;
		x/=2;
	}return re;
}
#define M 11
const int N=1<<M;
int n,m;
int valid[128][N];//���з���
// valid[x][id]=countbit(id) :����
// valid[x][id]=-1 :������
char map[M];//��ǰ�е�ͼ������DFS
char X[M];
void DFS(int x,int pos){
	if(pos==m){
		int id=0;
		for(int i=0;i<m;i++){
			id=id*2+X[i];
		}
		valid[x][id]=countbit(id);
	}else{
		bool canplace=(map[pos]=='.');
		if(canplace){
			if(pos-1>=0&&X[pos-1]==1) canplace=false;
		}
		if(canplace){
			X[pos]=1;
			DFS(x,pos+1);
		}
		X[pos]=0;
		DFS(x,pos+1);
	}
}
int f[2][N];
int end;
bool safe(int x,int y){// x can behind y
	char map[16]={0};
	int cnt=0;
	while(x>0){
		int id=x%2;
		x/=2;
		if(id==1){
			int a=cnt-1;
			if(a>=0) map[a]=1;
			int b=cnt+1;
			if(b<m) map[b]=1;
		}
		cnt++;
	}
	cnt=0;
	while(y>0){
		int id=y%2;
		y/=2;
		if(id==1&&map[cnt]==1) return false;
		cnt++;
	}
	return true;
}
void solve(){
	int i,j;
	scanf("%d %d\n",&n,&m);
	end=(1<<m);
	memset(valid,-1,sizeof(valid));
	for(i=0;i<n;i++){
		int re=0;
		scanf("%s",map);
		memset(X,0,sizeof(X));
		DFS(i,0);//DFSȷ�����з���
	}
	int _max=*max_element(valid[0],valid[0]+end);
	//
	//assert(*max_element(valid[1],valid[1]+end)==5);
	//
	if(n==1){ 
		printf("%d\n",_max);
		return;
	}
	memset(f[1],0,sizeof(f[1]));
	for(i=0;i<end;i++) if(valid[0][i]>=0){
		f[0][i]=valid[0][i];
	}
	//�������
	for(int cnt=1;cnt<n;cnt++){
		int cur=cnt%2,pre=(cnt-1)%2;
		memset(f[cur],0,sizeof(f[cur]));
			for(j=end-1;j>=0;j--) if(valid[cnt-1][j]>=0){
				//if(f[pre][j]+m/2<_max) continue;//�����Լ�֦
				for(int k=end-1;k>=0;k--) if(valid[cnt][k]>=0){//
					if( safe(k,j) ){
						int tmp=f[pre][j]+valid[cnt][k];
						if(f[cur][k]<tmp){
							if(tmp>_max) _max=tmp;
							f[cur][k]=tmp;							
						}
					}					
				}
			}
	}
	printf("%d\n",_max);
}
int main()
{	
	freopen("t.in", "r", stdin);
	freopen("t.out", "w", stdout);
	int cas;
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++){
		printf("Case #%d: ",ii);
		solve();
	}
	return 0;
}