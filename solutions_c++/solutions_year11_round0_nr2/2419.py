#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <sstream>
#define MAX 100
#define BIT(x) (1<<(x-1))
using namespace std;
#define min(a,b) (((a) < (b)) ? (a) : (b))

char queue[MAX+1];
int fp;
char seq[MAX+1];
struct _combine{
	char A;
	char B;
	char T;
};

struct _opposed{
	char A;
	char B;
};

struct _combine com[MAX];
struct _opposed opp[MAX];
int n_com;
int n_opp;
int len;
void readdata()
{
	int i;
	fp = 0;
	scanf("%d ",&n_com);
	for (i=0; i<n_com; ++i){
		scanf("%c%c%c ",&com[i].A, &com[i].B, &com[i].T);
	}
	scanf("%d ",&n_opp);
	for (i=0; i<n_opp; ++i){
		scanf("%c%c ",&opp[i].A, &opp[i].B);
	}
	
	scanf("%d ",&len);
		scanf("%s",seq);
}
void check_com()
{
	int i;
	for (i=0; i<n_com; ++i){
		if ( (queue[fp-1] == com[i].A && queue[fp-2] == com[i].B) ||  \
			 (queue[fp-1] == com[i].B && queue[fp-2] == com[i].A) )
		{
			queue[fp-2] = com[i].T;
			fp--;
		}
	}
}

void check_opp()
{
	int i;
	int j;
	int hash[0x100];
	memset(hash, 0, sizeof(hash));

	for (i=0; i<fp; ++i){
		hash[queue[i]] = 1;
	}

	for (i=0; i<n_opp; ++i){
		if (hash[opp[i].A] && hash[opp[i].B])
			fp = 0;             //clear the queue , delete all the elements
	}
}
void solve()
{
	int i,j;
	for (i=0; i<len; ++i){
		queue[fp++] = seq[i]; // push element into the queue
		if (fp > 1){
			check_com();
			check_opp();
		}
	}
}

void output()
{
	int i;
	if (fp == 0)
		printf("[]\n");
	else{
		printf("[");
		for (i=0; i<fp-1; ++i)
			printf("%c, ",queue[i]);
		printf("%c]\n",queue[fp-1]);
	}
}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	int nt, it;
	
	scanf("%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		readdata();
		solve();
		printf("Case #%d: ",it);
		output();
		
	}
	return 0;
}