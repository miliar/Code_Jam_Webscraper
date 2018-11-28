#include <fstream>
#include <vector>
#include <queue>


using namespace std;

ifstream fin("B-small.in");
ofstream fout("B-small.out");

int cur=97;
int h,w;
vector< vector<int> >map;
vector< vector<int> >path;
vector< vector<int> >res;
vector< pair<int,int>>sicks;

void input()
{
	int i,j;
	fin>>h>>w;
	map.resize(h);
	path.clear();
	path.resize(h);
	res.resize(h);
	sicks.clear();
	for(i=0;i<h;i++)
	{
		map[i].resize(w);
		path[i].resize(w);
		res[i].resize(w);
		for(j=0;j<w;j++)
			fin>>map[i][j];
	}
	cur=97;
}

void get_path(int y,int x)
{
	int mi=99999,cur=map[y][x],res=0;
    if(y<h-1 && map[y+1][x]<cur && mi>=map[y+1][x])
	{
		mi=map[y+1][x];
		path[y][x]=4;
	}
	if(x<w-1 && map[y][x+1]<cur && mi>=map[y][x+1])
	{
		mi=map[y][x+1];
		path[y][x]=3;
	}
	if(x>0 && map[y][x-1]<cur && mi>=map[y][x-1])
	{
		mi=map[y][x-1];
		path[y][x]=2;
	}
	if(y>0 && map[y-1][x]<cur && mi>=map[y-1][x])
	{
		mi=map[y-1][x];
		path[y][x]=1;
	}
}

void get_path()
{
	int i,j;
	for(i=0;i<h;i++)
	for(j=0;j<w;j++)
		get_path(i,j);
}


bool check_sick(int y,int x)
{
	int cur=map[y][x];
	if(y>0 && map[y-1][x]<cur)return false;
	if(x>0 && map[y][x-1]<cur)return false;
	if(y<h-1 && map[y+1][x]<cur)return false;
	if(x<w-1 && map[y][x+1]<cur)return false;
	return true;
}


void output(int test)
{
	fout<<"Case #"<<test<<":"<<endl;
	int i,j;
	for(i=0;i<h;i++)
	{
		for(j=0;j<w;j++)
			fout<<char(res[i][j])<<" ";
		fout<<endl;
	}
}

void find_sicks()
{
	int i,j;
	pair<int,int>p;
	for(i=0;i<h;i++)
	for(j=0;j<w;j++)
		if(check_sick(i,j))
		{
			p.first=i;p.second=j;
			sicks.push_back(p);
		}
}

void process(int sy,int sx)
{
	queue< pair<int,int> >q;
	pair<int,int>p;
	int y,x,i,j,k;
	p.first=sy;p.second=sx;q.push(p);
	while(!q.empty())
	{
		y=q.front().first;x=q.front().second;q.pop();
		res[y][x]=cur;
		if(y>0 && path[y-1][x]==4)
		{p.first=y-1;p.second=x;q.push(p);}
		if(x>0 && path[y][x-1]==3)
		{p.first=y;p.second=x-1;q.push(p);}
		if(y<h-1 && path[y+1][x]==1)
		{p.first=y+1;p.second=x;q.push(p);}
		if(x<w-1 && path[y][x+1]==2)
		{p.first=y;p.second=x+1;q.push(p);}
	}
}

void get_res()
{
	int i,j,y,x;
	for(i=0;i<sicks.size();i++)
	{	
		y=sicks[i].first;x=sicks[i].second;
		process(y,x);
		cur++;
	}
}

void correct()
{
	int y=0,x=0,cur;
	while(path[y][x]!=0)
	{
		if(path[y][x]==1)y--;
		else if(path[y][x]==2)x--;
		else if(path[y][x]==3)x++;
		else if(path[y][x]==4)y++;
	}
	int i;
	for(i=0;i<sicks.size();i++)
		if(sicks[i].first==y && sicks[i].second==x)
			break;
	pair<int,int>p=sicks[i];
	sicks.erase(sicks.begin()+i);
	sicks.insert(sicks.begin(),p);
}

int main()
{
	int t;fin>>t;
	int i,j,z;
	for(i=0;i<t;i++)
	{
		input();
		find_sicks();
		get_path();
		correct();
		get_res();
		output(i+1);
	}
	return 0;
}