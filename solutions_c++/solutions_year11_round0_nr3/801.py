/*
TASK: G2011_Q_3 - Candy Splitting
LANG: C++
NAME: untitled.cpp
*/
#include <cstdio>
#include <algorithm>

#define NMAX 1000

using namespace std;

int table[NMAX];

void func()
{
	int n,sum=0,ret=0; scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d",table+i);
		sum = sum^table[i];
		ret += table[i];
	}

	if(0!=sum){
		printf("NO\n");
	}else{
		printf("%d\n",ret-*min_element(table,table+n));
	}

	return;
}


int main()
{
	FILE *fin=NULL,*fout=NULL;
	fin = freopen("input.txt","r",stdin);
	fout = freopen("output.txt","w",stdout);

	int t; scanf("%d",&t);
	for(int i=0;i<t;i++){
		printf("Case #%d: ",i+1);
		func();
	}

	//finalize
	if(NULL!=fin) fclose(fin);
	if(NULL!=fout) fclose(fout);

	return 0;
}