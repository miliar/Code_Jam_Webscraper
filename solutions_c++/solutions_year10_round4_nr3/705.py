#include <algorithm> 
#include <cassert>
#include <cctype> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <iostream>
#include <map> 
#include <set> 
#include <string> 
#include <sstream>
#include <queue> 
#include <vector> 
using namespace std;

int T, N=110,ans;
vector <vector <int> > mm;

void read()
{
	vector <int> tm;
	tm.resize(N);
	mm.resize(N,tm);
	int R;
	scanf("%d",&R);

	int x1,x2,y1,y2;
	for (int i=0; i<R; i++)
	{
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		for (int i=x1; i<=x2; i++)
			for (int j=y1; j<=y2; j++)
				mm[i][j]=1;
	}
}

bool next()
{
	vector <vector <int> > mnew;
	vector <int> tm;
	tm.resize(N);
	mnew.resize(N,tm);
	int tot=0;
	for (int i=1; i<N; i++)
		for (int j=1; j<N; j++)
		{
			if (mm[i][j]==1)
			{
				if (mm[i-1][j]==0 && mm[i][j-1]==0) mnew[i][j]=0;
				else {mnew[i][j]=1;tot++;}
			}
			else
				if (mm[i-1][j]==1 && mm[i][j-1]==1) {mnew[i][j]=1; tot++;}
				else mnew[i][j]=0;
		}

	mm=mnew;
	return (tot!=0);
}

void solve()
{
	ans=1;
	while (true)
	{
		if (next()) ans++;
		else break;
	}

}

void write(int i)
{
	printf("Case #%d: %d\n",i,ans);


}
int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	char buf[1000];
	string s;


	scanf("%d",&T);
	


	for (int i=0; i<T; i++)
	{
		read();
		solve();
		write(i+1);
	}
	return 0;
}
