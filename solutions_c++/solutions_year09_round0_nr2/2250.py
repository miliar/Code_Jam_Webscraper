#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

char code='a';
int H=0,W=0;

//(Altitude,(Parent,Child))
vector<pair<int,pair<int,int> > > t1(100);
vector<vector<pair<int,pair<int,int> > > > Map(100,t1);
vector<char>t2(100,'0');
vector< vector< char> >Res(100,t2);

//Mapping -1:None,0:NotAssigned,1:North,2:West,4:East,8:South
int opp(int x)
{
	if(x==1)
		return 8;
	if(x==8)
		return 1;
	if(x==2)
		return 4;
	if(x==4)
		return 2;
	return 0;
}
int value(int i,int j)
{
	if(i>=0 && i<H && j>=0 && j<W)
		return Map[i][j].first;
	return 11000;
}

int LowestNeighbour(int i,int j)
{
	int res=0;
	int val=value(i,j);
	if(value(i-1,j)<val)
	{	
		val=value(i-1,j);
		res=1;
	}
	if(value(i,j-1)<val)
	{	
		val=value(i,j-1);
		res=2;
	}
	if(value(i,j+1)<val)
	{	
		val=value(i,j+1);
		res=4;
	}
	if(value(i+1,j)<val)
	{	
		val=value(i+1,j);
		res=8;
	}
	return res;
}

int NeighbourI(int i,int d)
{
	if(d==1)
		return i-1;
	if(d==2)
		return i;
	if(d==4)
		return i;
	return i+1;
}
int NeighbourJ(int j,int d)
{
	if(d==1)
		return j;
	if(d==2)
		return j-1;
	if(d==4)
		return j+1;
	return j;
}
void Traverse(int i,int j)
{
	int l=LowestNeighbour(i,j);
	Map[i][j].second.second=l;
	int x=NeighbourI(i,l);
	int y=NeighbourJ(j,l);
	if(x>=0 && x<H && y>=0 && y<W)
		Map[x][y].second.first|=opp(l);
	if(l)
		Traverse(NeighbourI(i,l),NeighbourJ(j,l));
}

vector<int> Fill1(int i,int j)
{
	vector<int>Sink(2,0);
	Res[i][j]=code;
	if(Map[i][j].second.second==0)
	{
		Sink[0]=i,Sink[1]=j;
	}
	else
	{
		int l=Map[i][j].second.second;
		Sink=Fill1(NeighbourI(i,l),NeighbourJ(j,l));
	}
	return Sink;
}

void Fill2(int i,int j)
{
	Res[i][j]=code;
	int d=Map[i][j].second.first;
	if(d&1)
		Fill2(i-1,j);
	if(d&2)
		Fill2(i,j-1);
	if(d&4)
		Fill2(i,j+1);
	if(d&8)
		Fill2(i+1,j);
}

void Fill(int i,int j)
{
	Res[i][j]=code;
	vector<int>Sink=Fill1(i,j);
	Fill2(Sink[0],Sink[1]);
}

int main()
{
	freopen("b.in","r",stdin) ;
	freopen("bout.txt","w",stdout) ;
	int T=0;
	scanf("%d",&T);
	for(int I=0;I<T;++I)
	{
		scanf("%d %d",&H,&W);
		code='a';
		
		for(int i=0;i<H;++i)
			for(int j=0;j<W;++j)
			{
				Res[i][j]='0';
			}
		
		for(int i=0;i<H;++i)
			for(int j=0;j<W;++j)
			{
				scanf("%d",&Map[i][j].first);
				Map[i][j].second.first=0;
				Map[i][j].second.second=0;
			}
		for(int i=0;i<H;++i)
			for(int j=0;j<W;++j)
			{
				if(Map[i][j].second.second==0)
				{
					Traverse(i,j);
				}
			}
		
		
		for(int i=0;i<H;++i)
			for(int j=0;j<W;++j)
			{
				if(Res[i][j]=='0')
				{
					Res[i][j]=code;
					Fill(i,j);
					code++;
				}
			}
		
			printf("Case #%d:\n",I+1);
			for(int i=0;i<H;++i)
			{
				for(int j=0;j<W;++j)
					printf("%c ",Res[i][j]);
				printf("\n");
			}

	}
	return 0;
}