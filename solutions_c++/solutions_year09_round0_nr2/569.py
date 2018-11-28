#include <vector>
#include <string>
#include <list>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include<iostream>
using namespace std;
int T,H,W;
int maps[101][101];
int tmpresult[101][101];
char result[101][101];
char label;
char tmp[10001];
int find(int i,int j)
{
	if(tmpresult[i][j] != -1) return tmpresult[i][j];
	int an,aw,ae,as;
	if((i - 1) >= 0) an = maps[i - 1][j];
	else an = 1000000;
	if((i + 1) < H) as = maps[i + 1][j];
	else as = 1000000;
	if((j - 1) >= 0) aw = maps[i][j - 1];
	else aw = 1000000;
	if((j + 1) < W) ae = maps[i][j + 1];
	else ae = 1000000;

	int tmp;
	if(an == as && as == aw && aw == ae && an == 1000000) tmp = i * W + j;
	else if(an != 1000000 && an <= aw && an <= ae && an <= as && maps[i][j] > an) tmp = find(i - 1,j);
	else if(aw != 1000000 && aw <= an && aw <= ae && aw <= as && maps[i][j] > aw) tmp = find(i,j - 1);
	else if(ae != 1000000 && ae <= aw && ae <= an && ae <= as && maps[i][j] > ae) tmp = find(i,j + 1);
	else if(as != 1000000 && as <= aw && as <= ae && as <= an && maps[i][j] > as) tmp = find(i + 1,j);
	else  tmp = i * W + j;
	return tmpresult[i][j] = tmp;
}
void change(void)
{
	for(int i = 0;i < H;i++)
	{
		for(int j = 0;j < W;j++)
		{
			if(tmp[tmpresult[i][j]] != 'A') result[i][j] = tmp[tmpresult[i][j]];
			else {result[i][j] = tmp[tmpresult[i][j]] = ++label;}
		}
	}
}
int main()
{
	freopen("..\\B-large.in","r",stdin);
	freopen("..\\B.out","w",stdout);
	scanf("%d",&T);
	for(int i = 1;i <= T;i++)
	{
		scanf("%d%d",&H,&W);
		label = 'a' - 1;
		for(int j = 0;j < H;j++)
		{
			for(int k = 0;k < W;k++)
			{
				scanf("%d",&maps[j][k]);
				tmpresult[j][k] = -1;
			}
		}
		for(int j = 0;j < H;j++)
			for(int k = 0;k < W;k++)
				find(j,k);
		memset(tmp,'A',sizeof(tmp));
		change();
		printf("Case #%d:\n",i);
		for(int j = 0;j < H;j++)
		{
			for(int k = 0;k < W;k++)
			{
				if(k != 0) printf(" %c",result[j][k]);
				else printf("%c",result[j][k]);
			}
			printf("\n");
		}
	}
	return 0;
}