#include<iostream>
#include<set>
#include<vector>
#include<queue>
#include<bitset>
using namespace std;
#define display(goal) {cout<<endl;for(int i=0;i<goal.size();i++) cout<<goal[i];cout<<endl;}


char c[15][15];
int n,m;

typedef pair<int,int> node;
typedef vector<node> boxes;
#define x first
#define y second

const int   rule[4][2]={{1,0},{-1,0},{0,1},{0,-1}};
const int unrule[4][2]={{-1,0},{1,0},{0,-1},{0,1}};

ostream&
operator<<(ostream&out,const node&a){
	out<<'('<<a.x<<','<<a.y<<')';
}

node msk(const node&a,const int *b){
	return node(a.x+b[0],a.y+b[1]);
}

bool inside(const node&a){
	if(!((a.x>=0)&&(a.x<n)&&(a.y>=0)&&(a.y<m)))return 0;
	return c[a.x][a.y]!='#';
}


void nim(vector<node>&a){
	sort(a.begin(),a.end());
}

bool safe(const boxes&a){
	static bitset<5>b;
	static queue<node>q;
	b.reset();
	int ans=1;
	q.push(a[0]);
	b[0]=1;
	while(!q.empty()){
		node p=q.front();
		q.pop();
		for(int i=0;i<4;i++){
			node r=msk(p,rule[i]);
			for(int j=1;j<a.size();j++)
				if(b[j]==0&&r==a[j]){
					q.push(r);
					b[j]=1;
					ans++;
				}
		}
	}
	return ans==a.size();
}

boxes start,goal;

void init(){
	start.clear();
	goal.clear();
	scanf("%d%d",&n,&m);
	for(int i=0;i<n;i++)
		scanf("%s",c[i]);
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++){
			if(c[i][j]=='x'||c[i][j]=='w')goal.push_back(node(i,j));
			if(c[i][j]=='o'||c[i][j]=='w')start.push_back(node(i,j));
			if(c[i][j]!='#') c[i][j]='.';
		}
	nim(start);
	nim(goal);
}


void cover(const boxes&a,char b){
		for(int i=0;i<a.size();i++)
			c[a[i].x][a[i].y]=b;
}

int run(){
	set<boxes>hash;
	if(start==goal)return 0;
	queue<pair<boxes,int> > q;
	q.push(make_pair(start,0));
	while(!q.empty()){
		boxes a=q.front().first,c;
		int b=q.front().second;
		q.pop();
		bool flag=safe(a);
		cover(a,'#');
		for(int x=0;x<a.size();x++){
			for(int i=0;i<4;i++){
				c=a;
				c[x]=msk(a[x],unrule[i]);
				if(!inside(c[x]))continue;
				c[x]=msk(a[x],rule[i]);
				if(!inside(c[x]))continue;
				nim(c);
				if(!flag&&!safe(c))continue;
				if(hash.count(c)==0){
					if(c==goal)return b+1;
					hash.insert(c);
					q.push(make_pair(c,b+1));
				}
			}
		}
		cover(a,'.');
	}
	return -1;
}


int main(){
	freopen("inputa.txt","r",stdin);
	freopen("outputa.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int kase=1;kase<=t;kase++){
		init();
		printf("Case #%d: %d\n",kase,run());
	}
}
