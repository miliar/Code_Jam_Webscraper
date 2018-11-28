#include<iostream>
#include<string>
#include<queue>
#include<vector>
using namespace std;
#define ADD 0
#define SUB 1
struct triple
{
	short x,y,v;
	triple(){x=y=v=0;}
	triple(int X,int Y,int V){x=X;y=Y;v=V;}
};

int T,K;
int n,q,i,j,l;
string INF;
int v;

#define LOW 0
#define HIGH 1000
#define ZERO 500
char a[20][20];
string d[20][20][HIGH+1];
queue<triple> Q;
triple now;
int x,y,newV;
string next;
string best[251];

bool better(const string &a,const string &b)
{
	return a.length() < b.length() || (a.length() == b.length() && a<b);
}

int main()
{
	INF.resize(1000,'X');
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	cin>>T;
	for(K=1;K<=T;++K)
	{
		cout<<"Case #"<<K<<":"<<endl;
		cin>>n>>q;
		//read
		for(i=0;i<n;++i)
			for(j=0;j<n;++j)
			{
				do{cin>>a[i][j];}while(!isdigit(a[i][j]) && a[i][j]!='+' && a[i][j]!='-');

				for(l=LOW;l<=HIGH;++l)
					d[i][j][l] = INF;

				if(isdigit(a[i][j]))
				{
					d[i][j][ZERO+a[i][j]-'0'] = a[i][j];
					Q.push(triple(i,j,ZERO+a[i][j]-'0'));
				}
			}
		for(i=1;i<=250;++i) best[i] = INF;
		//compute with BFS
		while(!Q.empty())
		{
			now = Q.front();
			Q.pop();
			for(x=now.x-1,y=now.y;x<=now.x+1;x+=2)
				if(x>=0 && y>=0 && y<n && x<n)
				{
					next = d[now.x][now.y][now.v] + a[x][y];
					switch(a[now.x][now.y])
					{
					case '+':
						newV = now.v + (a[x][y] - '0');
						if(newV<LOW || newV>HIGH)
							break;
						if(better(next,d[x][y][newV]))
						{
							d[x][y][newV] = next;
							Q.push(triple(x,y,newV));
						}
						break;
					case '-':
						newV = now.v - (a[x][y] - '0');
						if(newV<LOW || newV>HIGH)
							break;
						if(better(next,d[x][y][newV]))
						{
							d[x][y][newV] = next;
							Q.push(triple(x,y,newV));
						}
						break;
					default:
						if(better(next,d[x][y][now.v]))
						{
							d[x][y][now.v] = next;
							Q.push(triple(x,y,now.v));
						}
						
					}
				}
			for(y=now.y-1,x=now.x;y<=now.y+1;y+=2)
				if(x>=0 && y>=0 && y<n && x<n)
				{
					next = d[now.x][now.y][now.v] + a[x][y];
					switch(a[now.x][now.y])
					{
					case '+':
						newV = now.v + (a[x][y] - '0');
						if(newV<LOW || newV>HIGH)
							break;
						if(better(next,d[x][y][newV]))
						{
							d[x][y][newV] = next;
							Q.push(triple(x,y,newV));
						}
						break;
					case '-':
						newV = now.v - (a[x][y] - '0');
						if(newV<LOW || newV>HIGH)
							break;
						if(better(next,d[x][y][newV]))
						{
							d[x][y][newV] = next;
							Q.push(triple(x,y,newV));
						}
						break;
					default:
						if(better(next,d[x][y][now.v]))
						{
							d[x][y][now.v] = next;
							Q.push(triple(x,y,now.v));
						}
						
					}
				}
		}
		//compute best for range 1...250
		for(i=0;i<n;++i)
			for(j=0;j<n;++j)
				if(isdigit(a[i][j]))
					for(l=1;l<=250;++l)
						if(better(d[i][j][ZERO+l],best[l]))
							best[l] = d[i][j][ZERO+l];
		//print solutions
		while(q--)
		{
			cin>>x;
			cout<<best[x]<<endl;
		}

	}
	fclose(stdout);
	return 0;
}
