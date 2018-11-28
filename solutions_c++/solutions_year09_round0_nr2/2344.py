#include<iostream>
#include<vector>
#include<queue>

using namespace std;

struct zibil
{
	int a,b;
	zibil () {}
	zibil (int x, int y) { a=x; b=y; }
	int get_else ( int x ) { return x==a ? b : a; }
};

vector< zibil > graph;
vector< vector< int > > v;
int n,h,w;
int graph_size;
bool used [100100];

void add_zibil ( int a, int b )
{
	zibil ed(a,b);
	graph.push_back(ed);
	v[a].push_back(graph_size);
	v[b].push_back(graph_size);
	++graph_size;
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
			t=graph[v[x][i]].get_else(x);
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
	graph_size=0;
	graph.clear();
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
				add_zibil( (i-1)*w+j,i*w+j );
			if(dir==2)
				add_zibil( i*w+j-1,i*w+j );
			if(dir==3)
				add_zibil( i*w+j+1, i*w+j );
			if(dir==4)
				add_zibil( (i+1)*w+j, i*w+j );
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


int main()
{
	freopen("answer.txt","w",stdout);
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
		graph.clear();
		v .clear();
		v.resize(n);
		cout<<"Case #"<<l+1<<":\n";
		solve();
	}
	return 0;
}