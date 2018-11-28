#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <climits>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>
using namespace std;
typedef long long LL;
const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;

char Mp[20][20];
char read_ch() {
	char ch;
	while (1) {
		ch = getchar();
		if (ch == '.' || ch == 'X' || ch == 'T' || ch == 'O')
			return ch;
	}
	return ch;
}
string Fun(char ch) {
	int i, j, k;
	string ret = "";
	int flag=0;
	for (i = 1; i <= 4; ++i)
		for (j = 1; j <= 4; ++j)
			if (Mp[i][j] == 'T')
				Mp[i][j] = ch;
			else if(Mp[i][j]=='.')
				flag=1;
	for (i = 1; i <= 4; ++i) {
		int n = 0;
		for (j = 1; j <= 4; ++j)
			if (Mp[i][j] == ch) {
				++n;
			} else
				break;
		if (n == 4) {
			ret=ch;
			ret+= " won";
			return ret;
		}
	}
	for (i = 1; i <= 4; ++i) {
		int n = 0;
		for (j = 1; j <= 4; ++j)
			if (Mp[j][i] == ch) {
				++n;
			} else
				break;
		if (n == 4) {
			ret=ch;
			ret+= " won";
			return ret;
		}
	}
	int n=0;
	for(i=1;i<=4;++i)
	{
		if(Mp[i][i]==ch)
			++n;
		else
			break;
		if(n==4)
		{
			ret=ch;
			ret+= " won";
			return ret;
		}
	}
	n=0;
	for(i=1;i<=4;++i)
	{
		if(Mp[i][5-i]==ch)
			++n;
		else
			break;
		if(n==4)
		{
			ret=ch;
			ret+= " won";
			return ret;
		}
	}
	if(flag) return "Game has not completed";
	return "Draw";
}
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int kas=1;kas<=T;++kas)
	{
		int i,j,k;
		memset(Mp,0,sizeof(Mp));
		int nx,ny;
		nx=ny=0;
		for(i=1;i<=4;++i)
		for(j=1;j<=4;++j)
		{
			Mp[i][j]=read_ch();
			if(Mp[i][j]=='X')
			++nx;
			else if(Mp[i][j]=='O')
			++ny;
		}
		printf("Case #%d: ",kas);
		char ch='X';
		if(nx<=ny) ch='O';
		cout << Fun(ch) << endl;
	}
	return 0;
}
