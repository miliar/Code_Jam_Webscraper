#include<iostream>
#include<map>
#include<string>
#include<sstream>
#include<vector>
#include<queue>
using namespace std;
int given[110][110];
int N,M;

struct data
{
	int r,c,a, dir;

	data(int rr,int cc,int aa, int d=100)
	{
		r=rr; c=cc; a=aa; dir=d;
	}
};
int dr[]={-1,0,0,1};
int dc[]={0,-1,1,0};
bool operator<(const data& x,const data& y)
{
	if(x.a!=y.a) return x.a<y.a;
	return x.dir<y.dir;
}
int label[110][110];
vector<data> v;
vector<data> path;
void goback(int num)
{
	for(int i=0;i<path.size();i++) label[path[i].r][path[i].c]=num;
}

void go(int row,int col,int num)
{
	path.clear();
	queue<data> q;
	q.push(data(row,col,given[row][col]));
	while(!q.empty())
	{
		path.push_back(q.front());
		int r=q.front().r, c=q.front().c; 
		q.pop();
		if(label[r][c]!=-1 && label[r][c]!=num)
		{
			goback(label[r][c]);
			break;

		}
		label[r][c]=num;
		vector<data> tmp;
		for(int i=0;i<4;i++)
		{
			int nr=r+dr[i], nc=c+dc[i];
			if(nr<0 || nr>=N || nc<0 || nc>=M || given[nr][nc]>=given[r][c]) continue;
			tmp.push_back(data(nr,nc,given[nr][nc],i));
		}
		if(tmp.size()==0) continue;
		sort(tmp.begin(),tmp.end());
		q.push(tmp[0]);
	}
}

int main()
{
	int t;
	cin>>t;
	int cnum=0;
	while(t--)
	{
		cnum++;
		cin>>N>>M;
		v.clear();
		for(int i=0;i<N;i++) for(int j=0;j<M;j++) cin>>given[i][j], v.push_back(data(i,j,given[i][j]));
		memset(label,-1,sizeof label);
		sort(v.rbegin(),v.rend());
		int cnt=0;
		for(int i=0;i<v.size();i++) if(label[v[i].r][v[i].c]==-1)
		{
			cnt++;
			go(v[i].r,v[i].c,cnt);
		}
		map<int,char> mp;
		char now='a';
		for(int i=0;i<N;i++) for(int j=0;j<M;j++) if(!mp.count(label[i][j]))
		{
			mp[label[i][j]]=now;
			now++;
		}
		cout<<"Case #"<<cnum<<":"<<endl;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				if(j) cout<<' ';
				cout<<mp[label[i][j]];
			}
			cout<<endl;
		}

	}
}


