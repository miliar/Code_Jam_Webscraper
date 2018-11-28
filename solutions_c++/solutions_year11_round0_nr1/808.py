/*
TASK: G2011_Q_1 - Bot Trust
LANG: C++
NAME: untitled.cpp
*/
#include <cstdio>
#include <algorithm>

#define NMAX 101
#define ABS(x) ((x)<0?-(x):(x))
const int INTMAX=1<<30;

using namespace std;

char robot[NMAX];
int seq[NMAX],table[2][NMAX];

void func()
{
	int n,cnt[2]={0,0}; scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("\n%c%d",robot+i,seq+i);
		if('O'==robot[i]){
			table[0][cnt[0]++] = seq[i];
		}else if('B'==robot[i]){
			table[1][cnt[1]++] = seq[i];
		}
	}
	table[0][cnt[0]] = table[1][cnt[1]] = INTMAX;

	int ret=0,cur[2]={1,1}; cnt[0] = cnt[1] = 0;
	for(int i=0;i<n;i++){
		int index=('O'==robot[i]?0:1),val=ABS(table[index][cnt[index]]-cur[index])+1,mov=ABS(table[index^1][cnt[index^1]]-cur[index^1]);
		cur[index] = table[index][cnt[index]];
		if(val>mov){
			cur[index^1] = table[index^1][cnt[index^1]];
		}else{
			cur[index^1] += table[index^1][cnt[index^1]]>cur[index^1]?val:-val;
		}
		ret += val; cnt[index]++;
	}

	printf("%d\n",ret);

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