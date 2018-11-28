#include <iostream>

using namespace std;

#define INF 2000000
#define MIN(a,b) ((a)<(b)?(a):(b))
struct points
{
	int x, y;
	points(int xx=0, int xy=0){x=xx;y=xy;}
	/*
	bool operator<(points& z)
	{
		if(x!=z.x) return x<z.x;
		return y<z.y;
	}
	*/
	bool operator==(points& z)
	{
		if(x==z.x && y==z.y) return true;
		return false;
	}
};

bool comp(points x, points y)
{
	if(x.x != y.x) return x.x < y.x;
	return x.y < y.y;
}
int map[120][120];
char now_sign;
char sign[120][120];
points parent[120][120];

points get_parent(points z)
{
	if(z==parent[z.x][z.y]) return z;
	parent[z.x][z.y]=get_parent(parent[z.x][z.y]);
	return parent[z.x][z.y];
}

char get_sign(points z)
{
	if(sign[z.x][z.y]) return sign[z.x][z.y];
	sign[z.x][z.y]=now_sign++;
	return sign[z.x][z.y];
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t, h, w, i, j, c;
	cin>>t;
	for(c=1;c<=t;c++)
	{
		cin>>h>>w;
		now_sign='a';
		for(i=0;i<=h+1;i++) map[i][0]=map[i][w+1]=INF;
		for(i=0;i<=w+1;i++) map[0][i]=map[h+1][i]=INF;
		for(i=1;i<=h;i++) for(j=1;j<=w;j++) cin>>map[i][j];
		for(i=1;i<=h;i++) for(j=1;j<=w;j++)
		{
			sign[i][j]=0;
			int min = MIN(MIN(MIN(map[i-1][j], map[i][j-1]),map[i+1][j]),map[i][j+1]);
			if(map[i][j]<=min) 		  parent[i][j]=points(i,j);
			else if(map[i-1][j]==min) parent[i][j]=points(i-1,j);
			else if(map[i][j-1]==min) parent[i][j]=points(i,j-1);
			else if(map[i][j+1]==min) parent[i][j]=points(i,j+1);
			else 					  parent[i][j]=points(i+1,j);
		}
		//for(i=0;i<=h+1;i++, cout<<endl) for(j=0;j<=w+1;j++) cout<<map[i][j]<<' ';
		//sort(sink, sink+no_sink, comp);
		//for(i=0;i<no_sink;i++) sign[sink[i].x][sink[i].y]=i+'a';
		
		points par;
		
		cout<<"Case #"<<c<<":\n";
		for(i=1;i<=h;i++)
		{
			points par=get_parent(parent[i][1]);
			cout<<get_sign(par);
			for(j=2;j<=w;j++)
			{
				par=get_parent(parent[i][j]);
				cout<<' '<<get_sign(par);
			}
			cout<<endl;
		}
	}
	return 0;
}
