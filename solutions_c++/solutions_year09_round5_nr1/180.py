#include<iostream>
#include<algorithm>
#include<queue>
#define DEBUG 0
#undef DEBUG
using namespace std;
int n,m;
struct State{
	char s[14][15];
	bool stable;
	int step;
#ifdef DEBUG
	void print(){
		for(int i=1;i<=n;++i)
			cout<<s[i]<<endl;
		cout<<stable<<' '<<step<<endl;
	}
#endif
}state;
const int P=5634637;
bool hash[P],u[14][14];
int box_sum;
const int dx[4]={-1,1,0,0},dy[4]={0,0,-1,1};
bool hash_check(){
#ifdef DEBUG
	cout<<"hash_check in"<<endl;
#endif
	int sum=0;
	for(int i=1;i<=n;++i)
		for(int j=1;j<=m;++j){
			sum+=state.s[i][j];
			sum*=7;
			sum%=P;
		}
#ifdef DEBUG
	cout<<"hash_check out"<<endl;
#endif
	if(hash[sum])
		return false;
	hash[sum]=1;
	return true;
}
int dfs_box(int x,int y){
#ifdef DEBUG
	cout<<"dfs_box in"<<endl;
#endif
	u[x][y]=1;
	int sum=1;
	for(int i=0;i<4;++i)
		if(!u[x+dx[i]][y+dy[i]] && (state.s[x+dx[i]][y+dy[i]]=='o' || state.s[x+dx[i]][y+dy[i]]=='w'))
			sum+=dfs_box(x+dx[i],y+dy[i]);
#ifdef DEBUG
	cout<<"dfs_box out"<<endl;
#endif
	return sum;
}
bool stable_check(){
#ifdef DEBUG
	cout<<"stable check"<<endl;
#endif
	memset(u,0,sizeof(u));
	for(int i=1;i<=n;++i)
		for(int j=1;j<=m;++j)
			if(state.s[i][j]=='o' || state.s[i][j]=='w')
				return dfs_box(i,j)==box_sum;
}
bool finish_check(){
#ifdef DEBUG
	cout<<"finish check"<<endl;
#endif
	for(int i=1;i<=n;++i)
		for(int j=1;j<=m;++j)
			if(state.s[i][j]=='o')
				return false;
	return true;
}
void move(int x,int y,int x2,int y2){
	if(state.s[x][y]=='o')
		state.s[x][y]='.';
	else
		state.s[x][y]='x';
	if(state.s[x2][y2]=='.')
		state.s[x2][y2]='o';
	else
		state.s[x2][y2]='w';
}
int bfs(){
	queue<State> que;
	que.push(state);
	hash_check();
	while(!que.empty()){
		state=que.front();
#ifdef DEBUG
		state.print();
		//system("pause");
#endif
		if(finish_check())
			return state.step;
		que.pop();
		bool old_stable=state.stable;
		++state.step;
		for(int i=1;i<=n;++i)
			for(int j=1;j<=m;++j)
				if(state.s[i][j]=='o' || state.s[i][j]=='w'){
					int k;
					for(k=0;k<2;++k)
						if((state.s[i+dx[k]][j+dy[k]]!='.' && state.s[i+dx[k]][j+dy[k]]!='x'))
							break;
					if(k==2)
						for(k=0;k<2;++k){
							move(i,j,i+dx[k],j);
							if(hash_check()){
								state.stable=stable_check();
								if(old_stable||state.stable)
									que.push(state);
							}
							move(i+dx[k],j,i,j);
						}
					for(k=2;k<4;++k)
						if((state.s[i+dx[k]][j+dy[k]]!='.' && state.s[i+dx[k]][j+dy[k]]!='x'))
							break;
					if(k==4)
						for(k=2;k<4;++k){
							move(i,j,i,j+dy[k]);
							if(hash_check()){
								state.stable=stable_check();
								if(old_stable||state.stable)
									que.push(state);
							}
							move(i,j+dy[k],i,j);
						}
				}
	}
	return -1;
}
int main(){
	int t;
	cin>>t;
	for(int k=1;k<=t;++k){
		cin>>n>>m;
		for(int i=0;i<=n+1;++i)
			for(int j=0;j<=m+1;++j)
				state.s[i][j]='#';
		memset(hash,0,sizeof(hash));
		box_sum=0;
		for(int i=1;i<=n;++i)
			for(int j=1;j<=m;++j){
				char t;
				cin>>t;
				state.s[i][j]=t;
				if(t=='o' || t=='w')
					++box_sum;
			}
#ifdef DEBUG
		cout<<"input finish"<<endl;
#endif
		state.stable=stable_check();
		state.step=0;
		printf("Case #%d: %d\n",k,bfs());
	}
	return 0;
}
