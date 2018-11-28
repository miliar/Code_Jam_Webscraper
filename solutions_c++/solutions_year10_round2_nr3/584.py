#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cstdlib>
#include <stdlib.h>
#include <stack>
#include <cstdio>
#include <map>
#include <cmath>
#include <time.h>
using namespace std;

#define MAX(a,b) ((a>=b)?a:b)
#define MIN(a,b) ((a<=b)?a:b)
#define ABS(a) ((a<0)?-(a):a)

int mas[26];
int main()
{
	//freopen("in.txt","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out3.out","w",stdout);
	//preprocessed:
	mas[2]=1;
	mas[3]=2;
	mas[4]=3;
	mas[5]=5;
	mas[6]=8;
	mas[7]=14;
	mas[8]=24;
	mas[9]=43;
	mas[10]=77;
	mas[11]=140;
	mas[12]=256;
	mas[13]=472;
	mas[14]=874;
	mas[15]=1628;
	mas[16]=3045;
	mas[17]=5719;
	mas[18]=10780;
	mas[19]=20388;
	mas[20]=38674;
	mas[21]=73562;
	mas[22]=40265;
	mas[23]=68060;
	mas[24]=13335;
	mas[25]=84884;
	int T,n;
	scanf("%d",&T);
	for(int t=0;t<T;++t)
	{
		scanf("%d",&n);
		printf("Case #%d: ",t+1);
		printf("%d\n",mas[n]);
	}
}