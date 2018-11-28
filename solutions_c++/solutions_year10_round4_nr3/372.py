#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <string.h>
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "C-small-attempt0(2)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}

int mas[111][111],mas2[111][111];
int step()
{
	int res=0;
	for (int i=1;i<=105;i++)
	for (int j=1;j<=105;j++)
	{
		if (mas[i][j])
		{
			res = 1;
			if (mas[i-1][j] || mas[i][j-1])
				mas2[i][j]=1; 
		} else
			if (mas[i-1][j] && mas[i][j-1])
				mas2[i][j]=1; 	
	}
	memcpy(mas,mas2,sizeof(mas));
	memset(mas2,0,sizeof(mas));
	
	return res;
}

int main()
{
	//init();


	

	int tst;
	scanf("%d",&tst);

	for (int cas=1;cas<=tst;cas++)
	{
		int r;
		scanf("%d",&r);
		memset(mas2,0,sizeof(mas2));
		while (r--)
		{
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (int i=x1;i<=x2;i++)
			for (int j=y1;j<=y2;j++)
				mas[i][j]=1;
			
		}
		int res=0;
		while (step()) res++;
		
		printf("Case #%d: %d\n",cas,res);
	
	}
	



	
  return 0;
}
