#include <iostream>
using namespace std;
int n,m;
int map[500][500];
bool visit[1000];
int l[1000];//邻接点
bool find(int a)
{
	for(int i=1;i<=n;++i)
		if(map[2*a][2*i-1]&&!visit[2*i-1])
		{
			visit[2*i-1]=1;
			if(!l[2*i-1]||find(l[2*i-1]))
			{
				l[2*i-1]=a;
				return true;
			}
		}
	return false;
}

void init(){
	memset(l,0,sizeof(l));
	memset(map,0,sizeof(map));
}

void add(int a,int b){
	map[2*a][2*b-1]=1;
}

int run(){
	int ans=0;
	for(int i=1;i<=n;++i)
	{
		memset(visit,0,sizeof(visit));
		if(find(i))ans++;
	}
	return n-ans;
}

bool compare(int*a,int*b,int n){
	for(int i=0;i<n;i++)
		if(b[i]>=a[i])return 0;
	return 1;
}

int a[500][100];

int main()
{
	int cas;
	scanf("%d",&cas);
	for(int kase=1;kase<=cas;++kase)
	{
		init();
		cout<<"Case #"<<kase<<": ";
		int k;
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;i++)
			for(int j=0;j<k;j++)
				scanf("%d",a[i]+j);
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				if(i!=j)
					if(compare(a[i],a[j],k))
						add(i+1,j+1);
		cout<<run()<<endl;
	}
	return 0;
}
