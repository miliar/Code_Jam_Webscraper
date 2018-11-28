/*
TASK: G2012_Q_3 - Recycled Numbers
LANG: C++
NAME: untitled.cpp
*/
#include <cstdio>
#include <algorithm>

#define PWMAX 8
#define BMAX 2000000

using namespace std;

int pw[PWMAX],vis[BMAX+1];

int getdigit(int val)
{
	int tmp=10;
	for(int i=1;;i++){
		if(val<tmp){
			return i;
		}
		tmp *= 10;
	}
	return -1;
}

void solve()
{
	int a,b,ret=0; scanf("%d%d",&a,&b);
	fill(vis,vis+(BMAX+1),-1);
	for(int i=a;i<=b;i++){
		int dig=getdigit(i);
		for(int j=1;j<dig;j++){
			int m=(i%pw[j])*pw[dig-j]+i/pw[j];
			if(i<m&&m<=b&&i!=vis[m]){
				//printf("%d %d\n",i,m);
				ret++; vis[m] = i;
			}
		}
	}

	printf("%d\n",ret);

	return;
}

int main()
{
	FILE *fin=NULL,*fout=NULL;
	fin = freopen("input.txt","r",stdin);
	fout = freopen("output.txt","w",stdout);

	//‘S’TõB O(B)

	pw[0] = 1;
	for(int i=1;i<PWMAX;i++){
		pw[i] = pw[i-1]*10;
	}

	int t; scanf("%d",&t);
	for(int i=0;i<t;i++){
		printf("Case #%d: ",i+1);
		solve();
	}

	//finalize
	if(NULL!=fin) fclose(fin);
	if(NULL!=fout) fclose(fout);

	return 0;
}