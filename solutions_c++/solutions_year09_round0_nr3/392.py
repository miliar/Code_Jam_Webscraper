#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

int N,M;
const int MLEN=111111;
const char wl[]={"welcome to code jam"};
const int mod=10000;
char buf[MLEN];
vector<int> pos[256];
int res[MLEN];
void test()
{
	cin.getline(buf,MLEN);
	N=strlen(buf);
	int i,j,x,J;
	for(i=0;i<=M;i++) res[i]=0;
	res[0]=1;
	for(i=0;i<N;i++)
	{
		x=buf[i];
		if(!pos[x].empty())
		{
			J=pos[x].size();
			for(j=0;j<J;j++)
			{
				res[pos[x][j]]=(res[pos[x][j]]+res[pos[x][j]-1])%mod;
			}
		}
	}

	printf("%.4d\n",res[M]);
	
}

void init()
{
	M=strlen(wl);
	int i;
	for(i=M-1;i>=0;i--)
	{
		pos[wl[i]].push_back(i+1);
	}
	cin.getline(buf,MLEN);
	
}
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);

	int t=0,T;

	scanf("%d",&T);

	init();
	for(t=0;t<T;t++)
	{
		printf("Case #%d: ",t+1);
		test();
	}
}