#include <iostream>
#include <vector>

using namespace std;
#define pb push_back
#define LL long long
#define M 500
int P[M][M];
int Q[M][M];
int vis[M][M];
int dx[]={1,-1,0,0};
int dy[]={0,0,1,-1};
int X,Y;
int dir;
void move()
{
	switch(dir)
	{
		case 0:
			Y--;
			break;
		case 1: X--;
			break;
		case 2: Y++;
			break;
		case 3:X++;
		       break;
	}
}
void mark(string& s,int t)
{
	for(int i=0;i<t;i++)
		for(int j=0;j<s.length();j++)
		{
			//cout<<X<<" "<<Y<<"\n";
			switch(s[j])
			{
			case 'L':
				dir++;
				dir%=4;
				break;
			case 'R':
				dir+=3;
				dir%=4;
				break;
			case 'F':move();
				 P[X][Y]=1;
				 move();
				 P[X][Y]=1;
			}
		}
}
void dfs(int x,int y)
{
	//cerr<<x<<" "<<y<<"\n";
	if(x<0 || y<0 || x>=M || y>=M) return;
	if( vis[x][y]) return;
	if( P[x][y]==1) return;
	vis[x][y]=1;
	for(int i=0;i<4;i++)
		dfs(x+dx[i],y+dy[i]);
	
}



class tmp
{
	public:
		int x,y;
};

int calcnew()
{
	//cerr<<"Here\n";
	for(int i=0;i<M;i++) for(int j=0;j<M;j++) vis[i][j]=0;
	vis[0][0]=true;
	tmp p;
	p.x = p.y =0;
	vector<tmp> vec;
	vec.pb(p);
	while(!vec.empty())
	{
		tmp l = vec[vec.size()-1];
		vec.pop_back();
		for(int i=0;i<4;i++)
		{
			int x1 = l.x+dx[i];
			int y1 = l.y + dy[i];
			if(x1>=0 && y1>=0 && x1<M && y1<M && P[x1][y1]==-1 && !vis[x1][y1])
			{
				vis[x1][y1]=1;
				tmp p1;
				p1.x = x1;
				p1.y = y1;
				vec.pb(p1);
			}
		}
	}

	//for(int i=0;i<M;i++)
	//	for(int j=0;j<M;j++)
	//		if(vis[i][j]==0)
	//			cout<<i<<" "<<j<<" is unv\n";


	int ret = 0;
	for(int i=1;i<M;i+=2)
		for(int j=1;j<M;j+=2)
			if(vis[i][j])
			{
				bool f1,f2,f3,f4;
				f1 = f2 = false;
				f3 = f4 = false;
				for(int k=0;k<M;k++)
				{
					if(P[i][k]==1 && k<j)
						f1=true;
					else if(P[i][k]==1 && k>j)
						f2=true;
					if(P[k][j]==1 && k<i)
						f3=true;
					else if(P[k][j]==1 && k>i)
						f4=true;
				}
				if( (f1 && f2) || ( f3 && f4))
				{
	//				cout<<"Choosing "<<i<<" "<<j<<"\n";
					ret++;
				}
					
			}
	return ret;
}

int calc()
{
	bool vis[M][M];
	bool vis1[M][M];
	for(int i=0;i<M;i++)
		for(int j=0;j<M;j++)
			vis[i][j]=vis1[i][j]=false;
	vis[0][0]=vis1[0][0]=true;
	int dx[]={1,-1,0,0};
	int dy[]={0,0,1,-1};
	tmp p;
	p.x = p.y =0;
	vector<tmp> vec;
	vec.pb(p);
	while(!vec.empty())
	{
		tmp l = vec[vec.size()-1];
		vec.pop_back();
		for(int i=0;i<4;i++)
		{
			int x1 = l.x+dx[i];
			int y1 = l.y + dy[i];
			if(x1>=0 && y1>=0 && x1<M && y1<M && P[x1][y1]==-1 && !vis[x1][y1])
			{
				vis[x1][y1]=1;
				tmp p1;
				p1.x = x1;
				p1.y = y1;
				vec.pb(p1);
			}
		}
	}
	p.x = p.y =0;
	vec.pb(p);
	while(!vec.empty())
	{
		tmp l = vec[vec.size()-1];
		vec.pop_back();
		for(int i=0;i<4;i++)
		{
			int x1 = l.x+dx[i];
			int y1 = l.y + dy[i];
			if(x1>=0 && y1>=0 && x1+1<M && y1+1<M && !vis1[x1][y1])
			{
				bool f;
				if(l.x == x1)
					f=(P[x1+1][y1]!=1 || P[x1][y1]!=1);
				else
					f=(P[x1][y1+1]!=1 || P[x1][y1]!=1);

				if(f)
				{
				vis1[x1][y1]=1;	
				tmp p1;
				p1.x = x1;
				p1.y = y1;
				vec.pb(p1);
				}
			}
		}
	}
	for(int i=0;i<M;i++)
		for(int j=0;j<M;j++)
			Q[i][j]=0;
	for(int i=0;i<M;i++)
		for(int j=0;j<M;j++)
			if(P[i][j]==1)
				Q[i][j]=1;
		else if(vis[i][j])
		{
			bool f1=false;
			bool f2=false;
			for(int k=0;k<M;k++)
				if(P[i][k]==1 && k<=j) f1=true;
				else
				if(P[i][k]==1 && k>=j) f2=true;
			if( f1 && f2)
				Q[i][j]=1;
			bool f3,f4;
			f3=f4=false;
			
			for(int k=0;k<M;k++)
				if(P[k][j]==1 && k<=i) f3=true;
				else
				if(P[k][j]==1 && k>=i) f4=true;
		}


	int ret = 0;
	for(int i=0;i<M-1;i++)
		for(int j=0;j<M-1;j++)
		{
			if(Q[i][j] && Q[i+1][j] && Q[i][j+1] && Q[i+1][j+1]
			  && (P[i][j]!=1 || P[i+1][j]!=-1 || P[i][j+1]!=-1 || P[i+1][j+1]!=-1))
				ret++;
			else if(Q[i][j] && Q[i+1][j] && Q[i][j+1] && Q[i+1][j+1] && vis1[i][j])
				ret++;

		}
	return ret;
}
int main()
{
	int TT;
	scanf("%d",&TT);
	int c=0;
	while(TT--)
	{
		int L;
		cin>>L;
		dir = 0;
		for(int i=0;i<M;i++) for(int j=0;j<M;j++)
			P[i][j]=-1;
		X = Y = 200;
		P[X][Y] = 1;
		for(int i=0;i<L;i++)
		{
			string s;
			int t;
			cin>>s>>t;
			mark(s,t);
		}
		cout<<"Case #"<<++c<<": "<<calcnew()<<"\n";
	}
	return 0;
}
