#include<iostream>
using namespace std;

int cas,N,K;
int dir[8][2]={1,0,1,1,0,1,-1,1,-1,0,-1,-1,0,-1,1,-1};

char map[60][60];
char temp[60][60];

bool blue,red;

inline bool ill(int i,int j)
{
	return i>=1 && i<=N && j>=1 && j<=N;
}

void find()
{
	for(int i=1;i<=N;i++)
	{
		for(int j=1;j<=N;j++)
		{
			if( map[i][j]=='B' )
			{
				//if( blue ) continue;
				for(int in=0;in<8;in++)
				{
					int k=0;
					while( true )
					{
						int x=i+dir[in][0]*k;
						int y=j+dir[in][1]*k;

						if( !ill(x,y) || map[x][y]!='B') break;
						else k++;
					}
					if( k>=K) blue=true;
				}
			}
			if( map[i][j]=='R' ) 
			{
				//if( red ) continue;
				for(int in=0;in<8;in++)
				{
					int k=0;
					while( true )
					{
						int x=i+dir[in][0]*k;
						int y=j+dir[in][1]*k;

						if( !ill(x,y) || map[x][y]!='R') break;
						else k++;
					}
					if( k>=K) red=true;
				}
			}
		}
	}
}

void process()
{
	for(int j=1;j<=N;j++)
	{
		int ind=1;
		for(int i=1;i<=N;i++)
			if( map[i][j]!='.') 
				map[ind++][j]=map[i][j];
		while(ind<=N) map[ind++][j]='.';
	}
}

void test()
{
	while( cin>>N>>K)
	{
		for(int i=N;i>=1;i--) scanf(" %s",map[i]+1);

		red=blue=false;

		find();

		cout<<red << ' '<<blue<<endl;
	}
}

int main()
{
	//test();
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int kkk=1;
	scanf("%d",&cas);
	while( cas-- )
	{
		scanf("%d%d",&N,&K);
		for(int i=N;i>=1;i--)
		{
			scanf(" %s",temp[i]+1);
		}

		for(int i=1;i<=N;i++)
		{
			for(int j=1;j<=N;j++)
			{
				map[N-j+1][i]=temp[i][j];
			}
		}

		process();

		blue=red=false;

		find();

		printf("Case #%d: ",kkk++);
		if( red && blue )puts("Both");
		else if( !red && !blue) puts("Neither");
		else if( red ) puts("Red");
		else puts("Blue");
	}
}