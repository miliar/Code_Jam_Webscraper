#include <map>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <cstring>
#include <utility>
#include <iostream>
#include <algorithm>
#define CASEID printf("Case #%d: ",iD++)
#define CASES  for(scanf("%d",&cases);cases--;)
#define MAX 1001
#define LL long long
using namespace std;

LL C[1001];
int M,N;
string grid[MAX];

void make()
{
	for(char c='0';c<='9';c++) C[c]=c-'0';
	for(char c='A';c<='F';c++) C[c]=c-55;
}

string convert(string tmp,int len) // hex to binary
{
	string ret="";
	LL ans=0;
	for(int i=tmp.length()-1,base=1;i>=0;i--,base*=16)
		ans+=(base*C[tmp[i]]);

	while(ans) {
		if(ans&1) ret="1"+ret;
		else ret="0"+ret;
		ans>>=1;
	}
	while(ret.length()<len)
		ret="0"+ret;
	return ret;
}

void print() {
	for(int i=0;i<M;i++)
		cout<<grid[i]<<endl;
}

bool ok(int x1,int y1,int x2,int y2) // is valid chess board
{
	if(x2-x1 != y2-y1) return false; // not a square
	
	for(int i=x1;i<=x2;i++)
		for(int j=y1;j<y2;j++)
			if(grid[i][j]==grid[i][j+1]) return false;

	for(int i=x1;i<x2;i++)
		for(int j=y1;j<=y2;j++)
			if(grid[i][j]==grid[i+1][j]) return false;

	return true;
}

bool valid(int x1,int y1,int x2,int y2)
{
	for(int i=x1;i<=x2;i++)
		for(int j=y1;j<=y2;j++)
			if(grid[i][j]=='X') return false;
	return true;
}

bool Remove(int x1,int y1,int x2,int y2)
{
	for(int i=x1;i<=x2;i++)
		for(int j=y1;j<=y2;j++)
			grid[i][j]='X';
}

int main()
{
	int cases,iD=1;
	string data;

	make();

	CASES
	{
		cin>>M>>N;
		for(int i=0;i<M;i++)
		{
			cin>>data;
			grid[i]=convert(data,N);
		}
//		print();
		
		int ANS[1001]={0};

		for(int size=min(M,N);size>=0;size--) // try all sized boards
		{
			for(int i=0;i<M;i++)
			{
				for(int j=0;j<N;j++)
				{
					if(i+size<M && j+size<N && valid(i,j,i+size,j+size))
					{
						if(ok(i,j,i+size,j+size))
						{
							Remove(i,j,i+size,j+size);
							ANS[size]++;
						}
					}
				}
			}
		}
		CASEID;
		int cnt=0;
		for(int i=1000;i>=0;i--)
			if(ANS[i]!=0)
				cnt++;
		printf("%d\n",cnt);
		for(int i=1000;i>=0;i--)
			if(ANS[i]!=0)
				printf("%d %d\n",i+1,ANS[i]);
	}

	return 0;
}

