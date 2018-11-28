#include<iostream>
#include<vector>
using namespace std;
const int mx[8]={-1,-1,0,1,1,1,0,-1};
const int my[8]={0,1,1,1,0,-1,-1,-1};
int times,n,k,map[100][100];
bool use[3];
char ch;
bool t;
vector<int >  temp;
bool mov(int x,int y,int f,int all)
{
	bool p=false;
	if ((x==3)&&(y==5))
	{
		p=true;
//		printf("\n");
	}
	int mark=map[x][y];
	for (int a=1;a<all;++a)
	{
		x+=mx[f];
		y+=my[f];
	/*if (p)
		{
			if (a==4)
			{
				++a;
				--a;
			}
			printf("%d ",a);
		}*/
		if (x<1) return false;
		if (x>n) return false;
		if (y<1) return false;
		if (y>n) return false;
		if (map[x][y]!=mark) return false;
	}
	return true;
}
bool check(int x,int y,int all)
{
	for (int a=0;a<8;++a)
	{
		if (mov(x,y,a,all)) return true;
	//	printf("\n");
	}
	return false;
}
void mem()
{
	temp.clear();t=0;
	memset(use,0,sizeof(use));
	memset(map,0,sizeof(map));
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&times);
	for (int z=1;z<=times;++z)
	{
		scanf("%d%d",&n,&k);
		mem();
		for(int a=1;a<=n;++a)
		for(int b=1;b<=n;++b)
		{
			scanf("%c",&ch);
			while ((ch!='.')&&(ch!='R')&&(ch!='B')) scanf("%c",&ch);
			if (ch=='.')
			map[a][b]=0;else map[a][b]=(ch=='R'?1:2);
		}
		for (int a=1;a<=n;++a)
		{
			temp.clear();
			for (int b=1;b<=n;++b)
			{
				if (map[a][b])
				{
					temp.push_back(map[a][b]);
				}
			}
			for (int b=1;b<=n-temp.size();++b) map[a][b]=0;
			for (int b=0;b<temp.size();++b) map[a][b+n-temp.size()+1]=temp[b];
		}
		for (int a=1;a<=n;++a)
		{for (int b=1;b<=n;++b)
		{
		//	printf("%d",map[a][b]);
			if (map[a][b])
		{
			t=check(a,b,k);
			if (t)
			{
				use[map[a][b]]=1;
			}
		}
		}//printf("\n");
		}
		printf("Case #%d: ",z);
		if (use[1])
		{
			if (use[2])
			{
				printf("Both\n");
			}else printf("Red\n");
		}else
		{
			if (use[2])
			{
				printf("Blue\n");
			}else printf("Neither\n");
		}
	}
}
