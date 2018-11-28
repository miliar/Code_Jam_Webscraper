
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cassert>
using namespace std;

const int P=10;
const int N=(1<<P);
int p;
int v[N];
int w[P][N];
int mem[P][N][P];

int doit(int x, int y, int bought){
	if(x==-1){
		if(bought<p-v[y])return -2;
		else return 0;
	}

	int &ret=mem[x][y][bought];
	if(ret!=-1)return ret;
	ret=1000*1000*1000;

	int r1a=doit(x-1,2*y  ,bought  );
	int r1b=doit(x-1,2*y+1,bought  );
	int r2a=doit(x-1,2*y  ,bought+1);
	int r2b=doit(x-1,2*y+1,bought+1);
	if(r1a!=-2 && r1b!=-2)ret=min(ret,r1a+r1b        );
	if(r2a!=-2 && r2b!=-2)ret=min(ret,r2a+r2b+w[x][y]);

	if(ret==1000*1000*1000)ret=-2;

	//cout<<"x"<<x<<" y"<<y<<" bought"<<bought<<" ret"<<ret<<endl;
	return ret;
}
int main(){
	int nn;scanf("%d",&nn);
	for(int npr=1;npr<=nn;npr++){
		memset(mem,-1,sizeof(mem));

		scanf("%d",&p);
		int n=(1<<p);
		for(int i=0;i<n;i++)scanf("%d",v+i);
		for(int i=0;i<p;i++){
			for(int k=0;k<(n>>i)/2;k++)scanf("%d",w[i]+k);
		}

		int ans=doit(p-1,0,0);
		printf("Case #%d: %d\n",npr,ans);
	}
	return 0;
}
