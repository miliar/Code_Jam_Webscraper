#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <queue>
using namespace std;
const int maxn=15;
const int dx[4]={-1,0,1,0};
const int dy[4]={0,1,0,-1};
bool iswall[maxn*maxn];
bool istar[maxn*maxn];
int id[maxn][maxn];
int idx[maxn*maxn],idy[maxn*maxn];
bool tmp[maxn][maxn];
vector<int> pos;
vector<int> tar;
map<__int64,int> hash;
vector<vector<int> > q;
vector<bool> qd;
vector<int> step;
int n,m;
int cnt;

int oppo(int k){
	if (k==0){
		return 2;
	}
	if (k==2){
		return 0;
	}
	if (k==1){
		return 3;
	}
	if (k==3){
		return 1;
	}
}

bool outside(int x,int y){
	return (x<1)||(x>n)||(y<1)||(y>m);
}

bool check(){
	for (int i=1;i<=n;i++){
		for (int j=1;j<=m;j++){
			if (!tmp[i][j]){
				continue;
			}
			bool have=false;
			for (int wy=0;wy<4;wy++){
				int tx=i+dx[wy];
				int ty=j+dy[wy];
				if (outside(tx,ty)){
					continue;
				}
				if (tmp[tx][ty]){
					have=true;
					break;
				}
			}
			if (!have){
				return true;
			}
		}
	}
	return false;
}



vector<int> getlist(){
	vector<int> ans;
	ans.clear();
	for (int i=1;i<=n;i++){
		for (int j=1;j<=m;j++){
			if (!tmp[i][j]){
				continue;
			}
			ans.push_back(id[i][j]);
		}
	}
	return ans;
}

void init(){
	hash.clear();
	scanf("%d%d",&n,&m);
	memset(iswall,false,sizeof(iswall));
	memset(istar,false,sizeof(istar));
	pos.clear();
	tar.clear();
	q.clear();
	qd.clear();
	step.clear();
	int curid=0;
	for (int i=1;i<=n;i++){
		char str[maxn];
		scanf("%s",str);
		for (int j=1;j<=m;j++){
			curid++;
			id[i][j]=curid;
			idx[curid]=i;
			idy[curid]=j;
			if (str[j-1]=='.'){
				continue;
			}
			if (str[j-1]=='#'){
				iswall[curid]=true;
				continue;
			}
			if (str[j-1]=='x'){
				istar[curid]=true;
				tar.push_back(curid);
				continue;
			}
			if (str[j-1]=='o'){
				pos.push_back(curid);
				continue;
			}
			if (str[j-1]=='w'){
				istar[curid]=true;
				tar.push_back(curid);
				pos.push_back(curid);
				continue;
			}
		}
	}
	sort(tar.begin(),tar.end());
	sort(pos.begin(),pos.end());
	cnt=pos.size();
	return;
}

bool target(vector<int> tpos){
	for (int i=0;i<cnt;i++){
		if (tpos[i]!=tar[i]){
			return false;
		}
	}
	return true;
}

__int64 hashfun(vector<int> curpos){
	__int64 ans=0;
	for (int i=0;i<cnt;i++){
		ans*=1000;
		ans+=curpos[i];
	}
	return ans;
}

int bfs(){
	q.push_back(pos);
	qd.push_back(false);
	step.push_back(0);
	hash[hashfun(pos)]=0;
	if (target(pos)){
		return 0;
	}
	int ptr=0;
	while (true){
		if (ptr==q.size()){
			return -1;
		}
		vector<int> curpos=q[ptr];
		bool curstat=qd[ptr];
		int curstep=step[ptr];
		ptr++;
		memset(tmp,false,sizeof(tmp));
		for (int i=0;i<cnt;i++){
			tmp[idx[curpos[i]]][idy[curpos[i]]]=true;
		}
		for (int i=0;i<cnt;i++){
			for (int wy=0;wy<4;wy++){
				int owy=oppo(wy);
				int curx=idx[curpos[i]];
				int cury=idy[curpos[i]];
				int ox=curx+dx[owy];
				int oy=cury+dy[owy];
				if (outside(ox,oy)){
					continue;
				}
				if (iswall[id[ox][oy]]){
					continue;
				}
				if (tmp[ox][oy]){
					continue;
				}
				int tx=curx+dx[wy];
				int ty=cury+dy[wy];
				if (outside(tx,ty)){
					continue;
				}
				if (iswall[id[tx][ty]]){
					continue;
				}
				if (tmp[tx][ty]){
					continue;
				}
				tmp[tx][ty]=true;
				tmp[curx][cury]=false;
				bool danger=check();
				if (curstat&&danger){
					tmp[tx][ty]=false;
					tmp[curx][cury]=true;					
					continue;
				}
				vector<int> tpos=getlist();
				tmp[tx][ty]=false;
				tmp[curx][cury]=true;
				__int64 curfun=hashfun(tpos);
				#ifdef debug
				if (hash.find(curfun)!=hash.end()){
					continue;
				}
				#endif
				if (target(tpos)){
					return curstep+1;
				}
				for (int i=0;i<cnt;i++){
					printf("%d ",tpos[i]);
				}
				puts("");
				hash[curfun]=curstep+1;
				q.push_back(tpos);
				qd.push_back(danger);
				step.push_back(curstep+1);
			}
		}
	}
}

int main(){
	freopen("in.txt","r",stdin);
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++){
		init();
		printf("Case #%d: %d\n",i,bfs());
	}	
	return 0;
}
