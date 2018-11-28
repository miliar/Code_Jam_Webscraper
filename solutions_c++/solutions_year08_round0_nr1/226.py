#include <iostream>
#include <map>
#include <string>
using namespace std;

char strtmp[200];

typedef map<string,int> msi;

msi mm;
int S,Q;

int quary[2000];

int f[2][200];

void work()
{
	int X=0;
	int minn;
	memset(f,0,sizeof(f));
	for(int i=0;i<Q;++i)
	{
		for(int j=0;j<S;++j)
		{
			if(j==quary[i])
			{
				f[X][j]=-1;
				continue;
			}
			if(f[!X][j]!=-1)
			{
				f[X][j]=f[!X][j];
				continue;
			}
			minn=10000;
			for(int k=0;k<S;++k)
			{
				if(f[!X][k]<0) continue;
				if(f[!X][k]<minn) minn=f[!X][k];
			}
			f[X][j]=minn+1;
		}
		X=!X;
	}
	minn=10000;
	for(int k=0;k<S;++k)
	{
			if(f[!X][k]<0) continue;
			if(f[!X][k]<minn) minn=f[!X][k];
	}
	printf("%d\n",minn);
}

int main()
{
	int n;
	string ss;
	msi::iterator iter;
	scanf("%d",&n);
	for(int i=0;i<n;++i)
	{
		scanf("%d",&S);
		cin.getline(strtmp,200);
		mm.clear();
		for(int j=0;j<S;++j)
		{
			cin.getline(strtmp,200);
			ss=string(strtmp);
			mm[ss]=j;
		}
		scanf("%d",&Q);
		cin.getline(strtmp,200);
		for(int j=0;j<Q;++j)
		{
			cin.getline(strtmp,200);
			ss=string(strtmp);
			iter=mm.find(ss);
			quary[j]=iter->second;
		}
		printf("Case #%d: ",i+1);
		work();
	}
	return 0;
}

