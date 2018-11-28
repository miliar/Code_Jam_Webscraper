#include<iostream>
#include<vector>
#include<queue>

using namespace std;

struct edge
{
	int a,b;
	edge () {}
	edge (int x, int y) { a=x; b=y; }
	int get_else ( int x ) { return x==a ? b : a; }
};

vector< edge > g;
vector< vector< int > > v;
int n,h,w;
int g_size;
bool used [100100];

void add_edge ( int a, int b )
{
	edge ed(a,b);
	g.push_back(ed);
	v[a].push_back(g_size);
	v[b].push_back(g_size);
	++g_size;
}

char ans [110][110];
int inp [110][110];

void bfs ( int vert, char color )
{
	queue < int >  q;
	q.push(vert);
	used[vert]=true;
	ans[vert/w][vert%w]=color;
	int k,i,x,t;
	while(!q.empty())
	{
		x=q.front();
		q.pop();
		k=v[x].size();
		for(i=0;i<k;++i)
		{
			t=g[v[x][i]].get_else(x);
			if(!used[t])
			{
				used[t]=true;
				ans[t/w][t%w]=color;
				q.push(t);
			}
		}

	}
}

void solve()
{
	int i,j;
	int lmin;
	int dir;
	g_size=0;
	g.clear();
	for(i=0;i<h;++i)
		for(j=0;j<w;++j)
		{
			used[i*w+j]=false;
			lmin=1000000000;
			dir=0;
			if(i<h-1 && inp[i+1][j]<inp[i][j] && inp[i+1][j]<=lmin)
			{
				lmin=inp[i+1][j];
				dir=4;
			}
			if(j<w-1 && inp[i][j+1]<inp[i][j] && inp[i][j+1]<=lmin)
			{
				lmin=inp[i][j+1];
				dir=3;
			}
			if(j>0 && inp[i][j-1]<inp[i][j] && inp[i][j-1]<=lmin)
			{
				lmin=inp[i][j-1];
				dir=2;
			}
			if(i>0 && inp[i-1][j]<inp[i][j] && inp[i-1][j]<=lmin)
			{
				lmin=inp[i-1][j];
				dir=1;
			}
			if(dir==1)
				add_edge( (i-1)*w+j,i*w+j );
			if(dir==2)
				add_edge( i*w+j-1,i*w+j );
			if(dir==3)
				add_edge( i*w+j+1, i*w+j );
			if(dir==4)
				add_edge( (i+1)*w+j, i*w+j );
		}
		char color='a';
		for(i=0;i<n;++i)
			if(!used[i])
			{
				bfs(i,color);
				++color;
			}
		for(i=0;i<h;++i)
		{
			for(j=0;j<w;++j)
				cout<<ans[i][j]<<' ';
			cout<<endl;
		}

}

void load()
{
	int k;
	cin>>k;
	int i,j,l;
	for(l=0;l<k;++l)
	{
		cin>>h>>w;
		for(i=0;i<h;++i)
			for(j=0;j<w;++j)
				cin>>inp[i][j];
		n=w*h;
		g.clear();
		v .clear();
		v.resize(n);
		cout<<"Case #"<<l+1<<":\n";
		solve();
	}
}

int main()
{
	freopen("B-large.out","w",stdout);
	load();
	return 0;
}