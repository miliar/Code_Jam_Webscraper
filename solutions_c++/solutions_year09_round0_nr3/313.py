#include <cstdio>
#include <vector>
#include <iostream>
#include <map>

#define REP(i,n) for(int i=0; i<(n); ++i)
#define pi pair<int,int>
#define mp make_pair

using namespace std;

const char msg[] = "welcome to code jam";

int dy[600][20];
char buf[1024];

int GetDy(int i, int j)
{
//	cout << i << " " << j << endl;
	if(j == 19) return 1;
	if(buf[i] == 0) return 0;
	int &ret = dy[i][j];
	if(ret != -1) return ret;
	ret = 0;
	if(buf[i] == msg[j]) ret = GetDy(i+1,j+1);
	ret += GetDy(i+1,j);
	ret %= 10000;
	return ret;
}

void process(int kase)
{
	fgets(buf,600,stdin);

	REP(i,600)
		REP(j,20) dy[i][j] = -1;

	int val = GetDy(0,0);
	printf("Case #%d: %04d\n",kase,val);
}

int main()
{
	int t;
	scanf("%d\n",&t);
	REP(i,t) process(i+1);
	return 0;
}
