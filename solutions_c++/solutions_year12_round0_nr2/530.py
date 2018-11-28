/*
TASK: G2012_Q_2 - Dancing With the Googlers
LANG: C++
NAME: untitled.cpp
*/
#include <cstdio>
#include <algorithm>

#define SCOREMAX 30

using namespace std;

int table[SCOREMAX+1];

void solve()
{
	fill(table,table+(SCOREMAX+1),0);
	int n,s,p; scanf("%d%d%d",&n,&s,&p);
	for(int i=0;i<n;i++){
		int val; scanf("%d",&val);
		table[val]++;
	}

	int ret=0;
	for(int i=max(0,p*3-2);i<=SCOREMAX;i++){
		ret += table[i];
	}
	if(p>=2){
		for(int i=p*3-3;i>=p*3-4&&i>=0;i--){
			ret += min(table[i],s);
			s = max(0,s-table[i]);
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

	//greedyÅB O(N)

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