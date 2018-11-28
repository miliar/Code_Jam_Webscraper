#include <iostream>
#include <stdio.h>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <list>
#include <iomanip>
using namespace std;int cmp(const void *a,const void *b){	return *((int*)a)-*((int*)b);}int N, D;int llist[102][2], p;int tag[102];int f(int index, int d){	int d2;	if(llist[index][0] + d >= D)		return 1;	if(d < tag[index])		return 0;	tag[index] = d;	for(int i = index + 1; i < N; i++)	{		if(llist[i][0] - llist[index][0] > d)			break;		if(llist[i][1] < llist[i][0] - llist[index][0])			d2 = llist[i][1];		else			d2 = llist[i][0] - llist[index][0];		if(f(i, d2))			return 1;	}	return 0;}int main(){	//freopen("D:\\Visual Studio 2008\\Google Code Jam\\A-small-attempt0.in", "r", stdin ) ;

	//freopen("D:\\Visual Studio 2008\\Google Code Jam\\A-small-attempt0.out", "w", stdout ) ;	int T;	cin >> T;	for(int k = 1; k <= T; k++)	{		memset(tag, -1, sizeof(tag));		cin >> N;		for(int i = 0; i < N; i++)			cin >> llist[i][0] >> llist[i][1];		qsort(llist, N, sizeof(int) * 2, cmp);		cin >> D;		printf("Case #%d: ",k);		if(f(0, llist[0][0]))			printf("YES\n");		else			printf("NO\n");	}	return 0;}