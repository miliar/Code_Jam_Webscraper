#include <iostream>
#include <queue>
#include <map>
using namespace std;

enum {NORTH,WEST};

bool visited[23][23][4];
//int dist[23][23][4];
int W[23][23];
int N[23][23];
int T[23][23];


bool valid(int x, int y, int t, int d)
{
	int mod = (t-T[x][y])%(W[x][y]+N[x][y]);
	if(mod<0) mod+=W[x][y]+N[x][y];
	//cout<<"valid"<<t<<" "<<N[x][y]<<" "<<W[x][y]<<" "<<T[x][y]<<" "<<mod<<endl;
	if(mod<N[x][y]) return d==NORTH;
	else return d==WEST;
}
typedef pair<int,int> ip;
typedef pair<ip,ip> ipp;
typedef pair<ipp,int> ippp;
int main()
{
	int cases;
	cin>>cases;
	for(int i=1;i<=cases;i++)
	{
		memset(visited,0,sizeof(visited));
		//memset(dist,0,sizeof(dist));
		int X,Y;
		cin>>X>>Y;
		for(int x=0;x<X;x++)
		{
			for(int y=0;y<Y;y++)
			{
				cin>>N[x][y]>>W[x][y]>>T[x][y];
			}
		}
		priority_queue<ippp, vector<ippp>, greater<ippp> > q;
		q.push(ippp(ipp(ip(0,0), ip(X-1, 0)), 0));
		int ans;
		while(!q.empty())
		{
			ippp ele = q.top(); q.pop();
			int x = ele.first.second.first;
			int y = ele.first.second.second;
			int d = ele.first.first.first;
			int t = ele.first.first.second;
			int loc = ele.second;
			//printf("ele %d %d %d %d %d\n",x,y,d,t,loc);
			if(x==0 && y == Y-1 && loc == 2) {ans = t; break;}
			visited[x][y][loc]=true;
			q.push(ippp(ipp(ip(t+1,t+1), ip(x,y)), loc));
			if(valid(x,y,t,NORTH))
			{
				int newloc = loc^1;
				int newt=t+1;
				if(!visited[x][y][newloc])
				{
					visited[x][y][newloc]=true;
					q.push(ippp(ipp(ip(newt,newt),ip(x,y)), newloc));
				}
			}
			else if(valid(x,y,t,WEST))
			{
				int newloc = 3-loc;
				int newt=t+1;
				if(!visited[x][y][newloc])
				{
					visited[x][y][newloc]=true;
					q.push(ippp(ipp(ip(newt,newt),ip(x,y)), newloc));
				}
			}
			else
			{
				cout<<"!o.O!"<<endl;
				return 0;
			}
			if(loc==0 && y>0)
			{
				int newloc = 3;
				int newx = x;
				int newy = y-1;
				int newt = t+2;
				if(!visited[newx][newy][newloc])
				{
					visited[newx][newy][newloc]=true;
					q.push(ippp(ipp(ip(newt,newt),ip(newx,newy)),newloc));
				}
			}
			if(loc==0 && x<X-1)
			{
				int newloc = 1;
				int newx = x+1;
				int newy = y;
				int newt = t+2;
				if(!visited[newx][newy][newloc])
				{
					visited[newx][newy][newloc]=true;
					q.push(ippp(ipp(ip(newt,newt),ip(newx,newy)),newloc));
				}
			}
			if(loc==1 && y>0)
			{
				int newloc = 2;
				int newx = x;
				int newy = y-1;
				int newt = t+2;
				if(!visited[newx][newy][newloc])
				{
					visited[newx][newy][newloc]=true;
					q.push(ippp(ipp(ip(newt,newt),ip(newx,newy)),newloc));
				}
			}
			if(loc==1 && x>0)
			{
				int newloc = 0;
				int newx = x-1;
				int newy = y;
				int newt = t+2;
				if(!visited[newx][newy][newloc])
				{
					visited[newx][newy][newloc]=true;
					q.push(ippp(ipp(ip(newt,newt),ip(newx,newy)),newloc));
				}
			}
			if(loc==2 && x>0)
			{
				int newloc = 3;
				int newx = x-1;
				int newy = y;
				int newt = t+2;
				if(!visited[newx][newy][newloc])
				{
					visited[newx][newy][newloc]=true;
					q.push(ippp(ipp(ip(newt,newt),ip(newx,newy)),newloc));
				}
			}
			if(loc==2 && y<Y-1)
			{
				int newloc = 1;
				int newx = x;
				int newy = y+1;
				int newt = t+2;
				if(!visited[newx][newy][newloc])
				{
					visited[newx][newy][newloc]=true;
					q.push(ippp(ipp(ip(newt,newt),ip(newx,newy)),newloc));
				}
			}
			if(loc==3 && y<Y-1)
			{
				int newloc = 0;
				int newx = x;
				int newy = y+1;
				int newt = t+2;
				if(!visited[newx][newy][newloc])
				{
					visited[newx][newy][newloc]=true;
					q.push(ippp(ipp(ip(newt,newt),ip(newx,newy)),newloc));
				}
			}
			if(loc==3 && x<X-1)
			{
				int newloc = 2;
				int newx = x+1;
				int newy = y;
				int newt = t+2;
				if(!visited[newx][newy][newloc])
				{
					visited[newx][newy][newloc]=true;
					q.push(ippp(ipp(ip(newt,newt),ip(newx,newy)),newloc));
				}
			}
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}
