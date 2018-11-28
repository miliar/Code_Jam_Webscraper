#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
bool mk[10][10];
int N,B,Cnt;

inline void Readin()
{
	cin >> N >> B;
}

void DFS(int x,int re,bool mk[][10])
{
	if (x>=re && re) return;
	int c=0,tmp=x;
	bool xx[10][10];
	memcpy(xx,mk,sizeof xx);
	
	while (x)
	{
		++c;
		if (xx[c][x%B]) return;
		xx[c][x%B]=true;
		x/=B;
	}
	
	if (!re) 
	{
		++Cnt;
		return;
	}
	
	for (int y=tmp+1;y<=re;++y)
		DFS(y,re-y,xx);
}

inline void Solve()
{
	Cnt=0;
	for (int i=1;i<=N;++i)
		DFS(i,N-i,mk);
	
	cout << Cnt << endl;
}

int main()
{
	//freopen("i.txt","r",stdin);
	
	int Test,Case=0;
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
