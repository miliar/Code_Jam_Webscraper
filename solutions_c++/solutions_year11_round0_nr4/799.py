/*
TASK: G2011_Q_4 - GoroSort
LANG: C++
NAME: untitled.cpp
*/
#include <cstdio>

using namespace std;

void func()
{
	int n,cnt=0; scanf("%d",&n);
	for(int i=0;i<n;i++){
		int val; scanf("%d",&val);
		if(i+1!=val) cnt++;
	}

	printf("%.06lf\n",(double)cnt);

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