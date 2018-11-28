#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <map>
#define rep(i,n) for (int i=0;i<n;i++)
#define Max(a,b) a>b?a:b
#define Min(a,b) a<b?a:b
#define INF 0x7fffffff
#define fop freopen("1.in", "r", stdin);freopen("data.txt", "w", stdout)
#define fop2 freopen("2.in", "r", stdin);freopen("data2.txt", "w", stdout)
#define LL long long
using namespace std;
int flag;

char mp[4][4];
bool rowcheck(int row,char ch){
	int i;
	for (i=0;i<4;++i)
		if (mp[row][i]!=ch&&mp[row][i]!='T')
			break;
	if(i==4) return true;
	else return false;
}

bool colcheck(int col,char ch){
	int i;
	for (i=0;i<4;++i)
		if (mp[i][col]!=ch&&mp[i][col]!='T')
			break;
	if(i==4) return true;
	else return false;
}

bool dg1(char ch){
	int i,j;
	for (i=0;i<4;++i)
		if(mp[i][i]!=ch && mp[i][i]!='T')
			break;
	for (j=0;j<4;++j)
		if(mp[j][3-j]!=ch && mp[j][3-j]!='T')
		break;
	if(i==4||j==4) return true;
	else return false;

}

void check(char ch)
{
	for (int i=0;i<4;++i)
		if(rowcheck(i,ch)||colcheck(i,ch)){
			flag=(int)ch;
			return;
		}
		if(dg1(ch)) {
			flag=(int)ch;
			return;
		}
}

void solve()
{
	char ch='O';
	check(ch);
	if(flag==(int)ch) return;
	ch='X';
	check(ch);
	if(flag==(int)ch) return;
	bool empty=false;
	rep(i,4) rep(j,4)
		if(mp[i][j]=='.'){
			empty=true;
			flag=0;
			break;
		}
}
int main(){
	int T;
	fop2;
	scanf("%d",&T);
	for (int cas=1;cas<=T;++cas){
		flag=-1;
		for(int i=0;i<4;++i)
			scanf("%s",mp[i]);
		solve();
		printf("Case #%d: ",cas);
		if(flag==-1) 
			printf("Draw\n");
		else if(flag==0)
			printf("Game has not completed\n");
		else 
			printf("%c won\n",(char)flag);
	}
	return 0;
}
